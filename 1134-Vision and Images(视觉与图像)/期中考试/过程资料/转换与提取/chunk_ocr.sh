#!/bin/bash
cd "C:/Users/admin/Desktop/港城莞AI课程/1134-Vision and Images(视觉与图像)" || exit 1
SKILL="C:/Users/admin/.claude/skills/pdf-ocr/scripts/extract_pdf.py"
PARTS=".pdf_convert/parts"
TMP=".pdf_convert/tmp_chunk"
mkdir -p "$PARTS" "$TMP"
mv .pdf_convert/parts_test/lec00_1_8.md "$PARTS/lec00_introduction_p1.md" 2>/dev/null
mv .pdf_convert/parts_test/lec00_9_16.md "$PARTS/lec00_introduction_p2.md" 2>/dev/null

declare -A PAGES=(
  [lec00_introduction]=50
  [lec01_filtering]=39
  [lec02_edge]=30
  [lec03_resample]=38
  [lec04_harris]=49
  [lec05_invariance]=31
  [lec06_descriptors_matching]=46
  [lec07_transformations]=41
  [lec13_stereo]=37
  [lec14_mvs]=34
  [lec15_neural_networks]=61
  [lec16_cnns_transformers]=55
)

for name in lec00_introduction lec01_filtering lec02_edge lec03_resample lec04_harris lec05_invariance lec06_descriptors_matching lec07_transformations lec13_stereo lec14_mvs lec15_neural_networks lec16_cnns_transformers; do
  total=${PAGES[$name]}
  nchunks=$(( (total + 7) / 8 ))
  for i in $(seq 1 $nchunks); do
    a=$(( (i-1)*8 + 1 )); b=$(( i*8 )); [ $b -gt $total ] && b=$total
    part="$PARTS/${name}_p${i}.md"
    [ -f "$part" ] && { echo "SKIP $name p$a-$b"; continue; }
    ok=0
    for try in 1 2; do
      rm -f "$TMP/${name}.md"
      if timeout 150 python "$SKILL" ".pdf_convert/${name}.pdf" --pages ${a}-${b} -o "$TMP" >/dev/null 2>&1 && [ -f "$TMP/${name}.md" ]; then
        mv "$TMP/${name}.md" "$part"; ok=1; break
      fi
      sleep 3
    done
    if [ $ok -eq 1 ]; then echo "OK $name p$a-$b"; else echo "FAIL $name p$a-$b"; fi
  done
  have=$(ls "$PARTS/${name}_p"*.md 2>/dev/null | wc -l)
  if [ "$have" -eq "$nchunks" ]; then
    ls "$PARTS/${name}_p"*.md | sort -V | xargs cat > "期中考试/课件OCR_MD/${name}.md"
    echo "CONCAT $name"
  else
    echo "INCOMPLETE $name ($have/$nchunks)"
  fi
done
echo "=== CHUNK PIPELINE DONE ==="
