-- Filtro de pandoc para las guías (skill /exportar):
--   1. Las citas en bloque ("> …") que empiezan con una etiqueta conocida se convierten en
--      recuadros de color (estilos "Recuadro …" de plantilla_guia.docx). Las demás quedan como
--      cita normal (estilo "Block Text", con barra gris).
--   2. Salto de página antes de cada sección "## N." con N ≥ 1 (cada pregunta empieza en página
--      nueva) y antes de la primera sección sin número que viene después (glosario, errores…).
--      Se desactiva con la variable de metadatos sin_saltos (exportar.py --sin-saltos).

-- Etiqueta inicial del recuadro → estilo. Se compara con el texto plano del primer párrafo.
local ETIQUETAS = {
  { "^Idea%-fuerza", "Recuadro Idea" },
  { "^Fuente", "Recuadro Fuente" },
  { "^Aviso", "Recuadro Atencion" },
  { "^🔑", "Recuadro Clave" },
  { "^Punto clave", "Recuadro Clave" },
  { "^🎯", "Recuadro Parcial" },
  { "^Para el parcial", "Recuadro Parcial" },
  { "^Para un 10", "Recuadro Parcial" },
  { "^Esqueleto", "Recuadro Esqueleto" },
  { "^🧩", "Recuadro Esqueleto" },
  { "^⚠", "Recuadro Atencion" },
  { "^🚩", "Recuadro Atencion" },
  { "^Atención", "Recuadro Atencion" },
  { "^No confundir", "Recuadro Atencion" },
  { "^Trampa", "Recuadro Atencion" },
  { "^▸", "Recuadro Complemento" },
  { "^Complemento", "Recuadro Complemento" },
}

local function estilo_de(bloque)
  local primero = bloque.content[1]
  if not primero then return nil end
  local texto = pandoc.utils.stringify(primero):gsub("^%s+", "")
  for _, par in ipairs(ETIQUETAS) do
    if texto:find(par[1]) then return par[2] end
  end
  return nil
end

-- En Word, los ítems de una lista conservan el estilo de lista aunque estén dentro del recuadro:
-- se pasan a párrafos con su viñeta o número escritos para que tomen el color del recuadro.
local function aplanar_listas(bloques)
  local out = {}
  for _, b in ipairs(bloques) do
    if b.t == "BulletList" or b.t == "OrderedList" then
      local n = b.t == "OrderedList" and b.listAttributes.start or nil
      for _, item in ipairs(b.content) do
        local marca = n and (tostring(n) .. ". ") or "• "
        local primero = true
        for _, sub in ipairs(aplanar_listas(item)) do
          if primero and (sub.t == "Plain" or sub.t == "Para") then
            local inl = pandoc.List({ pandoc.Str(marca) })
            inl:extend(sub.content)
            table.insert(out, pandoc.Para(inl))
          else
            table.insert(out, sub)
          end
          primero = false
        end
        if n then n = n + 1 end
      end
    else
      table.insert(out, b)
    end
  end
  return out
end

function BlockQuote(bq)
  local estilo = estilo_de(bq)
  if not estilo then return nil end
  return pandoc.Div(aplanar_listas(bq.content), pandoc.Attr("", {}, { ["custom-style"] = estilo }))
end

local SALTO = pandoc.RawBlock("openxml", '<w:p><w:r><w:br w:type="page"/></w:r></w:p>')

function Pandoc(doc)
  if doc.meta.sin_saltos then return doc end
  local bloques, hubo_numerada, cerrado = {}, false, false
  for _, b in ipairs(doc.blocks) do
    if b.t == "Header" and b.level == 2 then
      local n = pandoc.utils.stringify(b.content):match("^(%d+)%.")
      if n and tonumber(n) >= 1 then
        hubo_numerada = true
        table.insert(bloques, SALTO)
      elseif hubo_numerada and not n and not cerrado then
        cerrado = true
        table.insert(bloques, SALTO)
      end
    end
    table.insert(bloques, b)
  end
  doc.blocks = bloques
  return doc
end

return {
  { BlockQuote = BlockQuote },
  { Pandoc = Pandoc },
}
