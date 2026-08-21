$word = New-Object -ComObject Word.Application
$word.Visible = $false
$doc = $word.Documents.Open("C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicoanálisis\3_Guias_de_Estudio\U04_Psicoanalisis_Guia_v5.docx")

$shape = $doc.Shapes.Item(1)
Write-Output "Current Shape Width: $($shape.Width)"
$shape.ScaleWidth(1.0, -1) # msoTrue for relative to original size
Write-Output "Shape Width at 100% Original: $($shape.Width)"

$doc.Close(0)
$word.Quit()
