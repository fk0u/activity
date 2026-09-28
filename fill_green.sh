#!/bin/bash
# Isi grafik kontribusi GitHub dari 1 November 2025 sampai hari ini (versi macOS).
# Jalankan di dalam folder repo hasil clone, lalu `git push`.

start="2025-11-01"
end=$(date +%Y-%m-%d)
d="$start"
total=0

while [[ "$d" < "$end" || "$d" == "$end" ]]; do
  n=$((RANDOM % 4 + 1))   # 1-4 commit per hari, biar warnanya bervariasi
  for ((i = 0; i < n; i++)); do
    t=$(printf "%sT%02d:%02d:00" "$d" $((RANDOM % 14 + 9)) $((RANDOM % 60)))
    echo "$t" >> activity.log
    git add activity.log
    GIT_AUTHOR_DATE="$t" GIT_COMMITTER_DATE="$t" git commit -q -m "update $d"
    total=$((total + 1))
  done
  d=$(date -j -v+1d -f "%Y-%m-%d" "$d" "+%Y-%m-%d")
done

echo "Selesai: $total commit dari $start sampai $end. Sekarang jalankan: git push"