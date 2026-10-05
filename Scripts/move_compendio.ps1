<#
.SYNOPSIS
    Copia guías de un compendio a 3_Guias_de_Estudio/ con la nomenclatura de AGENTS.md.

.DESCRIPTION
    Renombra al copiar:
        clase_1.md / clase_01.md   ->  C01_Guia.md        (provisional: falta el tema)
        clase_17_18.md             ->  C17_18_Guia.md
        00_global*.md              ->  Global_[Cuatrimestre]_Guia.md  (o Global_Guia.md)
        psicosis.md                ->  Transversal_Psicosis_Guia.md
    Los demás archivos se informan y se saltean.

    OJO: las guías de clase salen como C[NN]_Guia.md, sin tema, y AGENTS.md pide
    C[NN]_[Tema]_Guia.md. El script no puede saber el tema: avisa por cada guía y hay que
    renombrarlas después (el tema sale del título `#` de la guía; validar con
    python Scripts/estudio/nombres.py validar <archivo>).

.PARAMETER Origen
    Carpeta del compendio con los .md.

.PARAMETER Destino
    Carpeta 3_Guias_de_Estudio de la materia. Se crea si no existe.

.PARAMETER Cuatrimestre
    Opcional: 1erC o 2doC, para nombrar la guía global.

.PARAMETER Force
    Sobrescribe archivos que ya existan en el destino.

.EXAMPLE
    .\Scripts\move_compendio.ps1 -Origen "C:\descargas\compendio" -Destino ".\2do Año\Psicoanálisis\3_Guias_de_Estudio" -Cuatrimestre 2doC -WhatIf
#>
[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [Parameter(Mandatory = $true)] [string] $Origen,
    [Parameter(Mandatory = $true)] [string] $Destino,
    [ValidateSet('1erC', '2doC')] [string] $Cuatrimestre,
    [switch] $Force
)

if (-not (Test-Path -LiteralPath $Origen -PathType Container)) {
    throw "No existe la carpeta de origen: $Origen"
}
if (-not (Test-Path -LiteralPath $Destino)) {
    if ($PSCmdlet.ShouldProcess($Destino, 'Crear carpeta')) {
        New-Item -ItemType Directory -Path $Destino | Out-Null
    }
}

$global = if ($Cuatrimestre) { "Global_${Cuatrimestre}_Guia.md" } else { 'Global_Guia.md' }

Get-ChildItem -LiteralPath $Origen -Filter *.md | ForEach-Object {
    $name = $_.Name
    $newName = $null
    $sinTema = $false
    if ($name -match '^clase_(\d+(?:_\d+)*)\.md$') {
        # Cada número con dos dígitos: clase_7 -> C07, clase_17_18 -> C17_18
        $nums = ($matches[1] -split '_' | ForEach-Object { $_.PadLeft(2, '0') }) -join '_'
        $newName = "C${nums}_Guia.md"
        $sinTema = $true
    } elseif ($name -match '^00_global.*\.md$') {
        $newName = $global
    } elseif ($name -match '^psicosis\.md$') {
        $newName = 'Transversal_Psicosis_Guia.md'
    }

    if (-not $newName) {
        Write-Warning "Formato no reconocido, se saltea: $name"
        return
    }
    $target = Join-Path $Destino $newName
    if ((Test-Path -LiteralPath $target) -and -not $Force) {
        Write-Warning "Ya existe, se saltea (usar -Force para sobrescribir): $newName"
    } elseif ($PSCmdlet.ShouldProcess($newName, "Copiar desde $name")) {
        Copy-Item -LiteralPath $_.FullName -Destination $target -Force:$Force
        Write-Host "$name -> $newName"
        if ($sinTema) {
            Write-Warning "$newName no tiene tema en el nombre: renombrar a C${nums}_[Tema]_Guia.md (AGENTS.md)"
        }
    }
}
