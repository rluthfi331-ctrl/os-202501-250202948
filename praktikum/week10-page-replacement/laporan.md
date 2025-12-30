
# Laporan Praktikum Minggu 10
Topik: Manajemen Memori – Page Replacement (FIFO & LRU)

---

## Identitas
- **Nama**  : LUTHFI AULIA RAHMAN 
- **NIM**   : 250202948
- **Kelas** : 1 IKRB

---

## Tujuan
1. Mengimplementasikan algoritma page replacement FIFO dalam program.
2. Mengimplementasikan algoritma page replacement LRU dalam program.
3. Menjalankan simulasi page replacement dengan dataset tertentu.
4. Membandingkan performa FIFO dan LRU berdasarkan jumlah page fault.
5. Menyajikan hasil simulasi dalam laporan yang sistematis.

---

## Dasar Teori
Dalam sistem operasi, Page Replacement bertugas mencari ruang di RAM yang penuh dengan cara menukar data (page) lama ke disk agar data baru bisa masuk. Kejadian saat data tidak ditemukan di RAM disebut Page Fault.


1. FIFO (First-In, First-Out)
Konsep: Data yang pertama kali masuk adalah yang pertama kali keluar.

Logika: Seperti antrean, tidak peduli sesering apa data itu dipakai, kalau dia yang paling senior, dia yang diusir.

Karakteristik: Sangat simpel tapi kurang efisien.

2. LRU (Least Recently Used)
Konsep: Data yang paling lama tidak digunakan adalah yang akan dikeluarkan.

Logika: Melihat riwayat pemakaian. Kalau data baru saja dipakai, kemungkinan besar akan dipakai lagi (tetap di RAM).

Karakteristik: Lebih cerdas dan biasanya menghasilkan Page Fault yang lebih sedikit.


## Langkah Praktikum
1. Membuat folder praktikum/week10-page-replacement/ dengan subfolder code dan screenshots

2. Membuat file reference_string.txt berisi data uji: 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2 dan menetapkan jumlah frame = 3.

3. Membuat program Python (page_replacement.py) yang membaca file dataset, mensimulasikan antrian frame untuk FIFO, dan stack penggunaan untuk LRU.

4. Menjalankan program di terminal dan mencatat setiap kali status MISS (Page Fault) terjadi.

5. Mendokumentasikan seluruh hasil simulasi, perhitungan dan analisis dalam file laporan md

   

6. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 10 - Page Replacement FIFO & LRU"
   git push origin main
   ```


---

## Kode / Perintah
```python
def cetak_langkah(step, page, status, frames):
    print(f"Langkah [{step:02d}] | Page: {page} | Status: {status:4} | Frames: {list(frames)}")

def main():
    # Dataset dan konfigurasi frame
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    jumlah_frame = 3

    # === 1. SIMULASI FIFO ===
    print("\n--- HASIL SIMULASI FIFO ---")
    frames_fifo = []
    fifo_faults = 0
    pointer = 0

    for i, page in enumerate(pages):
        status = "HIT"
        if page not in frames_fifo:
            status = "MISS"
            fifo_faults += 1
            if len(frames_fifo) < jumlah_frame:
                frames_fifo.append(page)
            else:
                frames_fifo[pointer] = page
                pointer = (pointer + 1) % jumlah_frame
        cetak_langkah(i + 1, page, status, frames_fifo)
    print(f"Total Page Faults FIFO: {fifo_faults}")

    # === 2. SIMULASI LRU ===
    print("\n--- HASIL SIMULASI LRU ---")
    frames_lru = []
    lru_faults = 0

    for i, page in enumerate(pages):
        status = "HIT"
        if page in frames_lru:
            # Jika HIT, pindahkan page ke posisi paling baru (belakang)
            frames_lru.remove(page)
            frames_lru.append(page)
        else:
            status = "MISS"
            lru_faults += 1
            if len(frames_lru) < jumlah_frame:
                frames_lru.append(page)
            else:
                # Buang yang paling lama tidak digunakan (paling depan)
                frames_lru.pop(0)
                frames_lru.append(page)
        cetak_langkah(i + 1, page, status, frames_lru)
    print(f"Total Page Faults LRU : {lru_faults}")

    # === 3. RINGKASAN PERBANDINGAN ===
    print("\n" + "="*30)
    print(f"PERBANDINGAN AKHIR")
    print(f"FIFO Page Faults: {fifo_faults}")
    print(f"LRU Page Faults : {lru_faults}")
    print("="*30)
    
    if lru_faults < fifo_faults:
        print(">> Algoritma LRU lebih efisien pada dataset ini.")
    elif fifo_faults < lru_faults:
        print(">> Algoritma FIFO lebih efisien pada dataset ini.")
    else:
        print(">> Kedua algoritma memiliki efisiensi yang sama.")

if __name__ == "__main__":
    main()

```

---

## Hasil Eksekusi
![alt text](<Screenshot 2025-12-29 204750.png>)
---

## Analisis
Berdasarkan hasil eksekusi program pada dataset 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2 dengan 3 frame memori, didapatkan perbandingan sebagai berikut:

- Algoritma FIFO (First-In First-Out)

- Total Page Faults: 10 kali.

- Karakteristik: FIFO hanya mengeluarkan data berdasarkan urutan masuk. Pada langkah ke-4 (saat angka 2 masuk), FIFO mengeluarkan angka 7 karena ia yang paling pertama masuk, tanpa peduli apakah angka 7 akan dibutuhkan lagi dalam waktu dekat atau tidak.

- Algoritma LRU (Least Recently Used)

- Total Page Faults: 9 kali.

- Karakteristik: LRU lebih efisien karena ia melihat riwayat pemakaian. Saat memori penuh, LRU memilih mengeluarkan data yang sudah paling lama tidak diakses oleh sistem. Ini terbukti efektif karena pada dataset ini, LRU berhasil mempertahankan data yang masih sering digunakan, sehingga jumlah "MISS" (Page Fault) lebih sedikit.


## Kesimpulan
1. Page Fault sangat dipengaruhi oleh pemilihan algoritma penggantian halaman. Semakin efisien algoritma, semakin sedikit pula gangguan (interrupt) yang terjadi pada sistem.

2. Algoritma FIFO memiliki keunggulan pada kesederhanaan implementasi, namun sering kali kurang efisien karena tidak mempertimbangkan frekuensi atau waktu pemakaian data.

3. Algoritma LRU terbukti lebih optimal dalam simulasi ini dengan jumlah 9 Page Faults, dibandingkan FIFO yang berjumlah 10 Page Faults.

4. Secara keseluruhan, LRU merupakan pilihan yang lebih baik untuk sistem yang membutuhkan performa tinggi karena mampu mempertahankan data yang masih aktif digunakan di dalam RAM.

---

## Quiz
1. Mengapa FIFO dapat menghasilkan Belady’s Anomaly?

jawaban:

FIFO:

Kriteria: Berdasarkan urutan masuk.

Logika: Siapa yang paling lama di RAM, dia yang dibuang duluan.

Hasil: Kurang efektif karena sering menghapus data yang sebenarnya masih dipakai.

LRU:

Kriteria: Berdasarkan riwayat pemakaian.

Logika: Siapa yang paling lama tidak disentuh/dipakai CPU, dia yang dibuang.

Hasil: Lebih cerdas dan jumlah Page Fault biasanya lebih sedikit.

2. Mengapa FIFO dapat menghasilkan Belady’s Anomaly?

jawaban:

Sifat Kaku: FIFO hanya peduli pada siapa yang paling lama di RAM, bukan siapa yang sering dipakai.

Urutan yang Kacau: Saat jumlah frame ditambah, urutan "antrean" halaman berubah total. Data penting yang seharusnya masih ada di RAM malah bisa terhapus lebih cepat karena posisi antreannya bergeser.

Bukan Algoritma Stack: Karena FIFO tidak menjamin bahwa data di memori kecil pasti ada di memori yang lebih besar, performanya bisa jadi tidak konsisten saat RAM ditambah.

3. Mengapa LRU umumnya menghasilkan performa lebih baik dibanding FIFO?

jawaban:

Berdasarkan Pemakaian: LRU mempertahankan data yang sering diakses dan hanya membuang data yang sudah lama "nganggur".

Prediksi Akurat: Menggunakan logika bahwa data yang baru dipakai kemungkinan besar akan dipakai lagi dalam waktu dekat.

Lebih Stabil: Tidak mengalami Belady’s Anomaly; jadi kalau RAM ditambah, performa LRU pasti makin bagus atau stabil.


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
