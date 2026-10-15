#!/bin/bash
cd "C:/Users/admin/Desktop/港城莞AI课程/1134-Vision and Images(视觉与图像)" || exit 1
SKILL="C:/Users/admin/.claude/skills/pdf-ocr/scripts/extract_pdf.py"
PARTS=".pdf_convert/parts2"
TMP=".pdf_convert/tmp_chunk2"
PROBE=".pdf_convert/probe"
mkdir -p "$PARTS" "$TMP" "$PROBE"

probe_ok() {
  rm -f "$PROBE/probe.md"
  timeout 240 python "$SKILL" "$PROBE/probe.pdf" -o "$PROBE" >/dev/null 2>&1
  [ -f "$PROBE/probe.md" ]
}

# wait for service recovery, probe every 5 min
until probe_ok; do
  echo "[$(date +%H:%M:%S)] service still down, sleeping 300s..."
  sleep 300
done
echo "[$(date +%H:%M:%S)] service RECOVERED, starting full pass"

for pass in 1 2 3; do
  todo=0
  for pdf in .pdf_convert/chunks/*.pdf; do
    base=$(basename "$pdf" .pdf)
    part="$PARTS/${base}.md"
    [ -f "$part" ] && continue
    todo=$((todo+1))
  done
  [ $todo -eq 0 ] && break
  echo "=== pass $pass: $todo chunks to go ==="

  for pdf in .pdf_convert/chunks/*.pdf; do
    base=$(basename "$pdf" .pdf)
    part="$PARTS/${base}.md"
    [ -f "$part" ] && { echo "SKIP $base"; continue; }
    ok=0
    for try in 1 2; do
      rm -f "$TMP/${base}.md"
      if timeout 420 python "$SKILL" "$pdf" -o "$TMP" >/dev/null 2>&1 && [ -f "$TMP/${base}.md" ]; then
        mv "$TMP/${base}.md" "$part"; ok=1; break
      fi
      sleep 30
    done
    if [ $ok -eq 1 ]; then echo "OK $base"; else echo "FAIL $base"; fi
  done
done

echo "=== concat phase ==="
for name in lec00_introduction lec01_filtering lec02_edge lec03_resample lec04_harris lec05_invariance lec06_descriptors_matching lec07_transformations lec13_stereo lec14_mvs lec15_neural_networks lec16_cnns_transformers; do
  total=$(ls .pdf_convert/chunks/${name}_c*.pdf 2>/dev/null | wc -l)
  have=$(ls "$PARTS/${name}_c"*.md 2>/dev/null | wc -l)
  if [ "$have" -eq "$total" ] && [ "$total" -gt 0 ]; then
    ls "$PARTS/${name}_c"*.md | sort -V | xargs cat > "期中考试/课件OCR_MD/${name}.md"
    echo "CONCAT $name"
  else
    echo "INCOMPLETE $name ($have/$total)"
  fi
done
echo "=== SUPERVISOR DONE ==="
ls "$PARTS" | wc -l
