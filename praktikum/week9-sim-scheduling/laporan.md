
# Laporan Praktikum Minggu 9
Simulasi Algoritma Penjadwalan CPU (FCFS)

---

## Identitas
- **Nama**  : LUTHFI AULIA RAHMAN  
- **NIM**   : 250202948 
- **Kelas** : 1 IKRB

---

## Tujuan
1. Membuat program simulasi algoritma penjadwalan FCFS dan/atau SJF.
2. Menjalankan program dengan dataset uji yang diberikan atau dibuat sendiri.
3. Menyajikan output simulasi dalam bentuk tabel atau grafik.
4. Menjelaskan hasil simulasi secara tertulis.
5. Mengunggah kode dan laporan ke Git repository dengan rapi dan tepat waktu.

---

## Dasar Teori
1. Penjadwalan CPU Mekanisme sistem operasi untuk mengatur antrean proses agar penggunaan CPU lebih efisien dan tidak ada waktu yang terbuang sia-sia.

2. Algoritma FCFS First-Come, First-ServedAlgoritma paling dasar dengan prinsip siapa cepat, dia dapat. Proses yang punya Arrival Time waktu tiba paling awal akan dieksekusi lebih dulu sampai selesai Non-Preemptive.

3. Rumus UtamaUntuk menghitung performa algoritma, digunakan dua rumus wajib:

- Turnaround Time TAT: Finish Time - Arrival Time. Ini total waktu proses berada di sistem.

- Waiting Time WT: Turnaround Time - Burst Time. Ini murni waktu proses nganggur di antrean.

4. Convoy EffectKelemahan utama FCFS di mana proses pendek terhambat oleh proses panjang yang datang lebih dulu, sehingga rata-rata waktu tunggu menjadi tidak efisien.


## Langkah Praktikum
1. Menyiapkan folder kerja praktikum/week9-sim-scheduling/.

2. Membuat file dataset.csv yang berisi daftar proses (P1, P2, P3, P4) lengkap dengan Arrival Time dan Burst Time.

3. Membuat program Python sederhana yang membaca file CSV, mengurutkan data berdasarkan waktu kedatangan, dan menghitung waktu tunggu secara berurutan.

4. Menjalankan program di terminal dan membandingkan hasilnya dengan hitungan manual.

5. Mendokumentasikan seluruh hasil simulasi, perhitungan, dan analisis dalam file laporan.md.

6. Melakukan commit dan push hasil praktikum ke repositori GitHub.

`
git add .
git commit -m "Minggu 9 - Simulasi Scheduling CPU"
git push origin main
`


## Kode / Perintah
hasil logika utama algoritma FCFS yang di buat:

```python
def main_fcfs():
    
    data = [
        {"id": "P1", "at": 0, "bt": 6},
        {"id": "P2", "at": 1, "bt": 8},
        {"id": "P3", "at": 2, "bt": 7},
        {"id": "P4", "at": 3, "bt": 3}
    ]

    # FCFS: Pastikan urut berdasarkan Arrival Time
    data.sort(key=lambda x: x["at"])

    waktu_sekarang = 0
    total_wt = 0
    total_tat = 0

    print(f"\n{'ID':<5} | {'AT':<3} | {'BT':<3} | {'FT':<3} | {'TAT':<3} | {'WT':<3}")
    print("-" * 45)

    for p in data:
        # Jika CPU idle (menunggu proses datang)
        if waktu_sekarang < p["at"]:
            waktu_sekarang = p["at"]
        
        ft = waktu_sekarang + p["bt"]  # Finish Time
        tat = ft - p["at"]             # Turnaround Time
        wt = tat - p["bt"]             # Waiting Time
        
        print(f"{p['id']:<5} | {p['at']:<3} | {p['bt']:<3} | {ft:<3} | {tat:<3} | {wt:<3}")
        
        total_wt += wt
        total_tat += tat
        waktu_sekarang = ft

    # 2. Menghitung Rata-rata (Instruksi No. 3 & 4)
    avg_wt = total_wt / len(data)
    avg_tat = total_tat / len(data)

    print("-" * 45)
    print(f"Rata-rata Waiting Time    : {avg_wt:.2f}")
    print(f"Rata-rata Turnaround Time : {avg_tat:.2f}")

if __name__ == "__main__":
    main_fcfs()
  ```  

## Hasil Eksekusi
![alt text](<Screenshot 2025-12-25 222537.png>)

---

## Analisis
1. Jelaskan alur program.
2. Bandingkan hasil simulasi dengan perhitungan manual.
3. Jelaskan kelebihan dan keterbatasan simulasi


1 . Alur Program: 

- Pertama, program membaca input data yang terdiri dari Nama Proses, Waktu Kedatangan (Arrival Time), dan Durasi Eksekusi (Burst Time).

- Sistem akan mengurutkan proses berdasarkan siapa yang datang lebih dulu ke antrean (berdasarkan Arrival Time paling kecil).

- CPU mengeksekusi proses satu per satu secara berurutan; proses kedua tidak akan jalan sebelum proses pertama benar-benar selesai.

- Selama eksekusi berlangsung, program mencatat waktu selesai (Finish Time), lalu menghitung Turnaround Time (selisih waktu selesai dengan waktu datang) serta Waiting Time (selisih Turnaround Time dengan lama eksekusi).



2. Perbandingan Manual:

Parameter,Hitungan Manual,Hasil Program,Status
Rata-rata Waiting Time,8.75,8.75,Sesuai
Rata-rata Turnaround Time,14.75,14.75,Sesuai


3. Kelebihannya:

- Logikanya paling simpel dan gampang diterjemahin ke kodingan karena cuma ngikutin antrean biasa.

- Terasa adil secara urutan, karena nggak ada proses yang "nyalip" antrean proses lain yang sudah datang duluan.

Keterbatasannya:

- Ada masalah Convoy Effect. Jadi kalau ada satu proses yang durasinya lama banget (kayak P2 dengan BT=8) datang di awal, proses-proses kecil di belakangnya jadi keganggu dan nunggunya kelamaan.

- Kurang efisien kalau dibandingin sama algoritma lain (kayak SJF), karena rata-rata waktu tunggunya di FCFS ini cenderung lebih gede.


## Kesimpulan
Simulasi ini berhasil membuktikan akurasi algoritma FCFS. Program berjalan sesuai teori dan menghasilkan data yang valid dibanding hitungan manual. Tugas ini juga membantu saya memahami struktur folder proyek dan dokumentasi Markdown yang rapi.


---

## Quiz
1.  Mengapa simulasi diperlukan untuk menguji algoritma scheduling?
2. Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar?
3. Algoritma mana yang lebih mudah diimplementasikan? Jelaskan.

 1 . Bisa Lihat Hasil Langsung: Kita bisa simulasiin gimana CPU kerja tanpa harus nunggu sistem operasi aslinya jalan. Jadi lebih aman kalau ada bug atau logika yang salah.

Eksperimen Gampang: Kalau mau ganti-ganti data (misal prosesnya ditambah jadi 100), kita nggak perlu ngitung ulang pakai kertas. Tinggal ganti angkanya, klik run, langsung keluar hasilnya.

 2 . Manual = Risiko Salah: Manusia itu gampang capek dan nggak teliti kalau ngitung ribuan baris. Pasti ada aja yang kelewat.

Simulasi = Stabil: Komputer itu konsisten. Mau datanya 4 atau 40.000, akurasinya bakal tetap sama.

Waktu: Hitung manual ribuan data bisa seharian, simulasi cuma butuh waktu sekejap mata.

 3 . Karena logikanya "lurus" aja. Siapa yang datang duluan, dia yang dilayani. Kita nggak perlu bikin fungsi buat milih-milih mana yang paling pendek (SJF) atau bagi-bagi waktu (Round Robin). Ibarat antrean di kasir minimarket, yang datang pertama ya itu yang dibayar duluan. Nggak pakai mikir panjang!
    

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
