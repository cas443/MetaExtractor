from bs4 import BeautifulSoup
import requests
import urllib.request
import datetime
import os
import webbrowser
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

    master.mainloop()


def start():

    global url

    scrapedImagesList = ""

    print("[+] Scraping images from: ", url, "\n")
    r = requests.get(str(url))
    #r = requests.get("https://www.google.com/search?client=ubuntu&channel=fs&q=images&ie=utf-8&oe=utf-8")

    data = r.text

    soup = BeautifulSoup(data, "lxml")

    #print(soup)

    # masterScraper = Tk()
    # masterScraper.title("MetaEx: URL Scraping Results")
    # masterScraper.configure(background="#ffffff")
    # masterScraper.pack_propagate(0)
    # masterScraper.geometry("+{}+{}".format(int(100), int(100)))
    # masterScraper.resizable(False, False)

    # mainFrame = Frame(masterScraper).grid(row=0, column=0)

    i = 0
    for link in soup.find_all('img'):

        print(link)

        scrapedImagesList += link.get('src') + "\n"
        scrapedImageName = "scrapedImage " + str(i) + ": "+ link.get('src') # index of link
        #print(scrapedImageName)

        #try:
        # imageName = re.search(r"(?:.*/)(.*)(?=)", scrapedImageName).group(1)
        # urllib.request.retrieve(scrapedImageName, imageName)
        #except:
            #print("[ERR] The url scraped may not be a proper url but an extenrion to the address provided...")

        filename = datetime.datetime.today().strftime('%d%m%Y') + "_" + str(i) + ".jpg"
        with open(os.path.join("/home/jo/Desktop/ScrapedImages", filename), "wb") as f:
            f.write(requests.get(link.get('src')).content)
        i+=1


    master = Tk()

    extractionOutputFrame = Frame(master, bg="#ffffff")
    extractionOutputFrame.grid(row=0, column=0)

    ot = "Images extracted from: " + url[:30]
    originText = Label(extractionOutputFrame, text=ot, bg="#ffffff")
    originText.grid(row=1, column=0, pady=(5,5))

    sl = "Following images have been saved at: " + "/home/jo/Desktop/ScrapedImages"
    savedLocation = Label(extractionOutputFrame, text=sl, bg="#ffffff")
    savedLocation.grid(row=2, column=0, pady=(5,3))

    outputData = Label(extractionOutputFrame, text=scrapedImagesList, cursor="hand2", bg="#ffffff", font="Verdana 5")
    outputData.grid(row=3, column=0, padx=(2,0), pady=(5,2))

    try:
        webbrowser.open("/home/jo/Desktop/ScrapedImages", 2)
    except:
        pass











    #     locals()["panelFrame" + str(i)] = Frame(mainFrame, highlightthickness=1, bg="#f33fff").grid(row=i, column=0, padx=10, pady=10)
    #
    #     Label(locals()["panelFrame" + str(i)], text=scrapedImageName, font="Verdana 8", fg="#00695C", bg="#ffffff").grid(row=0, column=0, pady=10)
    #
    #
    #     i += 1
    #
    # left = Frame(masterScraper, width=200, height=500, highlightthickness=0, bg="#ffffff")
    # left.grid(row=0, column=0, padx=10, pady=2, sticky=N + S)

    #masterScraper.mainloop()