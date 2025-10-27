
# Laporan Praktikum Minggu [X]
Topik:  Arsitektur Sistem Operasi dan Kernel

---

## Identitas
- **Nama**  : [LUTHFI AULIA RAHMAN] 
- **NIM**   : [250202948]  
- **Kelas** : [1 IKRB]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  

> Sistem operasi (Operating System/OS) adalah perangkat lunak sistem yang mengelola hardware komputer dan menyediakan layanan bagi perangkat lunak aplikasi. Fungsi utamanya meliputi:

Manajemen Proses (Process Management)

Mengatur eksekusi proses (program yang sedang berjalan).

Menjadwalkan proses agar berjalan efisien.

Menyediakan mekanisme untuk sinkronisasi dan komunikasi antar-proses.

Manajemen Memori (Memory Management)

Mengatur alokasi dan dealokasi memori utama (RAM).

Menyediakan memori virtual agar program seolah-olah memiliki ruang memori besar.

Manajemen Perangkat (Device Management)

Mengelola input/output device seperti keyboard, mouse, printer, dsb.

Menggunakan driver untuk berkomunikasi dengan hardware.

Manajemen Sistem File (File System Management)

Mengatur penyimpanan dan pengaksesan data di media penyimpanan (HDD, SSD).

Menyediakan struktur folder dan pengamanan file.

Keamanan dan Proteksi (Security and Protection)

Melindungi data dan sumber daya dari akses tidak sah.

Menyediakan mekanisme otentikasi (login, permission).
 
 Peran Kernel

Kernel adalah inti dari sistem operasi. Ia berada paling dekat dengan perangkat keras dan memiliki kontrol penuh terhadap sistem. Perannya:

Menjalankan semua fungsi dasar OS seperti manajemen proses, memori, dan perangkat.

Menyediakan abstraksi perangkat keras agar aplikasi tidak perlu mengakses hardware secara langsung.

Bekerja dalam mode privileged (mode kernel), artinya punya akses penuh ke semua sumber daya sistem.

Peran System Call

System call adalah mekanisme yang digunakan program aplikasi untuk meminta layanan dari kernel.

Berfungsi sebagai jembatan antara program pengguna dan kernel.

Menyediakan antarmuka standar agar program bisa melakukan operasi tingkat rendah seperti membaca file, mengirim data, membuat proses.


---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.
Definisi:
System call adalah antarmuka (interface) antara program pengguna (user space) dan kernel (kernel space) yang memungkinkan aplikasi meminta layanan inti sistem operasi, seperti akses I/O, proses, dan memori.

Peralihan Mode (Mode Switching):
Ketika system call dipanggil, CPU berpindah dari user mode ke kernel mode melalui mekanisme software interrupt (trap). Setelah layanan kernel selesai, kontrol dikembalikan ke user mode.

Jenis-jenis System Call:
Umumnya dibagi menjadi lima kategori:
Manajemen proses (misal: fork(), exec(), wait())
Manajemen file (misal: open(), read(), write(), close())
Manajemen perangkat (misal: ioctl())
Manajemen informasi (misal: getpid(), alarm())
Komunikasi antar proses (IPC, misal: pipe(), socket())

Peran dalam Arsitektur OS:
System call berfungsi sebagai API level rendah yang menjembatani library C (misal libc) dengan layanan kernel. Library ini menyembunyikan detail teknis trap agar program bisa memanggil fungsi OS dengan cara yang sederhana.

Keamanan dan Isolasi:
System call menjaga agar program tidak langsung mengakses perangkat keras atau memori sistem secara sembarangan, dengan membatasi akses melalui layanan kernel yang terkontrol.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
strace ls
strace -e trace=open,read,write,close cat /etc/passwd
dmesg | tail -n 10
```
<img width="1919" height="1079" alt="Screenshot 2025-10-16 122558" src="https://github.com/user-attachments/assets/bcedb2a7-f09b-4bc4-ab9d-763a06cde382" />
<img width="1898" height="1063" alt="Screenshot 2025-10-16 123006" src="https://github.com/user-attachments/assets/bb7b5267-142e-4f3f-a474-a1760ebe46e9" />


<img width="1918" height="1079" alt="Screenshot 2025-10-16 122733" src="https://github.com/user-attachments/assets/e44db8d6-8fd0-41bb-b070-7302a4c64c02" />

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:


---

## Analisis
- Analisis bagaimana file dibuka, dibaca, dan ditutup oleh kernel.
- Catat 5–10 system call pertama yang muncul dan jelaskan fungsinya.  
- Amati log kernel yang muncul. Apa bedanya output ini dengan output dari program biasa?
---
1. Gambaran Umum: Apa yang Terjadi Saat File Diakses

Ketika program membuka, membaca, dan menutup file (misalnya dengan kode C berikut):

int fd = open("data.txt", O_RDONLY);
read(fd, buffer, 100);
close(fd);


program tidak langsung berinteraksi dengan disk, melainkan:

Memanggil system call (open(), read(), close()) ke kernel.

Kernel mengeksekusi fungsi internal untuk:

Memeriksa hak akses file.

Menemukan lokasi file di sistem berkas.

Membaca blok dari disk (melalui buffer cache).

Mengembalikan data ke ruang pengguna.

Setelah selesai, kernel mengembalikan kontrol ke program pengguna.

 2. System Call Pertama yang Muncul

Jika kamu melacak program dengan strace, hasil awalnya (tergantung konteks) bisa seperti ini:

strace ./program


Output contoh:

execve("./program", ["./program"], [/* env */]) = 0
brk(NULL)                               = 0x5631e6900000
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, <...>, 832)                     = 832
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = ...
close(3)                                = 0
openat(AT_FDCWD, "data.txt", O_RDONLY)  = 3
read(3, "Isi file ...", 100)            = 100
close(3)                                = 0

 3. Penjelasan 5–10 System Call Pertama
No	System Call	Fungsi
1	execve()	Menjalankan program baru di dalam proses ini. Kernel memuat biner ./program ke memori.
2	brk()	Mengatur batas segmen heap proses. Digunakan untuk alokasi dinamis (sebelum malloc()).
3	access()	Mengecek apakah file tertentu ada dan dapat diakses (sering dipanggil oleh dynamic linker).
4	openat()	Membuka file (open() versi modern). Mengembalikan file descriptor untuk libc.so.6 atau file target.
5	read()	Membaca data dari file descriptor ke buffer di ruang pengguna. Kernel menyalin data dari buffer cache atau disk.
6	mmap()	Memetakan file atau area memori ke ruang alamat proses (digunakan untuk library, buffer I/O).
7	close()	Menutup file descriptor dan melepaskan resource kernel.
8	openat() (kedua)	Membuka file target sebenarnya — misalnya "data.txt".
9	read() (kedua)	Membaca isi file yang diminta oleh program pengguna.
10	close() (kedua)	Menutup file data setelah selesai dibaca.
 4. Log Kernel yang Muncul

Jika kamu memantau log kernel (misalnya dengan dmesg -w atau journalctl -kf), kamu tidak akan melihat output system call seperti di strace.

Namun, kernel dapat menampilkan log jika:

Ada error, seperti:

permission denied

file not found

I/O error pada disk

Ada aktivitas khusus (misalnya auditd aktif, atau debugging syscalls via LSM/Audit).

Contoh log kernel:

audit: type=1400 audit(16912345.567:12): avc: denied { read } for pid=1024 comm="program" name="data.txt" dev="sda1" ino=34567 scontext=user_u tcontext=system_u tclass=file

 5. Perbedaan Output strace vs Log Kernel
Aspek	strace Output	Log Kernel
Sumber	Hasil user-space tracing (intercept system call)	Dihasilkan oleh kernel langsung
Tujuan	Melihat aktivitas program (urutan system call)	Melihat peristiwa sistem (error, security, driver)
Isi	Nama syscall, parameter, nilai balik	Informasi sistem, peringatan, error I/O, audit
Contoh	openat(AT_FDCWD, "data.txt", O_RDONLY) = 3	audit: denied { read } for pid=1024 ...
 6. Kesimpulan

File dibuka, dibaca, dan ditutup melalui system call open(), read(), dan close(), yang diproses sepenuhnya oleh kernel.

System call awal (seperti execve, brk, openat, mmap, dll.) menunjukkan proses bagaimana program dimuat dan file diakses.

Log kernel hanya mencatat peristiwa penting atau error, bukan seluruh detail system call seperti di strace.

Jadi, strace → untuk tracing aktivitas program, sedangkan dmesg/log kernel → untuk memantau kejadian di level kernel.

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
System call menjadi mekanisme utama komunikasi antara program pengguna dan kernel, sehingga memungkinkan program mengakses layanan sistem operasi secara aman dan terkontrol.

Setiap pemanggilan system call menyebabkan perpindahan dari user mode ke kernel mode, yang menunjukkan adanya lapisan keamanan dan isolasi antara aplikasi dan inti sistem.

Melalui praktikum ini, mahasiswa memahami cara kerja fungsi-fungsi seperti fork(), read(), atau write(), serta bagaimana operasi dasar sistem (proses, file, dan I/O) bergantung pada system call.


---

## Quiz
1.  Apa fungsi utama system call dalam sistem operasi?

Fungsi utama system call dalam sistem operasi adalah sebagai jembatan antara program aplikasi dan kernel sistem operasi. Dengan kata lain, system call memungkinkan program aplikasi untuk meminta layanan atau sumber daya yang hanya dapat diakses oleh sistem operasi
   
2. Sebutkan 4 kategori system call yang umum digunakan.

1. Process Control (Kontrol Proses)

Digunakan untuk membuat, mengelola, dan mengakhiri proses.

Contoh system call:

fork() – membuat proses baru

exec() – mengganti program yang dijalankan oleh suatu proses

exit() – mengakhiri proses

wait() – menunggu proses anak selesai

2. File Management (Manajemen File)

Digunakan untuk mengakses dan memanipulasi file serta direktori.

Contoh system call:

open() – membuka file

read() – membaca isi file

write() – menulis ke file

close() – menutup file

unlink() – menghapus file

3. Device Management (Manajemen Perangkat)

Digunakan untuk mengelola perangkat input/output.

Contoh system call:

ioctl() – mengatur parameter perangkat

read() – membaca dari perangkat

write() – menulis ke perangkat

open() / close() – membuka/menutup perangkat (diperlakukan seperti file)

4. Information Maintenance (Pemeliharaan Informasi)

Digunakan untuk memperoleh atau mengatur informasi tentang sistem dan proses.

Contoh system call:

getpid() – mendapatkan ID proses

alarm() – mengatur timer

time() – mendapatkan waktu sistem

getuid() – mendapatkan ID pengguna


3. mengapa system call tidak bisa dipanggil langsung oleh user program?
  
   1. Keamanan Sistem

User program berjalan di mode user, sedangkan system call dijalankan di mode kernel.

Jika program biasa bisa langsung mengakses kernel, maka pengguna bisa merusak sistem, mencuri data, atau mengakses perangkat keras secara tidak sah.

2. Perlindungan Kernel

Kernel adalah bagian inti sistem operasi yang sangat penting.

Dengan membatasi akses langsung, sistem mencegah user program mengubah atau merusak struktur internal kernel, yang bisa menyebabkan crash atau kerusakan sistem total (kernel panic)

3. Kontrol & Validasi

System call memungkinkan validasi parameter dan pengecekan izin akses sebelum menjalankan perintah.

Ini mencegah kesalahan fatal seperti menulis ke alamat memori yang tidak diizinkan atau mengakses file yang tidak memiliki izin.

4. Peralihan Mode (Mode Switching)

Untuk mengeksekusi system call, program harus menggunakan instruksi khusus (seperti int 0x80 di Linux lama, atau syscall di sistem modern).

Ini menyebabkan CPU berpindah dari mode user ke mode kernel, lalu kembali setelah system call selesai — proses ini disebut context switch dan hanya bisa terjadi melalui jalur yang dikontrol OS.


Tugas

Dokumentasikan hasil eksperimen strace dan dmesg dalam bentuk tabel observasi.

1 .Buat diagram alur system call dari aplikasi → kernel → hardware → kembali ke aplikasi.

2.Tulis analisis 400–500 kata tentang:
-Mengapa system call penting untuk keamanan OS?
-Bagaimana OS memastikan transisi user–kernel berjalan aman?

3.Sebutkan contoh system call yang sering digunakan di Linux.

| No | Perintah yang Dijalankan | Tujuan Observasi                                 | Cuplikan Output `strace`        | Analisis / Interpretasi                                                         | Kesimpulan                                                             |               |                                                                              |                                                                           |
| -- | ------------------------ | ------------------------------------------------ | ------------------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| 1  | `strace ls`              | Melihat sistem call saat menampilkan daftar file | `openat(AT_FDCWD, ".", O_RDONLY | O_NONBLOCK                                                                      | O_CLOEXEC                                                              | O_DIRECTORY)` | Program memanggil syscall `openat()` untuk membuka direktori kerja saat ini. | `ls` membaca isi direktori melalui syscall `openat()` dan `getdents64()`. |
| 2  | `strace cat file.txt`    | Mengamati proses pembacaan file                  | `read(3, "Hello\n", 6) = 6`     | Syscall `read()` digunakan untuk membaca isi file dari descriptor 3.            | `cat` membaca isi file dan menampilkannya ke stdout melalui `write()`. |               |                                                                              |                                                                           |
| 3  | `strace -p 1234`         | Melacak syscall dari proses berjalan (PID 1234)  | `wait4(1234, ...)`              | `strace` menempel pada proses untuk melihat aktivitas syscall secara real time. | Berguna untuk debugging proses yang tidak merespons.                   |               |                                                                              |                                                                           |


                                                                          |                                                                           |
| No | Aktivitas / Kondisi                           | Cuplikan Output `dmesg`                                                             | Analisis / Interpretasi                                             | Waktu / Timestamp | Kesimpulan                                                                        |
| -- | --------------------------------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ----------------- | --------------------------------------------------------------------------------- |
| 1  | Menyambungkan USB drive                       | `[12345.678901] usb 1-1: new high-speed USB device number 4 using xhci_hcd`         | Kernel mendeteksi perangkat USB baru dan menginisialisasinya.       | 12345.678 s       | Sistem mengenali perangkat USB dengan benar.                                      |
| 2  | Menjalankan program dengan segmentation fault | `[23456.789012] myprog[1234]: segfault at 0 ip 00007f... error 4 in libc.so.6[...]` | Kernel mencatat terjadinya segmentation fault pada proses `myprog`. | 23456.789 s       | Terjadi pelanggaran memori; perlu analisis lebih lanjut pada pointer atau buffer. |
| 3  | Booting sistem                                | `[0.000000] Linux version 6.5.0 ...`                                                | Kernel mencatat versi, parameter boot, dan perangkat yang dikenali. | 0.000 s           | Informasi dasar kernel saat sistem mulai berjalan.                                |

2. **Analisis: Pentingnya System Call untuk Keamanan Sistem Operasi**

System call (panggilan sistem) merupakan antarmuka penting antara program pengguna (user space) dan kernel dalam sistem operasi (OS). Melalui system call, aplikasi dapat meminta layanan inti dari kernel seperti manajemen file, proses, dan memori. Namun, di balik fungsinya yang fundamental, system call juga memainkan peran vital dalam **menjaga keamanan sistem operasi**. Tanpa mekanisme system call yang aman dan terkontrol, program pengguna bisa mengakses sumber daya kernel secara langsung, yang berpotensi menyebabkan **kerusakan sistem, kebocoran data, atau eskalasi hak akses**.

Pertama, system call penting untuk keamanan karena berfungsi sebagai **gerbang kontrol akses** antara user space dan kernel space. Kernel adalah bagian paling sensitif dari OS — ia memiliki hak istimewa tertinggi dan mengatur semua sumber daya sistem. Oleh karena itu, tidak boleh ada program pengguna yang dapat berinteraksi langsung dengan kernel tanpa melalui mekanisme yang terverifikasi. Dengan adanya system call, semua permintaan dari aplikasi akan melalui **lapisan validasi dan pemeriksaan izin**. Misalnya, ketika sebuah proses mencoba membaca file, kernel akan memeriksa apakah proses tersebut memiliki hak akses yang sesuai sebelum mengizinkan operasi dilakukan. Hal ini mencegah aplikasi berbahaya mengakses data atau memodifikasi konfigurasi sistem secara sembarangan.

Kedua, sistem operasi memastikan **transisi antara mode pengguna (user mode)** dan **mode kernel (kernel mode)** berjalan aman dengan menggunakan **mekanisme proteksi perangkat keras** dan **prosedur validasi perangkat lunak**. Dalam arsitektur CPU modern seperti x86, terdapat bit khusus yang menunjukkan tingkat hak akses (ring level). Saat program pengguna menjalankan instruksi system call, CPU akan secara otomatis berpindah dari ring 3 (user mode) ke ring 0 (kernel mode) menggunakan **interrupt gate** atau **system call interface (seperti `syscall` atau `int 0x80`)**. Transisi ini dilakukan melalui **tabel entri system call (system call table)** yang berisi daftar fungsi kernel yang dapat dipanggil. OS memastikan bahwa hanya system call yang sah dan telah terdaftar yang bisa diakses. Selain itu, kernel melakukan validasi parameter (seperti pointer dan buffer) untuk mencegah eksploitasi seperti **buffer overflow** atau pointer injection yang dapat memanipulasi memori kernel.

Ketiga, sistem operasi modern juga menggunakan isolasi memori dan pengendalian hak akses berbasis pengguna (User ID, Group ID, dan capability system) untuk membatasi dampak dari system call berbahaya. Misalnya, hanya proses dengan hak superuser (root) yang diizinkan menjalankan system call tertentu seperti `mount()` atau `reboot()`.

Beberapa contoh system call yang sering digunakan di Linux antara lain:

* `fork()` – membuat proses baru.
* `execve()` – menjalankan program baru.
* `open()` dan `read()` – membuka dan membaca file.
* `write()` – menulis data ke file atau output.
* `close()` – menutup file descriptor.
* `wait()` – menunggu proses anak selesai.
* `socket()` dan `connect()` – membuat dan menghubungkan soket jaringan.

Dengan demikian, system call tidak hanya berfungsi sebagai mekanisme komunikasi antara aplikasi dan kernel, tetapi juga sebagai lapisan keamanan fundamental Melalui validasi, isolasi, dan kontrol akses yang ketat pada setiap transisi user–kernel, OS mampu menjaga integritas sistem, melindungi data pengguna, serta mencegah eksploitasi terhadap sumber daya kritis.

3. System call seperti open(), read(), write(), dan close() merupakan dasar bagi hampir semua operasi file di Linux. Sedangkan fork(), exec(), dan wait() berperan penting dalam manajemen proses. Semua system call ini menjadi interface penting antara user space dan kernel space, memastikan aplikasi dapat berinteraksi dengan perangkat keras dan sumber daya sistem secara aman.




## Refleksi Diri
Tuliskan secara singkat:
- mengalahlakan rasa malas 
- ada sedikit kendakala di ubutu 

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
