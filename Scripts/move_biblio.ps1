<#
.SYNOPSIS
    Copia textos extraídos (.md) a 2_Textos_Extraidos/ con la nomenclatura de AGENTS.md.

.DESCRIPTION
    Toma archivos con el formato de la cátedra "NN. Autor - Título.md" y los copia como
    "[Unidad]_T[NN]_[Autor]_[Titulo]_Crudo.md", por ejemplo:

        "15. Freud - Duelo y melancolía.md"  ->  "U04_T15_Freud_DueloYMelancolia_Crudo.md"

    Autor y título se pasan a PascalCase sin acentos ni signos, y nunca se cortan palabras
    por la mitad. Los archivos que no siguen el formato se informan y se saltean.

.PARAMETER Origen
    Carpeta con los .md a copiar.

.PARAMETER Destino
    Carpeta 2_Textos_Extraidos de la materia. Se crea si no existe.

.PARAMETER Unidad
    Código de unidad o clase de dos dígitos: U04, C12, etc.

.PARAMETER MaxPalabras
    Cantidad máxima de palabras del título (0 = título completo). Recorta palabras enteras.

.PARAMETER Force
    Sobrescribe archivos que ya existan en el destino.

.EXAMPLE
    .\Scripts\move_biblio.ps1 -Origen "C:\descargas\biblio-2c" -Destino ".\2do Año\Psicoanálisis\2_Textos_Extraidos" -Unidad U04 -WhatIf
#>
[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [Parameter(Mandatory = $true)] [string] $Origen,
    [Parameter(Mandatory = $true)] [string] $Destino,
    [Parameter(Mandatory = $true)] [ValidatePattern('^[UC]\d{2}$')] [string] $Unidad,
    [ValidateRange(0, 50)] [int] $MaxPalabras = 0,
    [switch] $Force
)

function ConvertTo-PascalCase([string] $texto, [int] $max) {
    # Quita acentos (á -> a, ñ -> n) y deja solo letras y números separados por espacios
    $sinAcentos = -join ($texto.Normalize([Text.NormalizationForm]::FormD).ToCharArray() |
        Where-Object { [Globalization.CharUnicodeInfo]::GetUnicodeCategory($_) -ne 'NonSpacingMark' })
    $palabras = @(($sinAcentos -replace '[^\p{L}\p{N}]+', ' ').Trim() -split '\s+' | Where-Object { $_ })
    if ($max -gt 0 -and $palabras.Count -gt $max) { $palabras = $palabras[0..($max - 1)] }
    return -join ($palabras | ForEach-Object { $_.Substring(0, 1).ToUpper() + $_.Substring(1) })
}

if (-not (Test-Path -LiteralPath $Origen -PathType Container)) {
    throw "No existe la carpeta de origen: $Origen"
}
if (-not (Test-Path -LiteralPath $Destino)) {
    if ($PSCmdlet.ShouldProcess($Destino, 'Crear carpeta')) {
        New-Item -ItemType Directory -Path $Destino | Out-Null
    }
}

Get-ChildItem -LiteralPath $Origen -Filter *.md | ForEach-Object {
    $name = $_.Name
    if ($name -match '^(\d+)\.\s*([^-]+?)\s*-\s*(.+)\.md$') {
        $num = $matches[1].PadLeft(2, '0')
        $autor = ConvertTo-PascalCase $matches[2] 0
        $titulo = ConvertTo-PascalCase $matches[3] $MaxPalabras

        $newName = "${Unidad}_T${num}_${autor}_${titulo}_Crudo.md"
        $target = Join-Path $Destino $newName

        if ((Test-Path -LiteralPath $target) -and -not $Force) {
            Write-Warning "Ya existe, se saltea (usar -Force para sobrescribir): $newName"
        } elseif ($PSCmdlet.ShouldProcess($newName, "Copiar desde $name")) {
            Copy-Item -LiteralPath $_.FullName -Destination $target -Force:$Force
            Write-Host "$name -> $newName"
        }
    } else {
        Write-Warning "No sigue el formato 'NN. Autor - Título.md', se saltea: $name"
    }
}
