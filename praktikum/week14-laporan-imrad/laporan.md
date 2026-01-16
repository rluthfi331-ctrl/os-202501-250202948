
# Laporan Praktikum Minggu 14

Topik: Penyusunan Laporan Praktikum Format IMRAD
---


## Identitas
- **Nama**  : LUTHFI AULIA RAHMAN
- **NIM**   : 250202948
- **Kelas** : 1 IKRB

Judul Laporan: Analisis Kinerja Algoritma Penjadwalan CPU FCFS dan SJF
---
**I. Pendahuluan (Introduction)**
---
**A. Latar Belakang**

Penjadwalan CPU adalah basis dari sistem operasi multiprogramming. Dengan berpindah antar proses, CPU meningkatkan produktivitas sistem. Masalah utama dalam penjadwalan adalah menentukan urutan eksekusi proses dalam antrean ready agar penggunaan CPU optimal. Algoritma First-Come, First-Served (FCFS) adalah metode paling sederhana, namun sering kali menyebabkan Convoy Effect. Sebagai alternatif, Shortest Job First (SJF) mengusulkan penjadwalan berdasarkan durasi burst terkecil untuk meminimalkan waktu tunggu.

**B. Rumusan Masalah**

Bagaimana perbandingan rata-rata waktu tunggu (Average Waiting Time) antara algoritma FCFS dan SJF (Non-Preemptive) pada sekumpulan proses dengan waktu kedatangan yang sama?

**C. Tujuan Praktikum**

1. Mensimulasikan mekanisme kerja algoritma FCFS dan SJF.

2. Mengukur dan membandingkan Waiting Time (WT) dan Turnaround Time (TAT) dari kedua algoritma.

3. Menganalisis keefektifan SJF dalam mengurangi rata-rata waktu tunggu dibandingkan FCFS.
---
**II. Metode (Methods)**
---
**A. Lingkungan Uji**

Simulasi dilakukan menggunakan bahasa pemrograman Python 3.10 pada lingkungan sistem operasi Windows 11. Alat bantu yang digunakan adalah pustaka matplotlib untuk visualisasi Gantt Chart.

**B. Prosedur Eksperimen**

1. Menentukan kumpulan proses (P1, P2, P3, P4, P5) dengan Burst Time yang bervariasi.

2. Mengasumsikan semua proses tiba pada waktu yang sama ($AT = 0$).

3. Mengimplementasikan logika FCFS (berdasarkan urutan input).

4. Mengimplementasikan logika SJF Non-Preemptive (mengurutkan proses berdasarkan Burst Time terpendek).

5. Menghitung WT dan TAT untuk setiap proses pada kedua skenario.

**C. Parameter Uji**

 Dataset Proses:

- P1 (Burst: 10ms)

- P2 (Burst: 1ms)

- P3 (Burst: 2ms)

- P4 (Burst: 7ms)

- P5 (Burst: 5ms)

Metrik Pengukuran:

- Waiting Time (WT): Waktu yang dihabiskan proses di antrean ready.

- Turnaround Time (TAT): Total waktu dari kedatangan hingga selesai ($TAT = WT + Burst$).

**III. Hasil (Results)**
---
Hasil penghitungan rata-rata waktu tunggu dan total durasi eksekusi disajikan pada tabel di bawah ini:

**Tabel 1: Perbandingan Metrik FCFS vs SJF**

| Algoritma | Total Burst Time | Avg. Waiting Time (AWT) | Avg. Turnaround Time (ATAT) |
| :--- | :---: | :---: | :---: |
| **FCFS** | 25 ms | 11.2 ms | 16.2 ms |
| **SJF** | 25 ms | 5.2 ms | 10.2 ms |


### Bukti Eksekusi Program

![alt text](<Screenshot 2026-01-15 203222.png>)


**IV. Pembahasan (Discussion)**
---

**A. Interpretasi Hasil**

Data pada Tabel 1 menunjukkan penurunan drastis pada Average Waiting Time ketika berpindah dari FCFS ke SJF. Pada FCFS, proses P1 yang memiliki burst time terbesar (10ms) dijalankan pertama kali, memaksa proses-proses kecil (P2, P3) menunggu lama. Sebaliknya, SJF mendahulukan P2 dan P3, sehingga akumulasi waktu tunggu secara keseluruhan berkurang lebih dari 50% (dari 11.2ms menjadi 5.2ms).

**B. Analisis Kinerja (Convoy Effect vs Optimization)**

FCFS mengalami apa yang disebut sebagai Convoy Effect, di mana proses pendek terjebak di belakang proses panjang. SJF secara matematis terbukti optimal dalam memberikan rata-rata waktu tunggu minimum. Namun, pembatasan SJF pada sistem nyata adalah durasi burst CPU di masa depan sulit diprediksi secara akurat.

**C. Keterbatasan**

Praktikum ini menggunakan skenario waktu kedatangan nol ($AT = 0$). Dalam kondisi nyata di mana proses datang pada waktu yang berbeda, kinerja SJF Non-Preemptive mungkin berbeda karena proses panjang yang sudah berjalan tidak bisa diinterupsi.

**V. Kesimpulan (Conclusion)**
---
1. Algoritma SJF jauh lebih efisien dibandingkan FCFS dalam meminimalkan rata-rata waktu tunggu.

2. Penjadwalan FCFS sangat bergantung pada urutan kedatangan, sementara SJF bergantung pada karakteristik beban kerja.

3. Penggunaan SJF disarankan untuk sistem yang memprioritaskan responsivitas pada tugas-tugas kecil.

**VI. Daftar Pustaka**
---
 Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). Operating System Concepts (10th ed.). Wiley.

 Stallings, W. (2017). Operating Systems: Internals and Design Principles (9th ed.). Pearson.

Tanenbaum, A. S., & Bos, H. (2015). Modern Operating Systems (4th ed.). Pearson Education.

 Arpaci-Dusseau, R. H., & Arpaci-Dusseau, A. C. (2018). Operating Systems: Three Easy Pieces. Arpaci-Dusseau Books.

**VII. Quiz**
---
1. Mengapa format IMRAD membantu membuat laporan praktikum lebih ilmiah? Format IMRAD memisahkan antara data objektif (Hasil) dan opini peneliti (Pembahasan). Struktur ini memastikan eksperimen dapat direplikasi oleh orang lain karena metodologi dijelaskan secara rinci.

2. Apa perbedaan antara bagian Hasil dan Pembahasan? Hasil menyajikan data mentah (angka, tabel, grafik) secara objektif. Pembahasan memberikan interpretasi terhadap data tersebut, menjelaskan "mengapa" hasil itu terjadi, dan menghubungkannya dengan teori.

3. Mengapa sitasi dan daftar pustaka penting? Sitasi memberikan kredit kepada penulis asli, menghindari plagiarisme, dan memberikan landasan teori yang kuat bagi laporan praktikum tersebut.

##

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
