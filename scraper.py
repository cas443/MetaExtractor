from bs4 import BeautifulSoup
import requests
from tkinter import *

url = ""

def scrape_url():

    def goto_start():
        global url
        url = e1.get()
        start()

    global url

    master = Tk()
    master.title("MetaEx: Scrap URL")
    #master.geometry("280x150")
    master.geometry("+{}+{}".format(int(master.winfo_screenwidth()/4 - master.winfo_reqwidth()/4), int(master.winfo_screenheight()/2 - master.winfo_reqheight()/2)))
    Label(master, text="Scrap URL: ").grid(row=0, padx=10, pady=30)

    e1 = Entry(master)
    e1.grid(row=0, column=1)

    url = e1.get()

    print(url)

    b = Button(master, text='Scrape', command=goto_start)
    b.configure(bg="#1ba1e2", fg="#ffffff")
    b.grid(row=3, column=0, sticky="s")


def start():

    global url

    #r = requests.get("http://halsey.wikia.com/wiki/Ghost")
    print("[+] Scraping images from: ", url, "\n")
    #r = requests.get(str(url))
    r = requests.get("https://www.google.com/search?client=ubuntu&channel=fs&q=images&ie=utf-8&oe=utf-8")

    data = r.text

    soup = BeautifulSoup(data, "lxml")



    master = Tk()
    master.title("MetaEx: URL Scraping Results")
    master.configure(background="#ffffff")
    master.pack_propagate(0)
    master.geometry("+{}+{}".format(int(100), int(100)))
    master.resizable(False, False)

    i = 0
    for link in soup.find_all('img'):
        #print("\t", link.get('src'))

        scrapedImageName = "scrapedImage" + str(i) + link.get('src') + "\n" # index of link
        #print(scrapedImageName)

        locals()["panelFrame" + str(i)] = Frame(master, highlightthickness=1, bg="#f333ff")
        locals()["panelFrame" + str(i)].grid(row=0, column=0, padx=10, pady=2+i*2)

        Label(locals()["panelFrame" + str(i)], text=scrapedImageName, font="Verdana 8", fg="#00695C", bg="#ffffff").grid(row=0, column=0, pady=20+i*2)


        i += 1

    left = Frame(master, width=200, height=500, highlightthickness=0, bg="#ffffff")
    left.grid(row=0, column=0, padx=10, pady=2, sticky=N + S)