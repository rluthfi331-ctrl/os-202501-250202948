# Menggunakan base image Python yang ringan
FROM python:3.9-slim

# Menentukan folder kerja di dalam container
WORKDIR /app

# Menyalin file dari komputer asli ke dalam container.
COPY app.py .

# Menentukan perintah utama saat container dinyalakan.
CMD ["python", "app.py"]