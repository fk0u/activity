"""
Isi grafik kontribusi GitHub dari 1 November 2025 sampai hari ini.
Jalankan di dalam folder repo hasil clone, lalu `git push`.
"""
import os
import random
import subprocess
from datetime import date, timedelta

START = date(2025, 11, 1)
END = date.today()
MIN_COMMITS, MAX_COMMITS = 1, 4  # jumlah commit per hari (acak, biar warnanya bervariasi)
LOG_FILE = "activity.log"

hari = START
total = 0
while hari <= END:
    for _ in range(random.randint(MIN_COMMITS, MAX_COMMITS)):
        waktu = f"{hari.isoformat()}T{random.randint(9, 22):02d}:{random.randint(0, 59):02d}:00"
        env = {**os.environ, "GIT_AUTHOR_DATE": waktu, "GIT_COMMITTER_DATE": waktu}
        with open(LOG_FILE, "a") as f:
            f.write(waktu + "\n")
        subprocess.run(["git", "add", LOG_FILE], check=True)
        subprocess.run(["git", "commit", "-q", "-m", f"update {hari}"], env=env, check=True)
        total += 1
    hari += timedelta(days=1)

print(f"Selesai: {total} commit dari {START} sampai {END}. Sekarang jalankan: git push")