$ErrorActionPreference = 'Stop'
$root = 'C:\Users\admin\Desktop\港城莞AI课程\1134-Vision and Images(视觉与图像)'
$out = Join-Path $root '.pdf_convert'

$map = @(
    @{src='week1\lec00_introduction.pptx';                                            pdf='lec00_introduction'},
    @{src='week1\lec01_filtering_for_web.pptx';                                       pdf='lec01_filtering'},
    @{src='week1\Tutorial_01_Python&amp;amp;Image+Processing (1).pptx';               pdf='Tutorial_01_python_basics'},
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

$pp = New-Object -ComObject PowerPoint.Application
$ok = 0; $fail = @()
foreach ($m in $map) {
    $srcPath = Join-Path $root $m.src
    $pdfPath = Join-Path $out ($m.pdf + '.pdf')
    if (Test-Path $pdfPath) { $ok++; Write-Output "SKIP(done): $($m.pdf)"; continue }
    try {
        $pres = $pp.Presentations.Open($srcPath, -1, 0, 0)   # ReadOnly=msoTrue, Untitled/WithWindow=msoFalse
        $pres.SaveAs($pdfPath, 32)                            # 32 = ppSaveAsPDF
        $pres.Close()
        $ok++; Write-Output "OK: $($m.pdf)"
    } catch {
        $fail += $m.pdf; Write-Output "FAIL: $($m.pdf) :: $($_.Exception.Message)"
        try { if ($pres) { $pres.Close() } } catch {}
    }
}
$pp.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($pp) | Out-Null
Write-Output "=== $ok converted, $($fail.Count) failed ==="
if ($fail.Count -gt 0) { $fail | ForEach-Object { Write-Output "  FAILED: $_" } }
