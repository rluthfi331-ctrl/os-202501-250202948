
# Laporan Praktikum Minggu 11
Topik: Simulasi dan Deteksi Deadlock


---

## Identitas
- **Nama**  : LUTHFI AULIA RAHMAN
- **NIM**   : 250202948  
- **Kelas** : 1 IKRB

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:

1. Membuat program sederhana untuk mendeteksi deadlock.
2. Menjalankan simulasi deteksi deadlock dengan dataset uji.
3. Menyajikan hasil analisis deadlock dalam bentuk tabel.
4. Memberikan interpretasi hasil uji secara logis dan sistematis.
5. Menyusun laporan praktikum sesuai format yang ditentukan.

---

## Dasar Teori
1. Konsep Deadlock: Sebuah situasi dalam sistem operasi di mana beberapa proses terhenti secara permanen karena saling menunggu sumber daya yang sedang digunakan satu sama lain.

2. Kondisi Circular Wait: Salah satu penyebab utama deadlock di mana terjadi rantai melingkar antar proses. Mobil A membutuhkan jalur yang ditahan Mobil B, dan seterusnya hingga membentuk lingkaran yang tidak terputus.

3. Graf Alokasi Sumber Daya: Representasi visual yang menunjukkan hubungan ketergantungan antara kendaraan (proses) dan jalur (sumber daya). Adanya siklus pada graf ini menjadi indikator mutlak terjadinya deadlock.

4. Metode Pemulihan: Strategi untuk mengembalikan fungsi sistem dengan cara menghentikan salah satu proses (terminasi) guna membebaskan sumber daya yang tertahan.
---

## Langkah Praktikum
1. Menyiapkan Dataset

Membuat dataset sederhana yang berisi:

- Daftar proses
- Resource Allocation
- Resource Request / Need

Data tabel:

| Proses | Allocation | Request |
| :--- | :--- | :--- |
| Mobil_A | Jalur_Utara | Jalur_Timur |
| Mobil_B | Jalur_Timur | Jalur_Selatan |
| Mobil_C | Jalur_Selatan | Jalur_Utara |


Program:

- Membaca data proses dan resource.
- Menentukan apakah sistem berada dalam kondisi deadlock.
- Menampilkan proses mana saja yang terlibat deadlock.
3. Eksekusi & Validasi

- Menjalankan program dengan dataset uji.
- Memvalidasi hasil deteksi dengan analisis manual/logis.
- Menyimpan hasil eksekusi dalam bentuk screenshot.

4. Analisis Hasil

- Menyajikan hasil deteksi dalam tabel (proses deadlock / tidak).
- Menjelaskan mengapa deadlock terjadi atau tidak terjadi.
- Mengaitkan hasil dengan teori deadlock (empat kondisi).


---

## Kode / Perintah
1. Potongan Code deadlock_detection.py

```python

import csv
import time
from colorama import Fore, Style, init


init(autoreset=True)

def deteksi_deadlock():
    catatan = []
    try:
        with open('data_macet.csv', mode='r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                catatan.append(row)
    except FileNotFoundError:
        print(f"{Fore.RED}Error: File 'data_macet.csv' tidak ditemukan!")
        return

    posisi_jalur = {b['Allocation']: b['Proses'] for b in catatan}
    peta_tunggu = {}

    print(f"{Fore.YELLOW}\n=== MONITORING PERSIMPANGAN ===")
    for b in catatan:
        mobil = b['Proses']
        tujuan = b['Request']
        print(f"• {Fore.CYAN}{mobil}{Fore.WHITE} di {b['Allocation']} -> Ke {tujuan}")
        
        if tujuan in posisi_jalur:
            peta_tunggu[mobil] = posisi_jalur[tujuan]
            print(f"  {Fore.RED}[!] TERTAHAN oleh {posisi_jalur[tujuan]}")
        else:
            print(f"  {Fore.GREEN}[✓] JALUR KOSONG")
        time.sleep(0.3)

    # Deteksi Deadlock
    terjebak = []
    for m in [b['Proses'] for b in catatan]:
        jalur = []
        curr = m
        while curr in peta_tunggu and curr not in jalur:
            jalur.append(curr)
            curr = peta_tunggu[curr]
            if curr == m:
                terjebak = jalur
                break
        if terjebak: break

    print("-" * 30)
    if terjebak:
        print(f"{Fore.RED}{Style.BRIGHT}HASIL: TERDETEKSI DEADLOCK!")
        print(f"{Fore.RED}Mobil terlibat: {' -> '.join(terjebak)} -> {terjebak[0]}")
    else:
        print(f"{Fore.GREEN}HASIL: TIDAK ADA DEADLOCK")

if __name__ == "__main__":
    deteksi_deadlock()
   ```
   2. Potongan Code deadlock_solution.py
```python
   import csv
import time
from colorama import Fore, Back, Style, init


init(autoreset=True)

def baca_data():
    catatan = []
    try:
        with open('data_macet.csv', mode='r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                catatan.append(row)
        return catatan
    except FileNotFoundError:
        print("File data_macet.csv tidak ditemukan!")
        return []

def cari_siklus(peta_tunggu, mobil_sekarang, sudah_dicek, antrean_pantau):
    if mobil_sekarang in antrean_pantau:
        return True
    if mobil_sekarang in sudah_dicek:
        return False
    
    sudah_dicek.add(mobil_sekarang)
    antrean_pantau.add(mobil_sekarang)
    
    for tetangga in peta_tunggu.get(mobil_sekarang, []):
        if cari_siklus(peta_tunggu, tetangga, sudah_dicek, antrean_pantau):
            return True
            
    antrean_pantau.remove(mobil_sekarang)
    return False

def solusi_kemacetan():
    catatan = baca_data()
    if not catatan: return

    # 1. Deteksi Awal
    posisi_jalan = {baris['Allocation']: baris['Proses'] for baris in catatan}
    siapa_menunggu_siapa = {}
    for baris in catatan:
        mobil = baris['Proses']
        tujuan = baris['Request']
        if tujuan in posisi_jalan:
            siapa_menunggu_siapa[mobil] = [posisi_jalan[tujuan]]

    # Mencari mobil yang terjebak
    terjebak = []
    for mobil in [b['Proses'] for b in catatan]:
        if cari_siklus(siapa_menunggu_siapa, mobil, set(), set()):
            terjebak.append(mobil)

    if not terjebak:
        print(Fore.GREEN + "\n[!] Tidak ada kemacetan yang perlu diatasi.")
        return

    print(Fore.RED + f"\n[!] Terdeteksi kemacetan melingkar pada: {', '.join(terjebak)}")
    time.sleep(1)

    # 2. EKSEKUSI SOLUSI: Memilih Korban (Victim Selection)
    korban = terjebak[0]
    print(Fore.YELLOW + f"\n[PROSES PEMULIHAN] Memilih {korban} untuk diderek keluar...")
    time.sleep(1.5)
    
    print(Back.WHITE + Fore.BLACK + f" INFO: {korban} telah diderek keluar. Jalur sekarang terbuka! ")
    time.sleep(1)

    # 3. SIMULASI PERGERAKAN SETELAH SOLUSI
    print(Fore.GREEN + "\n[!] Mencoba menjalankan kembali kendaraan yang tersisa:")
    
    sisa_mobil = [b for b in catatan if b['Proses'] != korban]
    
    for baris in sisa_mobil:
        mobil = baris['Proses']
        asal = baris['Allocation']
        tujuan = baris['Request']
        
        # Jalur dianggap kosong jika tidak ada di Allocation mobil yang tersisa
        if tujuan not in [b['Allocation'] for b in sisa_mobil]:
            print(f"   {Fore.WHITE}{mobil} (di {asal}) -> {Fore.GREEN}BERHASIL MAJU {Fore.WHITE}ke {tujuan}")
        else:
            print(f"   {Fore.WHITE}{mobil} (di {asal}) -> {Fore.YELLOW}Menunggu giliran...")
        time.sleep(0.5)

if __name__ == "__main__":
    solusi_kemacetan()
```
    
    


## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:

- Hasil Mendeteksi Deadlock
![alt text](<Screenshot 2025-12-30 201851.png>)

- Hasil Solusi Dedlock
![alt text](<Screenshot 2025-12-30 202506.png>)


## Analisis
- Temuan Utama: Sistem terdeteksi mengalami Deadlock (kemacetan total) karena adanya siklus saling menunggu antara Mobil A, B, dan C.

- Penyebab (Circular Wait):

- Mobil A menahan Jalur Utara dan meminta Jalur Timur.

- Mobil B menahan Jalur Timur dan meminta Jalur Selatan.

- Mobil C menahan Jalur Selatan dan meminta Jalur Utara.

- Efek Simulasi: Tanpa intervensi, tidak ada kendaraan yang dapat bergerak maju karena sumber daya (jalur) yang dibutuhkan sedang dikuasai oleh kendaraan lain.

- Solusi Pemulihan: Dilakukan metode Victim Selection dengan menderek keluar satu kendaraan (Mobil A). Hal ini memutus rantai lingkaran sehingga kendaraan lainnya dapat melanjutkan pergerakan secara bergantian.
---

## Kesimpulan
1. Program simulasi ini berhasil mengimplementasikan algoritma deteksi deadlock secara akurat menggunakan dataset persimpangan jalan.

2. Munculnya kondisi Circular Wait pada skenario ini membuktikan bahwa pembagian sumber daya tanpa aturan prioritas dapat menyebabkan sistem lumpuh total.

3. Tindakan pemulihan melalui metode eliminasi satu proses terbukti efektif dalam mengatasi kemacetan melingkar dan mengembalikan stabilitas sistem.
---

## Quiz
1. Apa perbedaan antara deadlock prevention, avoidance, dan detection?

   Jawaban:
1. Deadlock Prevention (Pencegahan)

- Cara Kerja: Memastikan deadlock tidak mungkin terjadi dengan mematahkan salah satu dari 4 syarat utama (seperti Circular Wait atau Hold and Wait).

- Sifat: Sangat kaku dan preventif.

2. Deadlock Avoidance (Penghindaran)

- Cara Kerja: Sistem memeriksa setiap permintaan sumber daya secara dinamis. Permintaan hanya dikabulkan jika sistem tetap dalam kondisi aman (Safe State).

- Sifat: Selektif (menggunakan Algoritma Banker).

3. Deadlock Detection (Deteksi)

- Cara Kerja: Membiarkan deadlock terjadi, lalu menjalankan algoritma untuk menemukan siklus kemacetan.

- Sifat: Reaktif (butuh pemulihan/derek setelah terdeteksi).


2. Mengapa deteksi deadlock tetap diperlukan dalam sistem operasi?

   Jawaban:
- Efisiensi Tinggi: Tidak membatasi akses sumber daya secara ketat di awal, sehingga sistem bekerja lebih cepat dan maksimal.

- Realistis: Tidak membutuhkan informasi masa depan (seperti berapa maksimal jalur yang akan diminta) yang seringkali sulit diketahui oleh sistem.

- Penanganan Masalah Langka: Deadlock tidak selalu terjadi; lebih hemat sumber daya untuk mendeteksi dan memperbaikinya saat terjadi daripada mencegahnya setiap detik.

- Jaring Pengaman: Menjadi pertahanan terakhir jika protokol pencegahan lainnya gagal agar sistem tidak macet (stuck) selamanya.

3. Apa kelebihan dan kekurangan pendekatan deteksi deadlock?

    jawaban:

   Kelebihan:

- Efisien: Tidak membatasi proses, sehingga penggunaan sumber daya maksimal.

- Praktis: Tidak butuh informasi masa depan atau prediksi kebutuhan data.

- Hemat: Cocok untuk sistem yang jarang mengalami deadlock.

  Kekurangan:

- Risiko: Pemulihan bisa menyebabkan data hilang karena proses harus dihentikan paksa.

- Beban: Algoritma pemindaian siklus memakan daya CPU.

- Starvation: Risiko satu proses yang sama terus-menerus menjadi "korban" penghentian.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
