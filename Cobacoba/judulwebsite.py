import requests
from bs4 import BeautifulSoup

url = input("Masukkan URL: ")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Ambil judul
    title = soup.title.string if soup.title else "Tidak ditemukan"

    # Cari meta tag author
    author_meta = soup.find("meta", attrs={"name": "author"})
    author = author_meta["content"] if author_meta else "Tidak ditemukan"

    print("Judul halaman:", title)
    print("Penulis:", author)
else:
    print("Gagal mengakses halaman, status code:", response.status_code)