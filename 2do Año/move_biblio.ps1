$source = 'C:\Users\Fmendezcasariego\OneDrive\Carpetas\Desarrollo\psicoanalisis-estudio\biblio-2-cuatrimestre'
$dest = 'C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicoanálisis\2_Textos_Extraidos'

Get-ChildItem -Path $source -Filter *.md | ForEach-Object {
    $name = $_.Name
    if ($name -match '^(\d+)\.\s*([^-]+)\s*-\s*(.+)\.md$') {
        $num = $matches[1].PadLeft(2, '0')
        $autor = $matches[2].Trim() -replace '[^\w\s]', '' -replace '\s+', ''
        
        $tituloLargo = $matches[3].Trim() -replace '[^\w\s]', ''
        $palabras = $tituloLargo -split '\s+'
        $titulo = ($palabras | Select-Object -First 3) -join ''
        
        $newName = "U${num}_${autor}_${titulo}_Crudo.md"
        
        Write-Host "Renaming $name -> $newName"
        Copy-Item -Path $_.FullName -Destination (Join-Path $dest $newName)
    } else {
        Write-Host "Skipping: $name"
    }
}
