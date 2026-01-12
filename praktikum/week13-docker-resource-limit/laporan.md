
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
1.

---

## Kode / Perintah


---

## Hasil Eksekusi

---

## Analisis
1. Memori: Stabilitas vs. Ketersediaan
- Mekanisme: RAM bersifat finite (terbatas). Jika container melebihi Hard Limit, kernel akan melakukan termination (OOM Kill).

- Analisis: Limitasi memori wajib ada untuk mencegah memory leak dari satu container yang bisa mengakibatkan seluruh sistem (Host) freeze atau mati total.

2. CPU: Keadilan vs. Performa
- Mekanisme: Berbeda dengan RAM, CPU menggunakan sistem time-slicing. Jika jatah CPU habis, container tidak mati, tapi hanya mengalami throttling (pelambatan proses).

- Analisis: Pengaturan --cpus memberikan kepastian performa (predictable performance), sedangkan --cpu-shares memastikan distribusi beban yang adil saat server sedang sibuk (load tinggi).

---

## Kesimpulan
1. Isolasi adalah Proteksi: Fitur ini mencegah efek noisy neighbor, di mana satu container yang bermasalah (misal: memory leak) nggak bakal narik seluruh sistem host buat ikut crash.

2. Prediktabilitas Layanan: Dengan limitasi yang jelas (--memory dan --cpus), kita bisa ngejamin performa aplikasi jadi lebih stabil dan gampang diprediksi, karena jatah resource-nya udah dikunci dari awal.

3. Efisiensi Infrastruktur: Kita jadi lebih pinter dalam capacity planning. Kita bisa maksimalin jumlah container dalam satu server tanpa takut overload, karena setiap container udah punya "pagar" masing-masing lewat mekanisme cgroups.

Intinya: Lebih baik satu container yang lambat atau restart sendiri karena kena limit, daripada satu server yang freeze total dan bikin semua layanan tewas barengan.

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
