import webbrowser as wb
from bs4 import BeautifulSoup
import requests
import pyperclip

wb.open("http://127.0.0.1:3000/Page/fichier_soumettre.html")
import urllib

post_args = urllib.urlencode(post_params)

url = 'http://www.website.com/'
fp = urllib.urlopen(url, post_args)
soup = BeautifulSoup(fp)
