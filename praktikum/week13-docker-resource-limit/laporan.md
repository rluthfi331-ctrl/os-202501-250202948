
# Laporan Praktikum Minggu 13
Topik: Docker – Resource Limit (CPU & Memori)

---

## Identitas
- **Nama**  : LUTHFI AULIA RAHMAN 
- **NIM**   : 250202948
- **Kelas** : 1 IKRB

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:

1. Menulis Dockerfile sederhana untuk sebuah aplikasi/skrip.
2. Membangun image dan menjalankan container.
3. Menjalankan container dengan pembatasan CPU dan memori.
4. Mengamati dan menjelaskan perbedaan eksekusi container dengan dan tanpa limit resource.
5. Menyusun laporan praktikum secara runtut dan sistematis.

---

## Dasar Teori
1. Limitasi Memori (RAM)
- Hard Limit (--memory): Batas mati. Kalau container pake RAM lebih dari ini, dia langsung kena OOM Kill alias dimatiin paksa sama sistem.

- Soft Limit (--memory-reservation): Batas "sopan". Container boleh lewat batas ini kalau server lagi senggang, tapi bakal disuruh turun kalau server mulai penuh.

2. Limitasi CPU
- CPU Shares: Pakai sistem prioritas/bobot. Berguna kalau lagi rebutan CPU sama container lain.

- CPU Quota (--cpus): Jatah Core yang pasti. Misalnya kita set 0.5, berarti container cuma boleh pakai setengah dari kekuatan 1 Core CPU.

- CPU Pinning: Kita nentuin container ini harus jalan di Core nomor berapa (misal: Core 0 atau Core 1 aja).

---

## Langkah Praktikum
1. Persiapan Lingkungan

- Pastikan Docker terpasang dan berjalan.
- Verifikasi:
```
docker version
docker ps
```
2. Membuat Aplikasi/Skrip Uji

Buat program sederhana di folder code/ (bahasa bebas) yang:

- Melakukan komputasi berulang (untuk mengamati limit CPU), dan/atau
- Mengalokasikan memori bertahap (untuk mengamati limit memori).
Membuat Dockerfile

3. Tulis Dockerfile untuk menjalankan program uji.
Build image:
docker build -t week13-resource-limit .
Menjalankan Container Tanpa Limit

4. Jalankan container normal:
docker run --rm week13-resource-limit
Catat output/hasil pengamatan.
Menjalankan Container Dengan Limit Resource

5. Jalankan container dengan batasan resource (contoh):

```
docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
```
- Catat perubahan perilaku program (mis. lebih lambat, error saat memori tidak cukup, dll.).

6. Monitoring Sederhana

- Jalankan container (tanpa --rm jika perlu) dan amati penggunaan resource:
```
docker stats
```
- Ambil screenshot output eksekusi dan/atau docker stats.
7. Commit & Push
```
git add .
git commit -m "Minggu 13 - Docker Resource Limit"
git push origin main
```
---

## Kode / Perintah
 Tuliskan potongan kode atau perintah utama:
 python
 ```
 FROM python:3.9-slim
WORKDIR /app
COPY app.py .
CMD ["python", "app.py"]

# Membangun image dari folder code
docker build -t week13-resource-limit .

# Menjalankan dengan pembatasan RAM 200MB dan CPU 0.5
docker run --rm --cpus="0.5" --memory="200m" week13-resource-limit

```

---

## Hasil Eksekusi
![screenshot1](https://github.com/user-attachments/assets/e1c74774-fc7b-4b61-bb3e-792c6574618a)
![screenshot2](https://github.com/user-attachments/assets/28430d9d-7583-4ee8-b777-819f1773bade)
![screenshot3](https://github.com/user-attachments/assets/1351b169-b439-47a2-a152-acee322719da)
![screenshot4](https://github.com/user-attachments/assets/bbca0b31-a5c6-4136-a0f4-906d26d8ce07)





---

## Analisis
Program berjalan normal saat Docker tidak diberi batasan CPU dan memori, bahkan bisa menggunakan RAM hingga 500 MB. Namun, ketika dijalankan dengan limit CPU 0.5 core dan RAM 200 MB, container langsung berhenti karena kebutuhan memori melebihi batas. Hal ini menunjukkan bahwa pengaturan resource limit di Docker sangat memengaruhi jalannya aplikasi.

---

## Kesimpulan
Dockerfile berhasil digunakan untuk membangun image dan menjalankan aplikasi Python dengan baik. Saat container dijalankan tanpa batasan resource, program dapat berjalan normal. Namun, ketika container dijalankan dengan pembatasan CPU 0.5 core dan RAM 200 MB, kinerja aplikasi menjadi terbatas dan berpotensi berhenti jika kebutuhan memori melebihi batas. Hal ini menunjukkan bahwa pengaturan resource limit pada Docker sangat berpengaruh terhadap jalannya dan kestabilan aplikasi.

---

## Quiz
1. Mengapa container perlu dibatasi CPU dan memori?

   jawaban:

   Kenapa Container Harus Dibatasi?
-  Mencegah Efek "Noisy Neighbor": Biar nggak ada satu container yang "maruk" makan semua RAM/CPU, yang bisa bikin container lain di server yang sama jadi lemot atau mati.

-  Menjaga Stabilitas Server (Host): Biar server utama lo nggak freeze atau hang. Kalau RAM server habis total, Linux bakal otomatis matiin proses secara acak (OOM Kill), dan itu bahaya buat OS.

-  Isolasi Error: Kalau ada aplikasi yang error (misal: memory leak), efeknya cuma bakal ngerusak container itu sendiri, nggak merembet ke mana-mana.

-  Prediksi Performa: Biar lo tahu pasti tiap layanan dapet jatah berapa, jadi performa aplikasi lebih stabil dan nggak naik-turun gara-gara rebutan resource.

2. Apa perbedaan VM dan container dalam konteks isolasi resource?

   jawaban:
- VM itu isolasi hardware (berat tapi sangat aman).

- Container itu isolasi proses (ringan tapi bagi-bagi kernel).

3. Apa dampak limit memori terhadap aplikasi yang boros memori?

   jawaban:
 - OOMKilled (Mati Total): Begitu aplikasi lo nyentuh batas "Hard Limit" yang lo set, si Docker bakal langsung ngebunuh container itu. Statusnya bakal jadi Exited (137). Ini cara Docker nyelametin server biar nggak ikut hang.

- Throttling/Lemot Parah: Kalau ada sisa ruang di swap (disk), aplikasi nggak bakal langsung mati, tapi datanya dipindah ke disk. Karena disk jauh lebih lambat dari RAM, aplikasi lo bakal berasa "nge-lag" parah atau nggak ngerespon.



## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
