
# Laporan Praktikum Minggu [5]
Topik: ["Penjadwalan CPU – FCFS dan SJF"]

---

## Identitas
- **Nama**  : [LUTHFI AULIA RAHMAN]  
- **NIM**   : [25202948]  
- **Kelas** : [1 IKRB]

---

## Tujuan
1. Menghitung waiting time dan turnaround time untuk algoritma FCFS dan SJF.
2. Menyajikan hasil perhitungan dalam tabel yang rapi dan mudah dibaca.
3. Membandingkan performa FCFS dan SJF berdasarkan hasil analisis.
4. Menjelaskan kelebihan dan kekurangan masing-masing algoritma.
5. Menyimpulkan kapan algoritma FCFS atau SJF lebih sesuai digunakan.

---

## Dasar Teori
**1. FCFS (First come first surved)**
- konsep dasar: proses yang datang lebih dulu akan di eksekusi lebih dulu, seperti antrian di loket- prinsipnya first in, first out(FIFO)
- sederhana & mudah diimplenasikan, karena proses dijadwalakan berdasarkan urutan waktu kedatangan (arrival time)
- tidak adil untuk proses pendek, karena proses dengan burst time kecil bisa menunggu lama di belakang proses besar (conoy effect)
- tidak preemptive, artinya proses yang sedang berjalan tidak bisa di hentikan sampai selesai.
- kinerja baik untuk beban kerja seragam, tapi kurang efisien untuk campuran proses panjang dan pendek.

**2. SJF (shortest job first)**
- konsep dasar proses dengan waktu eksekusi (burst time) time paling pendek dieksekusi lebih dulu untuk meniminimalkan waktu tunggu rata-rata.
- tujuan utama: menghasilkan rata-rata waiting time dan turnaround time paling kecil di banding FCFS.
- dapat bersifat non-preemptive(sekali jalan sampai selesai) atau preemptive (dikenal sebagai shortest remaining time)


## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
. **Siapkan Data Proses**
   Gunakan tabel proses berikut sebagai contoh (boleh dimodifikasi dengan data baru):
   | Proses | Burst Time | Arrival Time |
   |:--:|:--:|:--:|
   | P1 | 6 | 0 |
   | P2 | 8 | 1 |
   | P3 | 7 | 2 |
   | P4 | 3 | 3 |

2. **Eksperimen 1 – FCFS (First Come First Served)**
   - Urutkan proses berdasarkan *Arrival Time*.  
   - Hitung nilai berikut untuk tiap proses:
     ```
     Waiting Time (WT) = waktu mulai eksekusi - Arrival Time
     Turnaround Time (TAT) = WT + Burst Time
     ```
   - Hitung rata-rata Waiting Time dan Turnaround Time.  

| Proses | Burst Time | WT | TAT |
| ------ | ---------- | -- | --- |
| P1     | 8          | 0  | 8   |
| P2     | 4          | 8  | 12  |
| P3     | 2          | 12 | 14  |
| P4     | 1          | 14 | 15  |

* **Rata-rata WT:**  = 8.5
* **Rata-rata TAT:** = 12.25


   - Buat Gantt Chart sederhana:  
     ```
     | P1 | P2 | P3 | P4 |
     0    6    14   21   24
     ```

3. **Eksperimen 2 – SJF (Shortest Job First)**
   - Urutkan proses berdasarkan *Burst Time* terpendek (dengan memperhatikan waktu kedatangan).  
   - Lakukan perhitungan WT dan TAT seperti langkah sebelumnya.  

   | Proses | Burst Time | WT | TAT |
| ------ | ---------- | -- | --- |
| P1     | 8          | 0  | 8   |
| P4     | 1          | 5  | 6   |
| P3     | 2          | 7  | 9   |
| P2     | 4          | 11 | 15  |

* **Rata-rata WT:**  = 5.75
* **Rata-rata TAT:**  = 9.5
   - Bandingkan hasil FCFS dan SJF pada tabel berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | FCFS | 8.5 | 12.25 | Sederhana dan mudah diterapkan | Tidak efisien untuk proses panjang |
     | SJF | 5.75 | 9.5 | Optimal untuk job pendek | Menyebabkan *starvation* pada job panjang |

4. **Eksperimen 3 – Visualisasi Spreadsheet (Opsional)**
   - Gunakan Excel/Google Sheets untuk membuat perhitungan otomatis:
     - Kolom: Arrival, Burst, Start, Waiting, Turnaround, Finish.
     - Gunakan formula dasar penjumlahan/subtraksi.
   - Screenshot hasil perhitungan dan simpan di:
     ```
     praktikum/week5-scheduling-fcfs-sjf/screenshots/
     ```

5. **Analisis**
   - Bandingkan hasil rata-rata WT dan TAT antara FCFS & SJF.  
   - Jelaskan kondisi kapan SJF lebih unggul dari FCFS dan sebaliknya.  
   - Tambahkan kesimpulan singkat di akhir laporan.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 5 - CPU Scheduling FCFS & SJF"
   git push origin main
   ```



---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Bandingkan hasil rata-rata WT dan TAT antara FCFS & SJF.
- Jelaskan kondisi kapan SJF lebih unggul dari FCFS dan sebaliknya.
- Tambahkan kesimpulan singkat di akhir laporan.


---

## 1. Perbandingan Rata-rata WT dan TAT

Misalkan kita punya contoh proses berikut:

| Proses | Arrival Time | Burst Time |
| ------ | ------------ | ---------- |
| P1     | 0            | 8          |
| P2     | 1            | 4          |
| P3     | 2            | 2          |
| P4     | 3            | 1          |

 **A. FCFS (First-Come, First-Served)**

**Langkah perhitungan:**

* WT = Waktu mulai eksekusi – Arrival Time
* TAT = WT + Burst Time

**Perhitungan:**

| Proses | Arrival | Burst | Start Time | Finish Time |  WT | TAT |
| :----: | :-----: | :---: | :--------: | :---------: | :-: | :-: |
|   P1   |    0    |   8   |      0     |      8      |  0  |  8  |
|   P2   |    1    |   4   |      8     |      12     |  7  |  11 |
|   P3   |    2    |   2   |     12     |      14     |  10 |  12 |
|   P4   |    3    |   1   |     14     |      15     |  11 |  12 |



* **Rata-rata WT:**  = 7
* **Rata-rata TAT:** = 10,75

---

 **B. SJF (Shortest Job First, non-preemptive)**

**Langkah:** Pilih proses dengan **burst time terkecil** yang sudah datang.

**Perhitungan:**

| Proses | Arrival Time | Burst Time | Start Time | Finish Time |  WT | TAT |
| :----: | :----------: | :--------: | :--------: | :---------: | :-: | :-: |
|   P1   |       0      |      8     |      0     |      8      |  0  | 8   |
|   P4   |       3      |      1     |      8     |      9      |  5  |   6 |
|   P3   |       2      |      2     |      9     |      11     |  7  |  9  |
|   P2   |       1      |      4     |     11     |      15     |  10 | 14  |

* **Rata-rata WT:**  = 5,5
* **Rata-rata TAT:**  = 9,25

---

 2. Analisis kondisi unggul masing-masing

| Algoritma | Kelebihan                                                                                                   | Kekurangan / Kondisi                                                                                                                           |
| --------- | ----------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **FCFS**  | - Sederhana, mudah diterapkan <br> - Tidak perlu prediksi burst time                                        | - Bisa menyebabkan **konvoi effect** (proses panjang menahan proses pendek) <br> - Tidak efisien jika burst time bervariasi besar              |
| **SJF**   | - Menghasilkan rata-rata WT dan TAT lebih rendah dibanding FCFS <br> - Lebih efisien untuk batch processing | - Sulit diterapkan jika burst time tidak diketahui <br> - Bisa menyebabkan **starvation** untuk proses panjang jika proses pendek terus datang |

**Kondisi unggul:**

* **SJF lebih unggul** jika burst time dapat diketahui dan proses memiliki variasi durasi eksekusi, karena rata-rata WT dan TAT lebih rendah.
* **FCFS lebih unggul** pada sistem **real-time atau interaktif** di mana urutan kedatangan harus diprioritaskan, atau ketika prediksi burst time sulit dilakukan.

---

 
---

## Kesimpulan

1. JF lebih unggul daripada FCFS ketika sistem dapat memperkirakan lama eksekusi proses, karena mampu menghasilkan waktu tunggu dan waktu penyelesaian rata-rata yang lebih rendah.
2. FCFS lebih unggul jika keadilan dan kesederhanaan lebih diutamakan, terutama saat lama eksekusi proses tidak dapat diprediksi
3. Pemilihan algoritma tergantung pada tujuan sistem: efisiensi waktu (pilih SJF) atau keadilan dan kemudahan implementasi (pilih FCFS).

---

## Quiz
1. Apa perbedaan utama antara FCFS dan SJF?
2. Mengapa SJF dapat menghasilkan rata-rata waktu tunggu minimum?
3. Apa kelemahan SJF jika diterapkan pada sistem interaktif?

**1**
| Aspek                   | **FCFS (First Come First Served)**                                                            | **SJF (Shortest Job First)**                                                   |
| ----------------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **Prinsip kerja**       | Proses dieksekusi berdasarkan urutan kedatangan.                                              | Proses dengan waktu eksekusi (burst time) paling pendek dijalankan lebih dulu. |
| **Sifat algoritma**     | Non-preemptive (umumnya).                                                                     | Bisa **non-preemptive** atau **preemptive (SRTF)**.                            |
| **Keadilan (fairness)** | Adil dalam urutan datang, tapi bisa menyebabkan *convoy effect* (proses cepat menunggu lama). | Tidak selalu adil; proses panjang bisa terus tertunda.                         |
| **Kinerja rata-rata**   | Waktu tunggu rata-rata relatif lebih besar.                                                   | Waktu tunggu rata-rata paling kecil secara teori.                              |

**2.** Karena SJF selalu mengeksekusi proses dengan waktu terpendek terlebih dahulu, maka:

- Proses cepat segera selesai tanpa harus menunggu proses panjang.
- Proses-proses berikutnya menunggu lebih sedikit waktu total.
- Secara matematis, SJF meminimalkan average waiting time (WT) dan turnaround time (TAT) untuk kumpulan proses yang sama.

**3.** Kelemahan SJF pada sistem interaktif

- Tidak tahu burst time secara pasti. Sistem interaktif sulit memprediksi berapa lama proses akan berjalan.
- Tidak adil bagi proses panjang. Proses dengan waktu eksekusi besar bisa tertunda terus (starvation).
- Kurang responsif. Untuk sistem interaktif (misalnya OS dengan banyak input pengguna), keadilan dan respon cepat lebih penting daripada efisiensi waktu tunggu total.

## Tugas
1. Hitung waiting time dan turnaround time dari minimal 2 skenario FCFS dan SJF.
2. Sajikan hasil perhitungan dalam tabel perbandingan (FCFS vs SJF).
3. Analisis kelebihan dan kelemahan tiap algoritma.

---


 **Skenario 1**

### Data Proses

| Proses | Arrival Time | Burst Time |
| :----: | :----------: | :--------: |
|   P1   |       0      |      5     |
|   P2   |       1      |      3     |
|   P3   |       2      |      8     |

---

### 🔹 **FCFS (First Come First Served)**

Urutan berdasarkan *arrival time*: **P1 → P2 → P3**

| Proses | Arrival | Burst | Start | Finish | Waiting Time (WT) | Turnaround Time (TAT) |
| :----- | :-----: | :---: | :---: | :----: | :---------------: | :-------------------: |
| P1     |    0    |   5   |   0   |    5   |         0         |           5           |
| P2     |    1    |   3   |   5   |    8   |   5 − 1 = **4**   |     8 − 1 = **7**     |
| P3     |    2    |   8   |   8   |   16   |   8 − 2 = **6**   |    16 − 2 = **14**    |

 **Rata-rata:**

* WT rata-rata = (0 + 4 + 6) / 3 = **3.33**
* TAT rata-rata = (5 + 7 + 14) / 3 = **8.67**

---

### 🔹 **SJF (Shortest Job First, non-preemptive)**

Urutan berdasarkan *burst time* (setelah proses datang):

* P1 mulai dulu (datang pertama).
* Setelah P1 selesai (t=5), proses yang tersedia adalah P2 (3) dan P3 (8) → pilih **P2** karena burst terkecil.

Urutan: **P1 → P2 → P3**

| Proses | Arrival | Burst | Start | Finish |       WT      |       TAT       |
| :----- | :-----: | :---: | :---: | :----: | :-----------: | :-------------: |
| P1     |    0    |   5   |   0   |    5   |       0       |        5        |
| P2     |    1    |   3   |   5   |    8   | 5 − 1 = **4** |  8 − 1 = **7**  |
| P3     |    2    |   8   |   8   |   16   | 8 − 2 = **6** | 16 − 2 = **14** |

 **Hasil sama dengan FCFS** karena urutannya kebetulan sama.

---

 **Skenario 2**

### Data Proses

| Proses | Arrival | Burst |
| :----: | :-----: | :---: |
|   P1   |    0    |   6   |
|   P2   |    2    |   4   |
|   P3   |    3    |   2   |

---

### 🔹 **FCFS**

Urutan berdasarkan *arrival time*: **P1 → P2 → P3**

| Proses | Arrival | Burst | Start | Finish |       WT       |       TAT      |
| :----- | :-----: | :---: | :---: | :----: | :------------: | :------------: |
| P1     |    0    |   6   |   0   |    6   |        0       |        6       |
| P2     |    2    |   4   |   6   |   10   |  6 − 2 = **4** | 10 − 2 = **8** |
| P3     |    3    |   2   |   10  |   12   | 10 − 3 = **7** | 12 − 3 = **9** |

**Rata-rata:**

* WT = (0 + 4 + 7) / 3 = **3.67**
* TAT = (6 + 8 + 9) / 3 = **7.67**

---

### 🔹 **SJF (Non-preemptive)**

Langkah-langkah:

* t=0: hanya **P1** → jalankan P1 (0–6)
* t=6: **P2 (4)** dan **P3 (2)** sudah datang → pilih **P3** (burst terkecil)
* urutan: **P1 → P3 → P2**

| Proses | Arrival | Burst | Start | Finish |       WT      |       TAT       |
| :----- | :-----: | :---: | :---: | :----: | :-----------: | :-------------: |
| P1     |    0    |   6   |   0   |    6   |       0       |        6        |
| P3     |    3    |   2   |   6   |    8   | 6 − 3 = **3** |  8 − 3 = **5**  |
| P2     |    2    |   4   |   8   |   12   | 8 − 2 = **6** | 12 − 2 = **10** |

**Rata-rata:**

* WT = (0 + 3 + 6) / 3 = **3.0**
* TAT = (6 + 5 + 10) / 3 = **7.0**

---

**Perbandingan Hasil**

| Algoritma         | Rata-rata Waiting Time | Rata-rata Turnaround Time |
| :---------------- | :--------------------: | :-----------------------: |
| FCFS (Skenario 1) |          3.33          |            8.67           |
| SJF (Skenario 1)  |          3.33          |            8.67           |
| FCFS (Skenario 2) |          3.67          |            7.67           |
| SJF (Skenario 2)  |        **3.00**        |          **7.00**         |


---
**2.**
 **Skenario 1**

| Proses | Arrival Time | Burst Time |
| :----: | :----------: | :--------: |
|   P1   |       0      |      5     |
|   P2   |       1      |      3     |
|   P3   |       2      |      8     |

#### 🔹 FCFS

Urutan eksekusi: P1 → P2 → P3

| Proses | Arrival | Burst | Start | Waiting Time (WT) | Turnaround Time (TAT) |
| :----: | :-----: | :---: | :---: | :---------------: | :-------------------: |
|   P1   |    0    |   5   |   0   |         0         |           5           |
|   P2   |    1    |   3   |   5   |     5 - 1 = 4     |       4 + 3 = 7       |
|   P3   |    2    |   8   |   8   |     8 - 2 = 6     |       6 + 8 = 14      |

**Rata-rata WT = (0 + 4 + 6)/3 = 3.33**
**Rata-rata TAT = (5 + 7 + 14)/3 = 8.67**

#### 🔹 SJF (Non-preemptive)

Urutan eksekusi: P1 → P2 → P3 (karena P2 paling pendek setelah P1 selesai)

| Proses | Arrival | Burst | Start | Waiting Time (WT) | Turnaround Time (TAT) |
| :----: | :-----: | :---: | :---: | :---------------: | :-------------------: |
|   P1   |    0    |   5   |   0   |         0         |           5           |
|   P2   |    1    |   3   |   5   |     5 - 1 = 4     |       4 + 3 = 7       |
|   P3   |    2    |   8   |   8   |     8 - 2 = 6     |       6 + 8 = 14      |

*(hasil sama seperti FCFS karena urutan burst juga sama)*
**Rata-rata WT = 3.33**, **Rata-rata TAT = 8.67**

---

 **Skenario 2**

| Proses | Arrival Time | Burst Time |
| :----: | :----------: | :--------: |
|   P1   |       0      |      7     |
|   P2   |       2      |      4     |
|   P3   |       4      |      1     |

#### 🔹 FCFS

Urutan eksekusi: P1 → P2 → P3

| Proses | Arrival | Burst | Start |     WT     |    TAT    |
| :----: | :-----: | :---: | :---: | :--------: | :-------: |
|   P1   |    0    |   7   |   0   |      0     |     7     |
|   P2   |    2    |   4   |   7   |  7 - 2 = 5 | 5 + 4 = 9 |
|   P3   |    4    |   1   |   11  | 11 - 4 = 7 | 7 + 1 = 8 |

**Rata-rata WT = (0 + 5 + 7)/3 = 4.00**
**Rata-rata TAT = (7 + 9 + 8)/3 = 8.00**

#### 🔹 SJF

Urutan eksekusi: P1 (0–7) → P3 (7–8) → P2 (8–12)

| Proses | Arrival | Burst | Start |     WT    |     TAT    |
| :----: | :-----: | :---: | :---: | :-------: | :--------: |
|   P1   |    0    |   7   |   0   |     0     |      7     |
|   P3   |    4    |   1   |   7   | 7 - 4 = 3 |  3 + 1 = 4 |
|   P2   |    2    |   4   |   8   | 8 - 2 = 6 | 6 + 4 = 10 |

**Rata-rata WT = (0 + 3 + 6)/3 = 3.00**
**Rata-rata TAT = (7 + 4 + 10)/3 = 7.00**

---

**Tabel Perbandingan FCFS vs SJF**

|     Algoritma     | Rata-rata Waiting Time | Rata-rata Turnaround Time | Keterangan                                               |
| :---------------: | :--------------------: | :-----------------------: | :------------------------------------------------------- |
| FCFS (Skenario 1) |          3.33          |            8.67           | Sama dengan SJF karena urutan sama                       |
|  SJF (Skenario 1) |          3.33          |            8.67           | Tidak ada perbedaan urutan                               |
| FCFS (Skenario 2) |          4.00          |            8.00           | Lebih lambat karena tidak efisien terhadap proses pendek |
|  SJF (Skenario 2) |          3.00          |            7.00           | Lebih efisien, waktu tunggu rata-rata lebih kecil        |

**3.**

**1. FCFS (First Come First Serve)**

Prinsip:
Proses yang datang lebih dulu akan dieksekusi lebih dulu, seperti antrian di kasir.

 Kelebihan:

Sederhana dan mudah diimplementasikan — urutan eksekusi hanya berdasarkan waktu kedatangan (arrival time).

Adil dalam konteks waktu kedatangan — tidak ada proses yang dilewati; siapa datang duluan, dilayani duluan.

Tidak memerlukan prediksi waktu proses — sistem tidak perlu tahu berapa lama proses akan berjalan.

 Kelemahan:

Masalah “Convoy Effect” — jie

Rata-rata waktu tunggu tinggi — terutama jika variasi burst time antar proses besar.

Kurang efisien untuk sistem interaktif — karena respon terhadap proses pendek menjadi lambat.

**2. SJF (Shortest Job First)**

Prinsip:
Proses dengan waktu eksekusi (burst time) paling pendek akan dijalankan terlebih dahulu.

 Kelebihan:

Rata-rata waktu tunggu minimum secara teoritis — karena proses pendek selesai lebih cepat, mengurangi antrian.

Meningkatkan throughput — lebih banyak proses dapat diselesaikan dalam waktu tertentu.

Efisien untuk sistem batch — cocok jika semua burst time sudah diketahui sebelumnya.

 Kelemahan:

Sulit menentukan burst time — sistem jarang tahu berapa lama proses akan berjalan.

Dapat menyebabkan starvation — proses dengan burst time panjang bisa terus tertunda.

Tidak cocok untuk sistem interaktif — karena membutuhkan prediksi waktu proses dan dapat mengabaikan prioritas pengguna.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  belum memahami tentang FCFS dan SJF
- Bagaimana cara Anda mengatasinya?  dengan mencari referensi di web site atau Ai

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
