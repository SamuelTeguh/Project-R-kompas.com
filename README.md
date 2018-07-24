# Project-R-kompas.com

## Project Member
| No | Photo Profile | Member Name | Github ID | Student ID |
| ------ | ------ | ------ | ------ | ------ |
| 1. | <img src="https://avatars.githubusercontent.com/SamuelTeguh" width=100 height=100 /> | Samuel Teguh | <a title="SamuelTeguh" href="https://github.com/SamuelTeguh">@SamuelTeguh</a> | 00000012383 | 
| 2. | <img src="https://avatars.githubusercontent.com/vrGun" width=100 height=100 /> | Veri Gunawan | <a title="vrGun" href="https://github.com/vrGun">@vrGun</a> | 00000012343 | 
| 3. | <img src="https://avatars.githubusercontent.com/yoeladrielcandr" width=100 height=100/> | Yoel Adriel Candra | <a title="yoeladrielcandr" href="https://github.com/yoeladrielcandr">@yoeladrielcandr</a> | 00000014204 |

## Installation

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

<p align="center"><img src="https://github.com/SamuelTeguh/Project-R-kompas.com/blob/master/Image/ss1.png"/></p>

File yang dihasilkan ada 2 file yang berisikan link berita dan isi berita.

<p align="center"><img src="https://github.com/SamuelTeguh/Project-R-kompas.com/blob/master/Image/ss2.png"/></p>
<p align="center"><img src="https://github.com/SamuelTeguh/Project-R-kompas.com/blob/master/Image/ss3.png"/></p>

## Pemodelan

Data yang didapatkan diproses kembali menjadi sebuah corpus text lalu membuang tanda baca, stop words dan angka
yang ada.
Data-data yang sudah diproses lalu dihitung frekuensi kata yang ada dan ditampilkan dalam bentuk grafik.

<p align="center"><img src="https://github.com/SamuelTeguh/Project-R-kompas.com/blob/master/Image/ss4.png"/></p>
