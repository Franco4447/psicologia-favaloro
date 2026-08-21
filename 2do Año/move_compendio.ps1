$source = 'C:\Users\Fmendezcasariego\OneDrive\Carpetas\Desarrollo\psicoanalisis-estudio\compendio'
$dest = 'C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicoanálisis\3_Guias_de_Estudio'

Get-ChildItem -Path $source -Filter *.md | ForEach-Object {
    $name = $_.Name
    if ($name -match '^clase_(\d+.*)\.md$') {
        $num = $matches[1]
        $newName = "U${num}_Clase_Guia.md"
        Write-Host "Renaming $name -> $newName"
        Copy-Item -Path $_.FullName -Destination (Join-Path $dest $newName)
    } elseif ($name -match '^00_global.*\.md$') {
        $newName = "U00_Global_Guia.md"
        Write-Host "Renaming $name -> $newName"
        Copy-Item -Path $_.FullName -Destination (Join-Path $dest $newName)
    } elseif ($name -match '^psicosis\.md$') {
        $newName = "U99_Psicosis_Guia.md"
        Write-Host "Renaming $name -> $newName"
        Copy-Item -Path $_.FullName -Destination (Join-Path $dest $newName)
    } else {
        Write-Host "Skipping: $name"
    }
}
