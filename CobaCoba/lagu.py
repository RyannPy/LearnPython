import time
import sys

lirik = [
    "Ku mulai lagu ini dengan bernyanyi, dududududududu",
    "Waktu berhenti khayal menari-nari, hanyut kedalam senyummu..",
    "Tak peduli.., langit menertawakanku",
    "Kau mencuri..., hatiku mimpiku semua hidupku."
]

def ketik_perlahan(teks, jeda=0.1):
    for huruf in teks:
        sys.stdout.write(huruf)
        sys.stdout.flush()
        time.sleep(jeda)
    print()  # Pindah ke baris baru

for baris in lirik:
    ketik_perlahan(baris)
    time.sleep(1)  # Jeda antar baris