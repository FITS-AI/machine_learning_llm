# Overview

Proyek ini bertujuan untuk membuat dan melatih model pembelajaran mesin yang dapat menganalisis informasi nutrisi produk dan memberikan penilaian kesehatan atau penyakit berdasarkan data yang ada. Dataset yang dihasilkan berisi prompt teks tentang informasi nutrisi, pertanyaan umum terkait kesehatan, serta pertanyaan yang terkait dengan kondisi penyakit tertentu. Model ini menggunakan pendekatan transfer learning, di mana model T5 yang sudah dilatih sebelumnya digunakan sebagai dasar untuk menyelesaikan tugas analisis nutrisi dan kesehatan.

Proyek ini dibagi menjadi beberapa bagian utama, yaitu pembuatan dataset, preprocessing data, pelatihan model, dan penyimpanan model yang telah dilatih. Setiap bagian berfokus pada pembuatan dataset yang seimbang, pemrosesan data teks, pelatihan model untuk generasi teks, serta penyimpanan hasil pelatihan untuk digunakan di masa depan.

Tujuan akhir proyek ini adalah untuk memiliki model yang dapat secara otomatis menganalisis informasi nutrisi dan memberikan rekomendasi atau penilaian apakah suatu produk sehat atau tidak, serta menjelaskan kondisi penyakit yang terkait.


# Pembuatan Dataset (Creating Dataset)

Bagian ini menjelaskan kode untuk menghasilkan dataset berisi prompt teks dan output analisis nutrisi yang sesuai.

## Poin Utama:
- Mendefinisikan rentang untuk berbagai fakta nutrisi (kalori, lemak, karbohidrat, dll).
- Membuat kondisi penyakit dengan tingkat sensitivitas untuk setiap fakta nutrisi.
- Mendefinisikan template pertanyaan untuk pertanyaan umum dan pertanyaan terkait penyakit.
- Menyediakan template penjelasan untuk output sehat/tidak sehat dan penjelasan penyakit.
- Mengimplementasikan fungsi `generate_product_optimized` untuk membuat data point.
  - Menerima status kesehatan atau penyakit sebagai input (opsional: memaksa kondisi bermasalah).
  - Menghasilkan nilai nutrisi berdasarkan input.
  - Memilih template pertanyaan dan membangun teks input dengan informasi nutrisi.
  - Menentukan teks output berdasarkan kesehatan atau penyakit dan menghasilkan penjelasan.
- Mengimplementasikan fungsi `generate_dataset_optimized` untuk menghasilkan seluruh dataset.
  - Menetapkan jumlah sampel target dan target distribusi terkait penyakit.
  - Melakukan loop untuk menghasilkan jumlah sampel yang diinginkan.
  - Memutuskan secara acak antara sampel umum atau terkait penyakit.
  - Untuk sampel terkait penyakit, memilih penyakit dan mempertimbangkan kebutuhan bermasalah/terkelola.
  - Untuk sampel umum, mempertimbangkan target distribusi sehat/tidak sehat.
  - Membuat DataFrame pandas dari data yang dihasilkan.
  - Mencetak informasi distribusi untuk verifikasi.
  - Menyimpan dataset yang dihasilkan dalam format CSV.

# Preprocessing Data (Data Preprocessing)

Bagian ini menjelaskan kode untuk menyiapkan dataset untuk pelatihan model pembelajaran mesin.

## Poin Utama:
- Memuat file CSV yang berisi dataset ke dalam DataFrame pandas.
- Menginisialisasi tokenizer T5 untuk pemrosesan teks.
- Mendefinisikan fungsi `clean_input` untuk memisahkan pertanyaan dari informasi nutrisi.
- Mengimplementasikan fungsi `preprocess_data` untuk memproses seluruh dataset.
  - Memisahkan pertanyaan dan informasi nutrisi.
  - Membuat input terformat dengan template pertanyaan yang sesuai ("nutrition_analysis" atau "health_assessment").
  - Tokenisasi input dan output menggunakan tokenizer T5 dengan pemangkasan dan padding.
  - Menetapkan label dengan menyalin ID output yang ditokenisasi.
  - Menambahkan fitur "question_type" untuk menunjukkan pertanyaan umum atau terkait penyakit.
  - Menggunakan pustaka Dataset dari Hugging Face untuk mengonversi DataFrame pandas.
  - Menerapkan fungsi `preprocess_data` ke dataset dalam batch.
  - Membagi dataset yang telah diproses menjadi set pelatihan (80%) dan validasi (20%).
  - Mencetak statistik dataset dan contoh data yang telah diproses dengan input dan output yang didekode.

# Pelatihan Model (Transfer Learning) (Model Training)

Bagian ini mencakup kode untuk melatih model menggunakan transfer learning.

## Poin Utama:
- Memuat model T5 yang sudah dilatih sebelumnya untuk generasi teks ("t5-small").
- Mendefinisikan argumen pelatihan menggunakan kelas `TrainingArguments`.
  - Menentukan direktori output, strategi evaluasi, laju pembelajaran, ukuran batch, jumlah epoch, decay bobot, direktori log, dan frekuensi logging.
- Menginisialisasi kelas `Trainer` untuk mengelola proses pelatihan.
  - Memberikan model yang telah dilatih sebelumnya, argumen pelatihan, dataset pelatihan dan validasi, serta tokenizer.
  - Melatih model menggunakan metode `train` dari Trainer.

# Model Disimpan (Saving Model)

Bagian ini menjelaskan cara menyimpan model dan tokenizer yang telah disesuaikan untuk digunakan di masa depan.

## Poin Utama:
- Menyimpan model yang telah dilatih menggunakan metode `save_pretrained` ke direktori yang ditentukan.
- Menyimpan tokenizer menggunakan metode `save_pretrained` ke direktori yang ditentukan.

