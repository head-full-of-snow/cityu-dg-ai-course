$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$src = Join-Path $root 'week1\lec00_introduction.pptx'
$pdf = Join-Path $PSScriptRoot 'lec00_introduction.pdf'

try { $app = New-Object -ComObject KWPP.Application } catch { Write-Output ("create ERR: " + $_.Exception.Message); exit 1 }
Write-Output 'KWPP created'

try {
    $pres = $app.Presentations.Open($src, $true, $false, $false)
    Write-Output ('opened, slides=' + $pres.Slides.Count)
    try {
        $pres.SaveAs($pdf, 32)
        Write-Output 'SaveAs(32) done'
    } catch {
        Write-Output ('SaveAs32 ERR: ' + $_.Exception.Message)
        $pres.ExportAsFixedFormat($pdf, 2)   # ppFixedFormatTypePDF
        Write-Output 'ExportAsFixedFormat done'
    }
    $pres.Close()
} catch { Write-Output ('ERR: ' + $_.Exception.Message) }
finally { try { $app.Quit() } catch {} }

if (Test-Path $pdf) {
    $fi = Get-Item $pdf
    Write-Output ('PDF OK: ' + $fi.Length + ' bytes')
} else { Write-Output 'PDF MISSING' }
