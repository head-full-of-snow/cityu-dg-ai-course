$ErrorActionPreference = 'Continue'
$out = $PSScriptRoot
$root = Split-Path -Parent $PSScriptRoot

$map = @(
    @{src='week2\lec02_edge_for_web.pptx';                                            pdf='lec02_edge'},
    @{src='week2\lec03_resample_for_web.pptx';                                        pdf='lec03_resample'},
    @{src='week2\Tutorial_01_Python&Image Processing.pptx';                           pdf='Tutorial_02_edge_resampling'},
    @{src='week3\lec04_harris_for_web.pptx';                                          pdf='lec04_harris'},
    @{src='week3\lec05_invariance_for_web.pptx';                                      pdf='lec05_invariance'},
    @{src='week3\Tutorial_03_Feature_detection.pptx';                                 pdf='Tutorial_03_feature_detection'},
    @{src='week4\Lecture_Tutorial__4_export\lec06_descriptors_and_matching.pptx';     pdf='lec06_descriptors_matching'},
    @{src='week4\Lecture_Tutorial__4_export\lec07_transformations_for_web.pptx';      pdf='lec07_transformations'},
    @{src='week4\Lecture_Tutorial__4_export\Tutorial_04_Image_Matching_and_Transformations.pptx'; pdf='Tutorial_04_matching_transformations'},
    @{src='week6\lec13_stereo_for_web.pptx';                                          pdf='lec13_stereo'},
    @{src='week6\lec14_mvs_for_web.pptx';                                             pdf='lec14_mvs'},
    @{src='week6\lec15_neural_networks_for_web.pptx';                                 pdf='lec15_neural_networks'},
    @{src='week6\lec16_cnns_Transformers.pptx';                                       pdf='lec16_cnns_transformers'},
    @{src='week6\Tutorial_06_Classfication_and_depth_estimation.pptx';                pdf='Tutorial_06_classification_depth'}
)

Get-ChildItem -Path $root -Recurse -Filter *.pptx | Unblock-File

function Clean-WPS {
    Get-Process wpp -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue
    Start-Sleep -Milliseconds 500
}

$ok = @(); $fail = @()
foreach ($m in $map) {
    $srcPath = Join-Path $root $m.src
    $pdfPath = Join-Path $out ($m.pdf + '.pdf')
    if (Test-Path $pdfPath) { $ok += $m.pdf; Write-Output "SKIP(done): $($m.pdf)"; continue }
    $done = $false
    foreach ($attempt in 1..2) {
        Clean-WPS
        $app = $null; $pres = $null
        try {
            $app = New-Object -ComObject KWPP.Application
            $pres = $app.Presentations.Open($srcPath, $true, $false, ($attempt -eq 2))
            try { $pres.SaveAs($pdfPath, 32) } catch { $pres.ExportAsFixedFormat($pdfPath, 2) }
            if (Test-Path $pdfPath) { $done = $true }
        } catch {
            Write-Output ("  attempt{0} ERR: {1}" -f $attempt, $_.Exception.Message)
            if (Test-Path $pdfPath) { $done = $true }   # saved before crash
        } finally {
            try { $pres.Close() } catch {}
            try { $app.Quit() } catch {}
            try { [Runtime.InteropServices.Marshal]::ReleaseComObject($pres) } catch {}
            try { [Runtime.InteropServices.Marshal]::ReleaseComObject($app) } catch {}
        }
        if ($done) { break }
        Start-Sleep -Seconds 2
    }
    Clean-WPS
    if ($done) { $ok += $m.pdf; Write-Output "OK: $($m.pdf)" }
    else { $fail += $m.pdf; Write-Output "FAIL: $($m.pdf)" }
}
Write-Output "=== $($ok.Count) converted, $($fail.Count) failed ==="
$fail | ForEach-Object { Write-Output "  FAILED: $_" }
