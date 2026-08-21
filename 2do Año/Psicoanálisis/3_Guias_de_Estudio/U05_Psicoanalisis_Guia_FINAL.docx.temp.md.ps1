
        param([string]$DocPath)
        $word = New-Object -ComObject Word.Application
        $word.Visible = $false
        $doc = $word.Documents.Open($DocPath)
        
        $doc.PageSetup.TopMargin = 36
        $doc.PageSetup.BottomMargin = 36
        $doc.PageSetup.LeftMargin = 36
        $doc.PageSetup.RightMargin = 36
        
        $paragraphs = $doc.Paragraphs
        foreach ($p in $paragraphs) {
            $p.Format.Alignment = 3
        }

        $pageWidth = 523
        $pageHeight = 700

        foreach ($inlineShape in $doc.InlineShapes) {
            if ($inlineShape.Type -eq 3 -or $inlineShape.Type -eq 4 -or $inlineShape.Type -eq 1 -or $inlineShape.Type -eq 24) {
                $altText = $inlineShape.AlternativeText
                if ($altText -and $altText -match 'diagram_ideal_(d+)') {
                    $idealWidth = [float]$matches[1]
                    
                    $shape = $inlineShape.ConvertToShape()
                    $shape.WrapFormat.Type = 7
                    $shape.LockAspectRatio = -1
                    
                    $originalRatio = $shape.Width / $shape.Height
                    $idealHeight = $idealWidth / $originalRatio
                    
                    if ($idealWidth -gt $pageWidth) {
                        $ratio = $pageWidth / $idealWidth
                        $idealWidth = $pageWidth
                        $idealHeight = $idealHeight * $ratio
                    }
                    if ($idealHeight -gt $pageHeight) {
                        $ratio = $pageHeight / $idealHeight
                        $idealHeight = $pageHeight
                        $idealWidth = $idealWidth * $ratio
                    }
                    
                    $shape.Width = [float]$idealWidth
                    $shape.Height = [float]$idealHeight
                    $shape.Left = -999995
                }
            }
        }
        
        $doc.Save()
        $doc.Close()
        $word.Quit()
        