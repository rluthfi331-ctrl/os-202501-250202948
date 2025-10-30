

# Laporan Praktikum Minggu [4]
Topik: [proses user]

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

---

## Dasar Teori

1. Konsep Proses dalam Sistem Operasi

- Proses adalah program yang sedang dieksekusi beserta semua konteksnya (seperti memori, status CPU, dan sumber daya lain).
- Setiap proses memiliki PID (Process ID) unik untuk identifikasi dan dapat membuat proses anak (child process).
- Linux mengatur proses menggunakan scheduler, yang menentukan urutan eksekusi agar sumber daya CPU digunakan secara efisien.


2. Konsep User dalam Sistem Operasi
User adalah identitas yang digunakan untuk mengakses sistem, dilengkapi dengan UID (User ID) dan GID (Group ID).
Sistem Linux menggunakan manajemen user dan group untuk mengatur hak akses terhadap file, direktori, dan proses.

User dibagi menjadi:

- Root (superuser): memiliki kontrol penuh terhadap sistem.
- User biasa: memiliki hak terbatas demi keamanan.


3. Hubungan Proses dan User terhadap Keamanan Sistem
- Setiap proses di Linux berjalan atas nama user tertentu, sehingga hak akses proses dibatasi oleh izin user tersebut.
- Mekanisme ini mencegah proses milik user biasa mengubah konfigurasi sistem atau membaca data user lain.
- Dengan demikian, manajemen user dan proses menjadi bagian penting dari kontrol keamanan dan isolasi sistem operasi.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).  
   - Pastikan Anda sudah login sebagai user non-root.  
   - Siapkan folder kerja:
     ```
     praktikum/week4-proses-user/
     ```

2. **Eksperimen 1 – Identitas User**
   Jalankan perintah berikut:
   ```bash
   whoami
   id
   groups
   ```
   - Jelaskan setiap output dan fungsinya.  
   - Buat user baru (jika memiliki izin sudo):
     ```bash
     sudo adduser praktikan
     sudo passwd praktikan
     ```
   - Uji login ke user baru.

3. **Eksperimen 2 – Monitoring Proses**
   Jalankan:
   ```bash
   ps aux | head -10
   top -n 1
   ```
   - Jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND.  
   - Simpan tangkapan layar `top` ke:
     ```
     praktikum/week4-proses-user/screenshots/top.png
     ```

4. **Eksperimen 3 – Kontrol Proses**
   - Jalankan program latar belakang:
     ```bash
     sleep 1000 &
     ps aux | grep sleep
     ```
   - Catat PID proses `sleep`.  
   - Hentikan proses:
     ```bash
     kill <PID>
     ```
   - Pastikan proses telah berhenti dengan `ps aux | grep sleep`.

5. **Eksperimen 4 – Analisis Hierarki Proses**
   Jalankan:
   ```bash
   pstree -p | head -20
   ```
   - Amati hierarki proses dan identifikasi proses induk (`init`/`systemd`).  
   - Catat hasilnya dalam laporan.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 4 - Manajemen Proses & User"
   git push origin main
   ``` 
---

## Hasil Eksekusi

<img width="1919" height="1079" alt="Screenshot 2025-10-30 090853" src="https://github.com/user-attachments/assets/ae1f63f8-452d-4cc9-af32-5dd7ac658e3b" />

<img width="1919" height="1078" alt="Screenshot 2025-10-30 090909" src="https://github.com/user-attachments/assets/8142759a-32a1-40f3-826d-4b2e61e39080" />

<img width="1919" height="1078" alt="Screenshot 2025-10-30 090932" src="https://github.com/user-attachments/assets/94a11ccd-041e-4aee-9215-63c8778d47fc" />




---

## Analisis
- Jelaskan setiap output dan fungsinya.
- Jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND.
- Catat PID proses sleep.
- Amati hierarki proses dan identifikasi proses induk (init/systemd).
 ### 1. Jelaskan setiap output dan fungsinya.
1. Perintah `whoami`

Fungsi:
Menampilkan nama user yang sedang login atau menjalankan shell saat ini.

Contoh output:
`whoami`
``` bash 
lutfi
```

Penjelasan:
Output lutfi menunjukkan bahwa user aktif saat ini adalah lutfi.
Perintah ini sangat sederhana — berguna untuk cepat mengecek user saat ini, terutama saat menggunakan sudo atau berpindah user dengan su.

2. Perintah `id`

Fungsi:Menampilkan informasi identitas user dalam bentuk angka dan nama, termasuk,UID (User ID),GID (Group ID),Grup tambahan yang diikuti user

Contoh output:`id`
``` bash 
uid=1000(lutfi) gid=1000(lutfi) groups=1000(lutfi),27(sudo),1001(project)
```

Penjelasan setiap bagian:
- uid=1000(lutfi) → ID unik untuk user lutfi.
- gid=1000(lutfi) → ID grup utama user lutfi.
- groups=... → daftar semua grup yang diikuti user:
- 1000(lutfi) = grup utama
- 27(sudo) = grup dengan hak administratif
- 1001(project) = grup tambahan

Fungsi penting: membantu administrator mengetahui hak akses dan keanggotaan grup user.

3. Perintah `groups`

Fungsi: Menampilkan semua grup yang diikuti oleh user saat ini (lebih ringkas dari id).

Contoh output:

`groups` 
``` bash
lutfi sudo project
```

Penjelasan:

lutfi → grup utama user

sudo dan project → grup tambahan
Artinya user lutfi memiliki hak sebagai anggota grup sudo dan project.

 ### 2. jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND.
 | Kolom                | Arti / Fungsi                                                                                                                                                                     |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **USER**             | Menunjukkan **nama user (pengguna)** yang menjalankan proses tersebut. Contoh: `root`, `student`, `www-data`. Ini penting untuk keamanan karena menunjukkan siapa pemilik proses. |
| **PID (Process ID)** | Nomor unik yang diberikan sistem kepada setiap proses yang berjalan. Digunakan untuk **mengidentifikasi** dan **mengontrol** proses (misalnya dengan `kill PID`).                 |
| **%CPU**             | Menunjukkan **persentase penggunaan CPU** oleh proses tersebut. Semakin tinggi nilainya, semakin besar beban CPU yang digunakan.                                                  |
| **%MEM**             | Persentase **penggunaan memori (RAM)** oleh proses. Berguna untuk memantau proses yang mengonsumsi banyak memori.                                                                 |
| **COMMAND**          | Menampilkan **nama program atau perintah** yang dijalankan beserta argumennya. Contoh: `/usr/bin/firefox`, `bash`, `systemd`.                                                     |

USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.1 168056  9580 ?        Ss   Oct27   0:05 /sbin/init
student  12456  1.2  2.3 512300 47200 ?        Sl   19:10   0:12 /usr/bin/gnome-terminal
student  12489  0.3  1.0 305000 21000 pts/0    Ss   19:11   0:02 bash
student  12502  5.6  4.2 175630 86000 pts/0    R+   19:12   0:30 top

Penjelasan per baris:

Baris 1: Proses init dijalankan oleh root, dengan PID 1. Ini adalah proses induk pertama di sistem Linux.

Baris 2: Proses terminal GNOME dijalankan oleh user student. Menggunakan CPU 1.2% dan memori 2.3%.

Baris 3: Shell bash yang aktif di terminal.

Baris 4: Perintah top sedang berjalan, menunjukkan daftar proses real-time.

systemd─┬─NetworkManager───dhclient
        ├─sshd───sshd───bash───top
        ├─gnome-terminal───bash───ps
        └─udisksd

Penjelasan:

systemd adalah proses induk utama dengan PID = 1.
➜ Dialah yang pertama kali dijalankan oleh kernel saat booting.
➜ Semua proses lain merupakan anak (langsung/tidak langsung) dari systemd.

sshd, bash, dan top adalah proses anak dari systemd.

Jika kamu menutup terminal, proses anak seperti bash atau top juga ikut berhenti.

### 3. 

### **4. Hierarki proses dan identifikasi proses induk**

Di Linux, setiap proses memiliki **proses induk (parent process)**, kecuali proses pertama di sistem yaitu **`init` atau `systemd`**.

Kamu dapat melihat **hierarki proses** menggunakan perintah:

``` bash
pstree
```

Contoh output:

```
systemd─┬─NetworkManager───{NetworkManager}
        ├─sshd───bash───pstree
        ├─gnome-shell───Xorg
        └─cron───cronjob.sh
```

## Kesimpulan
kesimpulan proses user
Hubungan antara proses dan user menunjukkan bahwa setiap aktivitas di Linux dijalankan atas nama user tertentu, dengan hak akses yang sesuai. Manajemen proses dan user yang baik sangat penting untuk menjaga stabilitas, efisiensi, dan keamanan sistem operasi Linux.

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
1. whoami

Perintah whoami digunakan untuk memastikan user yang sedang aktif di terminal. Hasilnya menunjukkan bahwa user yang sedang login adalah luthfi.

2. id

Perintah id memberikan informasi detail tentang identitas user seperti UID, GID, dan grup yang diikuti. Hasil menunjukkan user luthfi tergabung dalam beberapa grup penting seperti sudo, adm, dan users, menandakan bahwa user ini memiliki hak administratif.

3. groups

Perintah groups menampilkan daftar grup tempat user luthfi tergabung. Ini menunjukkan hak akses tambahan yang dimiliki user, seperti kemampuan mengakses perangkat (plugdev) dan menjalankan perintah administratif (sudo).

4. sudo adduser praktikan

Perintah adduser digunakan untuk menambahkan user baru bernama praktikan ke sistem. Proses ini juga membuat direktori home dan menetapkan password, menunjukkan cara administrator mengelola user baru.

5. sudo passwd praktikan

Perintah ini berhasil mengubah password user praktikan. Ini menunjukkan pentingnya hak akses sudo dalam pengaturan keamanan akun di Linux.

6. ps aux | head -10

Perintah ini menampilkan daftar 10 proses pertama yang sedang berjalan di sistem, termasuk proses milik root dan layanan sistem seperti systemd. Ini membantu memahami aktivitas sistem dan penggunaan sumber daya.

7. top -n 1

top menampilkan penggunaan CPU, memori, dan daftar proses secara real-time. Hasil menunjukkan sistem dalam keadaan ringan dengan hampir seluruh CPU dalam kondisi idle (99.5%). Perintah ini penting untuk memantau performa sistem.

8. sleep 1000 &

Perintah ini menjalankan proses sleep di background selama 1000 detik. Ini menunjukkan cara menjalankan proses secara paralel tanpa mengganggu terminal utama.

9. ps aux | grep sleep

Perintah ini mencari proses dengan nama sleep dan menampilkan PID-nya. Hasil menunjukkan bahwa proses sleep sedang berjalan dengan PID 600, membuktikan bahwa proses background dapat dilacak menggunakan ps dan grep.

10. kill 600

Perintah kill berhasil menghentikan proses sleep dengan PID 600. Ini menunjukkan cara mengontrol atau mengakhiri proses yang tidak dibutuhkan atau bermasalah.

11. pstree -p | head -20

Perintah pstree menampilkan struktur hierarki proses dalam sistem. Hasil menunjukkan bahwa semua proses berawal dari systemd(1) sebagai proses induk utama, lalu bercabang ke berbagai layanan dan shell user. Ini menggambarkan hubungan antara proses induk dan proses anak di Linux.

---

## **2. Diagram Pohon Hierarki Proses (pstree)**

<img width="1173" height="906" alt="diagram Pohon" src="https://github.com/user-attachments/assets/a8abc6ac-05cf-4bd0-b665-7d589eb34f67" />



## ** 3. Jelaskan hubungan antara user management dan keamanan sistem Linux.**
Manajemen user memiliki peran yang sangat penting dalam menjaga keamanan sistem Linux. Dengan pengaturan user dan grup yang tepat, administrator dapat mengontrol siapa saja yang dapat mengakses sistem serta menentukan hak apa yang dimiliki oleh setiap pengguna. Melalui sistem permission (rwx), kepemilikan file (chown, chgrp), dan pembatasan hak akses root, Linux memastikan bahwa setiap user hanya dapat melakukan tindakan sesuai kewenangannya.Secara keseluruhan, user management dan keamanan sistem Linux saling berkaitan erat — pengelolaan user yang baik akan memperkuat keamanan sistem, sedangkan kelalaian dalam manajemen user dapat membuka celah bagi ancaman keamanan dan penyusupan ke dalam sistem.
 


---


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

Proses dan user merupakan dua komponen utama yang saling berkaitan dalam sistem operasi Linux.Proses adalah satuan kerja yang mewakili program yang sedang berjalan, dikelola langsung oleh kernel untuk memastikan penggunaan sumber daya yang efisien dan stabil.User berperan sebagai identitas yang menentukan hak akses terhadap sistem dan proses yang dijalankan.Setiap proses berjalan atas nama user tertentu, sehingga hak akses dan batasan keamanan sistem dapat dikontrol dengan ketat.Dengan demikian, manajemen proses dan user menjadi dasar dalam menjaga stabilitas, efisiensi, dan keamanan sistem Linux, memastikan bahwa setiap pengguna hanya dapat mengakses dan mengelola sumber daya sesuai kewenangannya.

* Output dari `ps`, `top`, atau `htop` menunjukkan daftar proses yang sedang berjalan beserta penggunaan sumber dayanya.
* Kolom **PID, USER, %CPU, %MEM, COMMAND** penting untuk memahami siapa yang menjalankan proses dan berapa besar sumber daya yang digunakan.
* Dengan `pstree`, kamu bisa melihat **struktur pohon proses**, di mana **`systemd` (PID 1)** adalah induk dari seluruh proses di sistem Linux.




## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  leptop kurang mendukung 
- Bagaimana cara Anda mengatasinya?  meminjam laptop teman

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
