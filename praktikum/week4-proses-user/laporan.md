
# Laporan Praktikum Minggu [X]
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : [LUTHFI AULIA RAHMAN]  
- **NIM**   : [250202948]  
- **Kelas** : [1 IKRB]

---

## Tujuan

1. Menjelaskan konsep proses dan user dalam sistem operasi Linux.
2. Menampilkan daftar proses yang sedang berjalan dan statusnya.
3. Menggunakan perintah untuk membuat dan mengelola user.
4. Menghentikan atau mengontrol proses tertentu menggunakan PID.
5. Menjelaskan kaitan antara manajemen user dan keamanan sistem.


### **1. Konsep Proses dan User dalam Sistem Operasi Linux**

**a. Proses (Process)**

* Proses adalah **program yang sedang dieksekusi** oleh sistem operasi.
* Setiap proses memiliki **PID (Process ID)** unik dan berjalan di ruang memori sendiri.
* Proses dapat memiliki **parent process** (proses induk) dan **child process** (proses turunan).
* Linux menggunakan mekanisme **multitasking**, sehingga banyak proses bisa berjalan secara bersamaan.

 **Contoh konsep:**    

* Saat kamu menjalankan `firefox`, sistem akan membuat proses baru dengan PID tertentu.
* Kamu bisa melihat proses induk Firefox adalah `bash` (jika dijalankan dari terminal).


**b. User (Pengguna)**

* Setiap **user** di Linux memiliki identitas unik berupa:

  * **Username**
  * **UID (User ID)**
  * **GID (Group ID)**
  * **Home directory**
  * **Shell login**
* User dikelola melalui file `/etc/passwd` dan hak aksesnya diatur di `/etc/group` serta `/etc/shadow`.

 **Contoh entri user di `/etc/passwd`:**

```
lutfi:x:1001:1001:Lutfi,,,:/home/lutfi:/bin/bash
```

Artinya:

* `lutfi` = nama user
* `1001` = UID
* `1001` = GID
* `/home/lutfi` = direktori home
* `/bin/bash` = shell default

---

### **2. Menampilkan Daftar Proses yang Sedang Berjalan dan Statusnya**

Gunakan beberapa perintah berikut:

| Perintah | Fungsi                                                             | Contoh Output                                     |
| -------- | ------------------------------------------------------------------ | ------------------------------------------------- |
| `ps aux` | Menampilkan semua proses lengkap dengan user, PID, CPU, dan memori | `root  1  0.0  0.1  /sbin/init`                   |
| `top`    | Menampilkan proses secara real-time                                | Menampilkan daftar proses dan resource CPU/memori |
| `htop`   | Versi interaktif dari `top` (lebih berwarna dan mudah dibaca)      | Bisa memfilter dan menghentikan proses langsung   |
| `pstree` | Menampilkan **hierarki proses** dalam bentuk pohon                 | Menunjukkan hubungan parent-child antar proses    |

 **Contoh:**

```
$ pstree
systemd─┬─NetworkManager───2*[{NetworkManager}]
        ├─sshd───bash───top
        └─systemd-logind
```

---

### **3. Menggunakan Perintah untuk Membuat dan Mengelola User**

| Perintah                      | Fungsi                                                    | Contoh                          |
| ----------------------------- | --------------------------------------------------------- | ------------------------------- |
| `sudo adduser namauser`       | Membuat user baru lengkap dengan direktori home dan shell | `sudo adduser student`          |
| `sudo userdel namauser`       | Menghapus user dari sistem                                | `sudo userdel student`          |
| `sudo passwd namauser`        | Mengatur atau mengganti password user                     | `sudo passwd student`           |
| `sudo usermod -aG group user` | Menambahkan user ke dalam grup tertentu                   | `sudo usermod -aG sudo student` |
| `id namauser`                 | Menampilkan UID, GID, dan grup user                       | `id lutfi`                      |

---

### **4. Menghentikan atau Mengontrol Proses Tertentu Menggunakan PID**

Gunakan perintah `kill`, `killall`, atau `pkill` untuk menghentikan proses berdasarkan PID atau nama proses.

| Perintah              | Fungsi                                                 | Contoh            |
| --------------------- | ------------------------------------------------------ | ----------------- |
| `kill PID`            | Menghentikan proses berdasarkan PID                    | `kill 1234`       |
| `kill -9 PID`         | Memaksa menghentikan proses (SIGKILL)                  | `kill -9 1234`    |
| `killall nama_proses` | Menghentikan semua proses dengan nama yang sama        | `killall firefox` |
| `pkill nama_proses`   | Menghentikan proses berdasarkan nama (mirip `killall`) | `pkill bash`      |

**Contoh:**

```
$ ps aux | grep firefox
lutfi   2345  2.3  ...  /usr/lib/firefox/firefox
$ kill 2345
```

---

### **5. Kaitan antara Manajemen User dan Keamanan Sistem**

Manajemen user berperan penting dalam **keamanan sistem Linux**, karena:

| Aspek                        | Penjelasan                                                                                                                                                        |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Pemisoliran Akses**        | Setiap user memiliki ruang kerja dan izin akses terbatas ke file/direktori tertentu. Ini mencegah pengguna lain mengubah atau menghapus file yang bukan miliknya. |
| **Hak Istimewa (Privilege)** | Hanya **root** yang memiliki hak penuh untuk mengubah konfigurasi sistem. Pengguna biasa tidak dapat melakukan operasi kritis tanpa izin.                         |
| **Group Management**         | Dengan grup, sistem bisa mengatur hak akses bersama untuk beberapa user (contoh: grup `sudo`, `www-data`).                                                        |
| **Audit & Logging**          | Aktivitas user dapat dilacak melalui log sistem (misal `/var/log/auth.log`) untuk mendeteksi tindakan mencurigakan.                                               |
| **Prinsip Least Privilege**  | Setiap user hanya diberi hak minimum yang diperlukan, untuk mengurangi risiko kesalahan atau serangan.                                                            |

 **Kesimpulan:**

> Pengelolaan user yang baik — dengan izin (`chmod`, `chown`), grup, dan hak akses yang tepat — adalah fondasi utama keamanan sistem Linux.



## Dasar Teori
1. Jelaskan setiap output dan fungsinya.
2. Jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND.
3. Amati hierarki proses dan identifikasi proses induk (init/systemd)

### **1. Penjelasan setiap output dan fungsinya**

Ketika kamu menjalankan perintah seperti `ps aux`, `top`, atau `htop` di Linux, kamu akan melihat daftar **proses** yang sedang berjalan.
Setiap baris menunjukkan **satu proses** yang aktif di sistem.
Fungsi utamanya adalah untuk **memantau dan mengelola proses** — misalnya mengetahui siapa pemilik proses, berapa besar CPU/memori yang digunakan, dan apa perintah yang dijalankan.

Contoh output dari `ps aux`:

```
USER       PID  %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1   0.0  0.1 167920  8300 ?        Ss   10:00   0:03 /sbin/init
user      2145   1.2  2.3 812340 94800 ?        Sl   10:15   1:45 /usr/bin/gnome-shell
user      3321   0.3  0.8 465120 32240 pts/0    R+   10:35   0:01 ps aux
```

---

### **2. Penjelasan kolom penting**

| Kolom                | Keterangan                                                                                                              |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **USER**             | Menunjukkan nama user (pemilik proses). Misalnya `root`, `user`, `daemon`.                                              |
| **PID (Process ID)** | Nomor unik untuk setiap proses. Digunakan untuk mengontrol atau menghentikan proses dengan perintah seperti `kill PID`. |
| **%CPU**             | Persentase penggunaan CPU oleh proses tersebut. Nilai tinggi berarti proses menggunakan banyak sumber daya prosesor.    |
| **%MEM**             | Persentase penggunaan memori RAM oleh proses tersebut. Berguna untuk mendeteksi proses yang boros memori.               |
| **VSZ**              | Virtual memory size – total memori virtual (dalam KB) yang digunakan proses.                                            |
| **RSS**              | Resident Set Size – memori fisik aktual (RAM) yang digunakan proses.                                                    |
| **TTY**              | Terminal terkait proses (misalnya `pts/0` untuk terminal aktif, atau `?` jika tidak terkait terminal).                  |
| **STAT**             | Status proses:                                                                                                          |

* **R** = Running
* **S** = Sleeping (idle)
* **T** = Stopped
* **Z** = Zombie (sudah berhenti tapi belum dihapus)
* **Ss** = Sleeping dengan status proses sistem |
  | **START** | Waktu atau tanggal kapan proses dimulai. |
  | **TIME** | Total waktu CPU yang sudah digunakan oleh proses. |
  | **COMMAND** | Perintah atau program yang dijalankan (misalnya `/sbin/init`, `bash`, `firefox`). |

---

### **3. Hierarki proses dan identifikasi proses induk**

Di Linux, setiap proses memiliki **proses induk (parent process)**, kecuali proses pertama di sistem yaitu **`init` atau `systemd`**.

Kamu dapat melihat **hierarki proses** menggunakan perintah:

```bash
pstree
```

Contoh output:

```
systemd─┬─NetworkManager───{NetworkManager}
        ├─sshd───bash───pstree
        ├─gnome-shell───Xorg
        └─cron───cronjob.sh
```

**Penjelasan:**

* **systemd** → adalah **proses induk utama (PID 1)** yang dijalankan pertama kali saat sistem boot.
  Semua proses lain merupakan turunan (anak) dari `systemd`.
* **NetworkManager**, **sshd**, **gnome-shell**, **cron** → adalah proses turunan dari `systemd`.
* Misalnya, `sshd` memiliki proses anak `bash`, dan `bash` kemudian menjalankan `pstree`.

---

### **Kesimpulan**

* Output dari `ps`, `top`, atau `htop` menunjukkan daftar proses yang sedang berjalan beserta penggunaan sumber dayanya.
* Kolom **PID, USER, %CPU, %MEM, COMMAND** penting untuk memahami siapa yang menjalankan proses dan berapa besar sumber daya yang digunakan.
* Dengan `pstree`, kamu bisa melihat **struktur pohon proses**, di mana **`systemd` (PID 1)** adalah induk dari seluruh proses di sistem Linux.


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
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. Apa fungsi dari proses init atau systemd dalam sistem Linux?
2. Apa perbedaan antara kill dan killall?
3. Mengapa user root memiliki hak istimewa di sistem Linux?


### **1. Fungsi dari proses `init` atau `systemd` dalam sistem Linux**

`init` (pada sistem lama) dan **`systemd`** (pada sistem modern) adalah **proses pertama yang dijalankan oleh kernel saat sistem booting**.
PID-nya selalu **1** (`PID 1`) dan menjadi **induk dari semua proses lain**.

🔹 **Fungsi utama `init` / `systemd`:**

* **Menginisialisasi sistem:** Menjalankan skrip booting, mengatur environment awal.
* **Menjalankan layanan (service):** Mengaktifkan proses penting seperti login, jaringan, cron, dsb.
* **Mengatur urutan startup:** Menentukan mana layanan yang dijalankan dulu, mana yang belakangan.
* **Mengawasi proses:** Jika ada service yang crash, `systemd` bisa otomatis me-restart-nya.
* **Mengelola shutdown dan reboot:** Menghentikan semua proses dengan urutan aman sebelum sistem dimatikan.


### **2. Perbedaan antara `kill` dan `killall`**

Keduanya digunakan untuk **menghentikan proses**, tapi caranya berbeda:

| Perintah  | Cara Kerja                                           | Contoh               | Keterangan                                     |
| --------- | ---------------------------------------------------- | -------------------- | ---------------------------------------------- |
| `kill`    | Menghentikan **proses berdasarkan PID (Process ID)** | `kill 1234`          | Hanya menghentikan proses dengan PID 1234      |
| `killall` | Menghentikan **semua proses dengan nama tertentu**   | `killall firefox`    | Semua proses bernama *firefox* akan dihentikan |
|           |                                                      | `kill -9 1234`       | Mengirim sinyal `SIGKILL` untuk paksa berhenti |
|           |                                                      | `killall -9 firefox` | Paksa hentikan semua proses *firefox*          |

 

### **3. Mengapa user `root` memiliki hak istimewa di sistem Linux**

User **root** adalah **superuser** — akun dengan **akses penuh ke seluruh sistem**.

🔹 **Alasan root memiliki hak istimewa:**

1. **Manajemen sistem:** Root perlu menginstal paket, mengubah konfigurasi sistem, dan mengelola user lain.
2. **Kontrol penuh atas file system:** Root bisa membaca, menulis, atau menghapus file apa pun (termasuk milik user lain).
3. **Akses langsung ke perangkat keras:** Hanya root yang bisa mengatur jaringan, disk, kernel module, dsb.
4. **Keamanan & isolasi:** Hanya satu user (root) yang memiliki izin total, mencegah pengguna biasa merusak sistem.

**tugas**

1. Dokumentasikan hasil semua perintah dan jelaskan fungsi tiap perintah.
2. Gambarkan hierarki proses dalam bentuk diagram pohon (pstree) di laporan.
3. Jelaskan hubungan antara user management dan keamanan sistem Linux.



## **1. Dokumentasikan hasil semua perintah dan jelaskan fungsinya**

| **Perintah**                | **Hasil (Contoh Output)**                                     | **Fungsi / Penjelasan**                                                                |
| --------------------------- | ------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `ps`                        | Menampilkan daftar proses aktif (misal: PID, TTY, TIME, CMD)  | Menunjukkan proses yang sedang berjalan di terminal saat ini.                          |
| `ps -ef`                    | Menampilkan semua proses secara lengkap (dari semua user)     | Memberikan tampilan penuh proses dengan UID, PID, PPID, waktu mulai, dan perintah.     |
| `top`                       | Menampilkan proses yang sedang berjalan secara dinamis        | Digunakan untuk memantau penggunaan CPU, memori, dan beban sistem secara real-time.    |
| `htop`                      | (Jika tersedia) Menampilkan proses dalam antarmuka interaktif | Versi lebih user-friendly dari `top`, memungkinkan scroll dan kill proses langsung.    |
| `pstree`                    | Menampilkan proses dalam bentuk pohon hierarki                | Menunjukkan hubungan induk–anak antara proses dalam sistem.                            |
| `who`                       | Menampilkan user yang sedang login ke sistem                  | Memantau siapa saja yang sedang menggunakan sistem.                                    |
| `id`                        | Menampilkan UID, GID, dan grup tambahan user                  | Menunjukkan identitas dan hak akses user saat ini.                                     |
| `adduser namauser`          | Menambahkan user baru ke sistem                               | Membuat akun baru lengkap dengan home directory dan shell bawaan.                      |
| `deluser namauser`          | Menghapus akun user dari sistem                               | Menghapus user dari sistem (dapat juga menghapus home directory dengan opsi tertentu). |
| `usermod -aG sudo namauser` | Menambahkan user ke grup `sudo`                               | Memberikan hak administratif (akses root) pada user.                                   |
| `chmod 755 file`            | Mengubah hak akses file                                       | Memberikan izin `rwxr-xr-x` (pemilik penuh, grup dan others hanya baca/jalankan).      |
| `chown user:group file`     | Mengubah kepemilikan file                                     | Mengatur siapa pemilik dan grup pemilik suatu file.                                    |

> **Catatan:** Semua hasil di atas sebaiknya dicatat di `laporan.md` lengkap dengan *output terminal* (salinan hasil perintah).

---

## **2. Diagram Hierarki Proses (pstree)**

Contoh hasil perintah:

```bash
$ pstree
systemd─┬─NetworkManager───2*[{NetworkManager}]
        ├─sshd───sshd───bash───pstree
        ├─cron
        ├─dbus-daemon
        ├─gnome-shell───Xorg
        └─...
```

**Diagram pohon hierarki proses:**

```
systemd
├── NetworkManager
│   └── {NetworkManager}
├── sshd
│   ├── sshd (session user)
│   │   └── bash
│   │       └── pstree
├── cron
├── dbus-daemon
└── gnome-shell
    └── Xorg
```

**Penjelasan:**

* `systemd` adalah proses **utama (PID 1)** — induk dari semua proses di sistem Linux.
* Proses seperti `sshd`, `cron`, dan `dbus-daemon` adalah **anak** dari `systemd`.
* Proses `bash` merupakan shell yang dijalankan oleh user setelah login.
* `pstree` adalah proses terakhir yang dijalankan oleh `bash` untuk menampilkan hierarki ini.

---

## **3. Hubungan antara User Management dan Keamanan Sistem Linux**

Manajemen user sangat berperan penting dalam **keamanan sistem Linux**, karena setiap aktivitas dan akses dikontrol berdasarkan identitas user dan grup.

### 🔹 **Hubungan dan Dampaknya:**

| **Aspek User Management**                     | **Pengaruh terhadap Keamanan**                                            |
| --------------------------------------------- | ------------------------------------------------------------------------- |
| **Pembagian hak akses (user, group, others)** | Menentukan siapa yang dapat membaca, menulis, atau menjalankan file.      |
| **Manajemen akun dan grup**                   | Memungkinkan pembatasan akses hanya kepada user tertentu sesuai peran.    |
| **User privilege (root vs regular user)**     | Mencegah user biasa mengubah konfigurasi penting sistem.                  |
| **File permission (chmod)**                   | Melindungi file penting agar tidak dimodifikasi oleh user tak berwenang.  |
| **Kepemilikan file (chown)**                  | Memastikan setiap file memiliki tanggung jawab keamanan yang jelas.       |
| **Penggunaan sudo**                           | Memberi akses administratif sementara dengan audit trail (log aktivitas). |
| **Penghapusan akun tidak aktif**              | Mengurangi risiko penyalahgunaan akun lama.                               |

### **Kesimpulan:**

Manajemen user adalah **fondasi utama keamanan Linux**. Dengan mengatur siapa yang dapat mengakses apa, sistem dapat mencegah kebocoran data, perubahan konfigurasi tidak sah, dan serangan internal. Kombinasi dari user, grup, permission (`chmod`), dan ownership (`chown`) menjaga sistem tetap aman dan terkontrol.



## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
