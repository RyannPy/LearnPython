import asyncio
from pyscript import window

lirik = [
    ("Dulu masih kici, kici, kici.. Nona", 2),
    ("Sekarang bale Jawa makin cantik.. Nona", 2),
    ("Ko perfect sekali, asli bidadari jatuh dari langit", 4.7),
    ("Kalau jadi deng Ade, kaka stop bamabo to", 2.7),
    ("Su pasti kaka ni Ade pu jodoh", 1.8),
    ("Sumpah ni ja'o sodho, iwa mbodho", 2)
]

async def ketik_perlahan(teks, durasi_total):
    elemen = window.document.getElementById("lirik")
    elemen.textContent = ""  
    jeda_huruf = durasi_total / len(teks)
    for huruf in teks:
        elemen.textContent += huruf
        await asyncio.sleep(jeda_huruf)

async def mulai():
    for baris, durasi_total in lirik:
        await ketik_perlahan(baris, durasi_total)
        await asyncio.sleep(0.5)

asyncio.ensure_future(mulai())
