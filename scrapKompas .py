import urllib
from bs4 import BeautifulSoup
import time
from time import sleep
from datetime import date, timedelta

url = "https://indeks.kompas.com/news/"

#ambil hari ini
day = date.today()
filename = "brt-%s.txt" % day
filelink = "link-%s.txt" % day

url += day.strftime("%Y-%m-%d")

def getUrl(url):
    '''ambil url tiap berita di indeks'''
    tautan = []
    url = urllib.request.urlopen(url)

    result = url.read()
    url.close()
    soup = BeautifulSoup(result, "html.parser")

    for link in soup.find_all('h3'):
        for l in link.find_all('a'):
            isi = l.get('href')
            tautan.append(isi)
    return tautan

def getIndeks(url):
    i = 1
    tautans = []
    tautan = getUrl(url)
    while (len(tautan) != 0 and i<2):
        url = "https://indeks.kompas.com/news/%s" %day + "/%d" %i
        print(url)
        i += 1
        tautan = getUrl(url)
        tautans += tautan

    print (len(tautans))
    bf = open(filelink, "w")
    for t in tautans:
        bf.write(t)
        bf.write("\n")
    bf.close()
    

def getBerita(l):
    l = urllib.request.urlopen(l)
    result = l.read()
    l.close()
    isiberita = ""

    soup = BeautifulSoup(result, "html.parser")
    for berita in soup.find_all('div', {'class':'read__content'}):
        isiberita += berita.get_text()
    for berita in soup.find_all('a', {'class':'tag__article__link'}):
        isiberita += berita.get_text() + "-"
    bf = open(filename, 'a')
    bf.write(isiberita)
    bf.write("\n")
    bf.close()

def getLinkFromFile():
    '''Ambil berita dari link yang sudah disimpan di link-tgl.txt'''
    print ("Ambil berita dari link tanggal %s. " % day)
    bf = open(filelink, 'r')
    i = 0
    for l in bf:
        print(l)
        getBerita(l)
    bf.close()

#mainkan
getIndeks(url)
getLinkFromFile()

#Sumber : https://ha.hn.web.id/2016/07/10/belajar-python-scraping-situs/
