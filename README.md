# Project-R-kompas.com

## Instalasi

1. Clone repositori ini
2. Install Python3
3. Install Beautiful Soup4 lib untuk Python
4. Buka R studio dan file R dari direktori
5. Install package yang dibutuhkan
   - `shiny`, `qdap`, `tm`, `stopwords`
   
## Flowchart

<p align="center"><img src="https://github.com/SamuelTeguh/Project-R-kompas.com/blob/master/Image/workflow.jpg"/></p>

## Web Scraping

Pada projek ini dilakukan scraping menggunakan python, dikarenakan kompas.com tidak menyediakan API.
Pada code python tersebut, digunakan library Beautiful Soup untuk parsing dokumen html dan xml.
Program ini berfungsi untuk mendapatkan data berita hari ini di indeks.kompas.com.

Fungsi getUrl() untuk mengambil url semua berita yang ada di indeks.kompas.com/news

Fungsi getIndeks() untuk membuat link yang diambil menjadi dynamic sehingga bisa mengambil berita di indeks.kompas.com/news di semua pages dan menulisnya dalam sebuah file .txt

Fungsi getBerita() untuk mengambil isi berita dari setiap link. Menggunakan teknik filtering menggunakan bs4 menggunakan metode find_all menggunakan attribute tag html :
  - for berita in soup.find_all('div', {'class':'read__content'}):

Fungsi getLinkFromFile() untuk mengambil link dari file .txt yang dihasilkan sebelumnya.

<p align="center"><img src="https://github.com/SamuelTeguh/Project-R-kompas.com/blob/master/Image/ss1.png"/></p>

File yang dihasilkan ada 2 file yang berisikan link berita dan isi berita.

<p align="center"><img src="https://github.com/SamuelTeguh/Project-R-kompas.com/blob/master/Image/ss2.png"/></p>
<p align="center"><img src="https://github.com/SamuelTeguh/Project-R-kompas.com/blob/master/Image/ss3.png"/></p>

## Pemodelan

Data yang didapatkan diproses kembali menjadi sebuah corpus text :
  -  news_corpus <- createCorpus("brt-2018-07-24.txt")
Corpus text lalu dibuang tanda baca, stop words dan angkanya menggunakan package tm, fungsi tm_map. tm_map adalah
interface untuk menerapkan fungsi transformasi ke corpus text.
Data-data yang sudah diproses lalu dihitung frekuensi katanya menggunakan package stopwords.
Package stopwords, menyediakan fungsi stopword() yang mereturn kata-kata stopwords dalam bentuk vectors untuk beberapa bahasa yang berbeda, menggunakan code bahasa ISO-639-1 dan menyediakan sources yang lain untuk stopwords yang belum dinyatakan. 
Hasilnya di sort dan dihitung frekuensi katanya menggunakan package qdap. Menggunakan fungsi freq_terms() untuk menghitung frekuensi kata pada suatu text vector yang mereturn frenkuensi kata dalam bentuk dataframe. 
- Proses :
  1. Membaca file csv yang berisikan stopwords bahasa Indonesia
  - stopwords <- read.csv("word.csv", header = FALSE)
  - stopwords <- as.character(stopwords$V1)
  - stopwords <- c(stopwords, stopwords()
  2. Memproses data dengan menghilangkan angka dan tanda baca serta membuat data menjadi lowercase semua
  - news_corpus_proc <- tm_map(news_corpus, content_transformer(tolower))
  - news_corpus_proc <- tm_map(news_corpus_proc, removePunctuation)
  - news_corpus_proc <- tm_map(news_corpus_proc, removeNumbers)
  3. Membuang semua stopwords yang ada didata, sesuai dengan data stopword pada file csv diatas.
  - news_corpus_proc <- tm_map(news_corpus_proc, removeWords, stopwords)
  4. Mengelompokan data yang didapatkan dan menghitung frekuensi kata
  - frequent_terms <- freq_terms(news_corpus_proc, input$wordNum)

<p align="center"><img src="https://github.com/SamuelTeguh/Project-R-kompas.com/blob/7ffc0fa16da4abd8e163674330c08306e832d8b3/Image/ss4.png"/></p>

## Referensi
  - https://ha.hn.web.id/2016/07/10/belajar-python-scraping-situs/
  - https://github.com/stopwords-iso/stopwords-id/blob/master/raw/indonesian-stopwords-complete.txt

## Disklaimer
Data yang berasal dari kompas.com hanya digunakan untuk membuat project kelas Frontier Technology, Universitas Pelita Harapan.

Project ini dibuat oleh :
  - Samuel Teguh / 00000012383
  - Veri Gunawan / 00000012343
  - Yoel Adriel Candra / 00000014204
