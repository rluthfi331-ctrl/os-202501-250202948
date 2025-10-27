
# Laporan Praktikum Minggu 3
Topik: [linux fs permission]

---

## Identitas
- **Nama**  : [LUTHFI AULIA RAHMAN]  
- **NIM**   : [250202948]
- **Kelas** : [1 IKRB]

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menggunakan perintah `ls`, `pwd`, `cd`, `cat` untuk navigasi file dan direktori.
2. Menggunakan `chmod` dan `chown` untuk manajemen hak akses file.
3. Menjelaskan hasil output dari perintah Linux dasar.
4. Menyusun laporan praktikum dengan struktur yang benar.
5. Mengunggah dokumentasi hasil ke Git Repository tepat waktu.

  1. Menggunakan perintah ls, pwd, cd, cat untuk navigasi file dan direktori
Perintah	Fungsi	Contoh	Penjelasan hasil output
pwd	Menampilkan direktori kerja saat ini (Print Working Directory).	$ pwd → /home/student	Menunjukkan lokasi direktori aktif saat ini di sistem file.
ls	Menampilkan isi direktori.	$ ls → Documents Downloads file.txt	Menampilkan daftar file dan folder di direktori aktif.
ls -a	Menampilkan semua isi direktori termasuk file tersembunyi (diawali dengan titik).	$ ls -a → . .. .bashrc Documents file.txt	Menunjukkan bahwa ada file konfigurasi tersembunyi seperti .bashrc.
cd	Berpindah direktori (Change Directory).	$ cd Documents	Masuk ke direktori Documents.
cat	Menampilkan isi file teks ke layar (Concatenate).	$ cat file.txt	Menampilkan seluruh isi dari file.txt.
2. Menggunakan chmod dan chown untuk manajemen hak akses file
Perintah	Fungsi	Contoh	Penjelasan hasil output
chmod	Mengubah izin akses file (read, write, execute).	$ chmod 755 script.sh	Memberi izin penuh (rwx) untuk pemilik, dan izin baca–eksekusi (r-x) untuk grup dan lainnya.
chown	Mengubah kepemilikan file/direktori.	$ sudo chown user1:user1 file.txt	Mengubah pemilik dan grup dari file.txt menjadi user1.

Makna permission contoh rwxr-xr--:

r (read) = izin membaca file

w (write) = izin menulis/mengubah file

x (execute) = izin menjalankan file

Format:

3 huruf pertama: hak akses pemilik

3 huruf tengah: hak akses grup

3 huruf terakhir: hak akses lainnya
Contoh:

rwxr-xr-- → pemilik bisa baca/tulis/jalankan, grup hanya baca/jalankan, lainnya hanya baca.

3. Menjelaskan hasil output dari perintah Linux dasar

Setelah menjalankan semua perintah di atas:

pwd menunjukkan posisi kita di sistem file (membantu navigasi).

ls dan ls -a membantu mengenali struktur direktori serta file tersembunyi.

cd memudahkan berpindah antar folder.

cat memungkinkan membaca isi file langsung dari terminal.

chmod dan chown memastikan keamanan file dengan mengontrol siapa yang dapat membaca, mengubah, atau menjalankan file tersebut.

4. Menyusun laporan praktikum dengan struktur yang benar

Contoh struktur laporan_praktikum.md:

# LAPORAN PRAKTIKUM SISTEM OPERASI

## 1. Tujuan
- Memahami penggunaan perintah dasar Linux untuk navigasi dan manajemen hak akses.

## 2. Alat dan Bahan
- OS: Linux Ubuntu
- Terminal/CLI
- GitHub Repository

## 3. Langkah Percobaan
1. Menjalankan `pwd`, `ls`, `ls -a`, `cd`, `cat`.
2. Mengubah izin file dengan `chmod`.
3. Mengubah pemilik file dengan `chown`.

## 4. Hasil dan Analisis
| Perintah | Output | Analisis |
|-----------|---------|----------|
| pwd | /home/student | Menunjukkan direktori aktif |
| ls -a | . .. .bashrc file.txt | Menampilkan file tersembunyi |
| chmod 755 file.sh | (tidak ada output) | Mengubah permission file |
| chown user1 file.txt | (tidak ada output) | Mengubah pemilik file |

## 5. Kesimpulan
Perintah dasar Linux membantu navigasi file dan pengelolaan hak akses, yang penting untuk keamanan sistem.

## 6. Dokumentasi
(Sertakan screenshot hasil terminal)

5. Mengunggah dokumentasi hasil ke Git Repository tepat waktu

Langkah-langkah:

# Inisialisasi Git (jika belum)
git init

# Tambahkan semua file hasil praktikum
git add .

# Commit perubahan
git commit -m "Menambahkan laporan praktikum Linux dasar"

# Tambahkan remote repository (ganti URL sesuai repo Anda)
git remote add origin https://github.com/username/nama-repo.git

# Push ke GitHub
git push -u origin main



---

## Dasar Teori
Model Kepemilikan (Ownership Model)
Setiap file dan direktori di Linux dimiliki oleh user (pemilik) dan group (kelompok), serta dapat diakses oleh others (pengguna lain) di sistem.

Tiga Jenis Hak Akses (Permissions Types)
Linux menggunakan tiga jenis izin utama: r (read): membaca isi file atau daftar direktori. w (write): mengubah atau menghapus isi file/direktori.

Representasi Simbolik dan Numerik
Hak akses dapat ditampilkan dalam bentuk simbolik (rwxr-xr--) atau numerik (contoh: 755), di mana setiap angka mewakili kombinasi izin (r=4, w=2, x=1).

Perintah Pengaturan Akses (chmod, chown, chgrp)
chmod untuk mengubah izin file dan chown untuk mengubah pemilik file.

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
   - Pastikan folder kerja berada di dalam direktori repositori Git praktikum:
     ```
     praktikum/week3-linux-fs-permission/
     ```

2. **Eksperimen 1 – Navigasi Sistem File**
   Jalankan perintah berikut:
   ```bash
   pwd
   ls -l
   cd /tmp
   ls -a
   ```
   - Jelaskan hasil tiap perintah.
   - Catat direktori aktif, isi folder, dan file tersembunyi (jika ada).

3. **Eksperimen 2 – Membaca File**
   Jalankan perintah:
   ```bash
   cat /etc/passwd | head -n 5
   ```
   - Jelaskan isi file dan struktur barisnya (user, UID, GID, home, shell).

4. **Eksperimen 3 – Permission & Ownership**
   Buat file baru:
   ```bash
   echo "Hello <NAME><NIM>" > percobaan.txt
   ls -l percobaan.txt
   chmod 600 percobaan.txt
   ls -l percobaan.txt
   ```
   - Analisis perbedaan sebelum dan sesudah chmod.  
   - Ubah pemilik file (jika memiliki izin sudo):
   ```bash
   sudo chown root percobaan.txt
   ls -l percobaan.txt
   ```
   - Catat hasilnya.

5. **Eksperimen 4 – Dokumentasi**
   - Ambil screenshot hasil terminal dan simpan di:
     ```
     praktikum/week3-linux-fs-permission/screenshots/
     ```
   - Tambahkan analisis hasil pada `laporan.md`.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 3 - Linux File System & Permission"
   git push origin main
   ```


---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![alt text](<Screenshot 2025-10-23 092015.png>)

---

## Analisis

2. Jelaskan hasil tiap perintah.
   - Catat direktori aktif, isi folder, dan file tersembunyi (jika ada).
3. Jelaskan isi file dan struktur barisnya (user, UID, GID, home, shell)
4. Analisis perbedaan sebelum dan sesudah chmod.
Ubah pemilik file (jika memiliki izin sudo)

 2. Catat direktori aktif, isi folder, dan file tersembunyi (jika ada)

Gunakan perintah berikut:

pwd
ls -la


Penjelasan:

pwd → (print working directory) menampilkan direktori kerja saat ini.
Contoh hasil:

/home/lutfi/Documents/linux_praktikum


→ Artinya kamu sedang berada di folder linux_praktikum dalam direktori Documents.

ls -la → menampilkan seluruh isi folder, termasuk file tersembunyi (yang diawali dengan titik .).
Contoh hasil:

drwxr-xr-x 2 lutfi lutfi 4096 Oct 24 09:30 .
drwxr-xr-x 4 lutfi lutfi 4096 Oct 24 09:00 ..
-rw-r--r-- 1 lutfi lutfi  120 Oct 24 09:10 data.txt
-rw-r--r-- 1 lutfi lutfi  200 Oct 24 09:12 .hidden_config


→ File tersembunyi di atas adalah .hidden_config (karena diawali titik).

3. Jelaskan isi file dan struktur barisnya

Jika kamu membuka file seperti /etc/passwd, gunakan:

cat /etc/passwd


Contoh potongan hasil:

root:x:0:0:root:/root:/bin/bash
lutfi:x:1000:1000:Lutfi:/home/lutfi:/bin/bash


Struktur tiap baris /etc/passwd:

user : password : UID : GID : description : home_directory : shell


Penjelasan tiap kolom:

Kolom	Nama	Arti
1	user	Nama akun pengguna (contoh: lutfi)
2	password	Biasanya berisi x, artinya password disimpan di file /etc/shadow
3	UID	User ID unik (0 = root, 1000+ = user biasa)
4	GID	Group ID utama pengguna
5	description	Keterangan pengguna (opsional)
6	home_directory	Lokasi direktori utama user (/home/lutfi)
7	shell	Shell yang digunakan (/bin/bash, /bin/sh, dll)
4. Analisis perbedaan sebelum dan sesudah chmod

Gunakan:

ls -l nama_file
chmod 744 nama_file
ls -l nama_file


Contoh hasil:
Sebelum:

-rw-r--r-- 1 lutfi lutfi 200 Oct 24 09:10 data.txt


Sesudah:

-rwxr--r-- 1 lutfi lutfi 200 Oct 24 09:10 data.txt


Analisis perubahan:

Bagian	Sebelum (rw-r--r--)	Sesudah (rwxr--r--)	Penjelasan
Owner	rw- (read, write)	rwx (read, write, execute)	Pemilik file kini bisa menjalankan file
Group	r--	r--	Tidak berubah (hanya bisa membaca)
Others	r--	r--	Tidak berubah (hanya bisa membaca)

🔹 Kesimpulan: chmod 744 memberi izin eksekusi pada pemilik file, sementara user lain tetap hanya bisa membaca.
Perubahan permission ini meningkatkan fleksibilitas pemilik, namun tetap menjaga keamanan terhadap user lain.

5. Ubah pemilik file (jika memiliki izin sudo)

Gunakan:

sudo chown root data.txt


Cek hasil:

ls -l data.txt


Sebelum:

-rwxr--r-- 1 lutfi lutfi 200 Oct 24 09:10 data.txt


Sesudah:

-rwxr--r-- 1 root lutfi 200 Oct 24 09:10 data.txt


Analisis:

Pemilik (owner) berubah dari lutfi → root

Group tetap lutfi

Artinya hanya root yang kini memiliki kontrol penuh atas file tersebut.

🔹 Implikasi keamanan:
Mengubah kepemilikan file ke root membatasi akses modifikasi bagi user biasa, mencegah perubahan tidak sah — berguna untuk file konfigurasi penting.
---

## Kesimpulan


1. inux FS Permission merupakan mekanisme dasar keamanan yang mengatur siapa yang boleh membaca, menulis, dan mengeksekusi file atau direktori, sehingga menjaga kerahasiaan dan integritas sistem.

2. Sistem izin berbasis user, group, dan others memastikan setiap file memiliki kontrol akses yang jelas dan terstruktur.

3. Pengelolaan izin melalui perintah seperti chmod dan chown memberi administrator fleksibilitas untuk menyesuaikan hak akses sesuai kebutuhan keamanan dan fungsi sistem.

## Tugas

1. Dokumentasikan hasil seluruh perintah pada tabel observasi di `laporan.md`.  
2. Jelaskan fungsi tiap perintah dan arti kolom permission (`rwxr-xr--`).  
3. Analisis peran `chmod` dan `chown` dalam keamanan sistem Linux
4. Upload hasil dan laporan ke repositori Git sebelum deadlien

1. | No | Perintah                    | Output (Hasil di Terminal)                                 | Penjelasan Singkat                                                                          |
| -- | --------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| 1  | `pwd`                       | `/home/student`                                            | Menampilkan direktori aktif saat ini.                                                       |
| 2  | `ls -a`                     | `.  ..  file1.txt  .hidden  Documents`                     | Menampilkan isi direktori termasuk file tersembunyi (`.` dan `..` adalah direktori khusus). |
| 3  | `cat /etc/passwd`           | `root:x:0:0:root:/root:/bin/bash`                          | Menampilkan isi file `passwd` yang berisi informasi user (username, UID, GID, home, shell). |
| 4  | `chmod 744 file1.txt`       | (tidak ada output)                                         | Mengubah hak akses file menjadi `rwxr--r--`.                                                |
| 5  | `ls -l file1.txt`           | `-rwxr--r-- 1 student student 1024 Oct 24 10:00 file1.txt` | Menampilkan detail file dan permission-nya.                                                 |
| 6  | `sudo chown root file1.txt` | (tidak ada output)                                         | Mengubah pemilik file menjadi `root`.                                                       |
| 7  | `ls -l file1.txt`           | `-rwxr--r-- 1 root student 1024 Oct 24 10:00 file1.txt`    | Terlihat perubahan pemilik file.                                                            |

2. Fungsi tiap perintah & arti kolom permission rwxr-xr--
Fungsi perintah:

pwd – Menampilkan direktori kerja (working directory) saat ini.

ls – Menampilkan isi direktori. Opsi -a menampilkan file tersembunyi.

cat – Menampilkan isi file teks secara langsung ke terminal.

chmod – Mengubah izin akses (permission) file atau direktori.

chown – Mengubah pemilik (owner) dan/atau grup dari file atau direktori.

| Bagian | Subjek           | Izin                 | Arti                                                           |
| ------ | ---------------- | -------------------- | -------------------------------------------------------------- |
| `rwx`  | Owner (pemilik)  | read, write, execute | Pemilik bisa membaca, menulis, dan menjalankan file.           |
| `r-x`  | Group (grup)     | read, execute        | Anggota grup bisa membaca dan menjalankan, tapi tidak menulis. |
| `r--`  | Others (lainnya) | read                 | Pengguna lain hanya bisa membaca.                              |

3. Analisis peran chmod dan chown dalam keamanan sistem Linux
a. Peran chmod (Change Mode)

Mengatur siapa yang dapat membaca (r), menulis (w), dan menjalankan (x) suatu file/direktori.

Menjadi lapisan kontrol akses pertama agar file sistem penting tidak bisa diubah oleh pengguna tak berwenang.

Contoh: File konfigurasi /etc/passwd hanya bisa dibaca oleh user biasa (r--r--r--) dan hanya bisa dimodifikasi oleh root.

Jika permission terlalu longgar (misalnya 777), maka siapa pun bisa memodifikasi file → berpotensi membuka celah keamanan.

b. Peran chown (Change Owner)

Mengatur siapa yang memiliki kontrol penuh terhadap file.

Pemilik file bisa menentukan hak akses menggunakan chmod.

Hanya user root yang bisa mengubah kepemilikan → mencegah user biasa mengambil alih file orang lain.

Sangat penting dalam multi-user system, agar tiap user hanya bisa mengakses file miliknya sendiri.

c. Kesimpulan

Kedua perintah ini merupakan bagian penting dari keamanan berbasis akses (Access Control) di Linux.

chmod menjaga tingkat akses (apa yang bisa dilakukan).

chown menjaga kepemilikan (siapa yang boleh mengatur).
Bersama-sama, keduanya memastikan integritas dan kerahasiaan data di lingkungan sistem operasi Linux.

Apakah kamu ingin saya bant

## Quiz

1. Apa fungsi dari perintah chmod?

   chmod (change mode) digunakan di sistem operasi Linux/Unix untuk mengubah hak akses (permission) suatu file atau direktori.
Dengan chmod, kita dapat menentukan siapa saja yang boleh membaca (read), menulis (write), atau mengeksekusi (execute) file atau folder tersebut.
2.  Apa arti dari kode permission rwxr-xr--?

   | Bagian | Siapa      | Kode  | Arti                 |
| ------ | ---------- | ----- | -------------------- |
| 1–3    | **Owner**  | `rwx` | read, write, execute |
| 4–6    | **Group**  | `r-x` | read, execute        |
| 7–9    | **Others** | `r--` | read only            |

3. Jelaskan perbedaan antara chown dan chmod.
   
| Perintah    | Fungsi Utama                                                        | Contoh                        | Keterangan                                     |
| ----------- | ------------------------------------------------------------------- | ----------------------------- | ---------------------------------------------- |
| **`chmod`** | Mengubah **izin akses (permission)** file atau direktori            | `chmod 755 file.txt`          | Mengatur siapa yang boleh read/write/execute   |
| **`chown`** | Mengubah **kepemilikan (owner dan/atau group)** file atau direktori | `chown user1:group1 file.txt` | Mengganti pemilik atau grup dari file tersebut |

---

## Refleksi Diri
- bagian yang menantang mungkin adalah memahami dan mengimplementasikan izin akses yang tepat menggunakan perintah chmod dan chown karena memerlukan pemahaman mendalam tentang konsep permission dan implikasinya.    

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
