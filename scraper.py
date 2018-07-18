from bs4 import BeautifulSoup
import requests
from tkinter import *

url = ""

def scrape_url():

    global url

    master = Tk()
    Label(master, text="Scrap URL: ").grid(row=0)

    e1 = Entry(master)
    e1.grid(row=0, column=1)

    url = str(e1)

    b = Button(master, text='Scrape', command=start)
    b.configure(bg="#1ba1e2", fg="#ffffff")


    b.grid(row=3, column=0, sticky="w", pady=4, padx=3)



def start():

    global url

    r = requests.get("http://halsey.wikia.com/wiki/Ghost")

    data = r.text

    soup = BeautifulSoup(data, "lxml")

    for link in soup.find_all('img'):
        print(link.get('src'))