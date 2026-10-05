[Windows.System.UserProfile.GlobalizationPreferences,Windows.System.UserProfile,ContentType=WindowsRuntime] | Out-Null
[Windows.Media.Ocr.OcrEngine,Windows.Foundation.UniversalApiContract,ContentType=WindowsRuntime] | Out-Null
[Windows.Graphics.Imaging.BitmapDecoder,Windows.Foundation.UniversalApiContract,ContentType=WindowsRuntime] | Out-Null

$lang = [Windows.System.UserProfile.GlobalizationPreferences]::Languages[0]
$engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromLanguage($lang)

foreach ($img in 1..3) {
    $file = Get-Item ".\media\image$img.png"
    $stream = $file.OpenRead()
    $decoderTask = [Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)
    $decoderTask.AsTask().Wait()
    $decoder = $decoderTask.GetResults()

    $softwareBitmapTask = $decoder.GetSoftwareBitmapAsync()
    $softwareBitmapTask.AsTask().Wait()
    $softwareBitmap = $softwareBitmapTask.GetResults()

    $ocrTask = $engine.RecognizeAsync($softwareBitmap)
    $ocrTask.AsTask().Wait()
    $ocrResult = $ocrTask.GetResults()

    Write-Host "--- Image $img ---"
    Write-Host $ocrResult.Text
    $stream.Dispose()
}
