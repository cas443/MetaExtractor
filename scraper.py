from bs4 import BeautifulSoup
import requests
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
    r = requests.get(str(url))
    data = r.text
    soup = BeautifulSoup(data, "lxml")

    print("[+] Scraping images from: ", url, "\n")

    i = 0
    for link in soup.find_all('img'):

        print(link)

        scrapedImagesList += link.get('src') + "\n"
        filename = datetime.datetime.today().strftime('%d%m%Y') + "_" + str(i) + ".jpg"

        try:
            with open(os.path.join("/home/jo/Desktop/ScrapedImages", filename), "wb") as f:
                f.write(requests.get(link.get('src')).content)
        except:
            print("[ERR] The url scraped may not be a proper url but an extenrion to the address provided...") # wording might not be clear enough
            pass
        i+=1


    master = Tk()
    master.title("MataEx")

    extractionOutputFrame = Frame(master, bg="#ffffff")
    extractionOutputFrame.grid(row=0, column=0)

    ot = "Images extracted from: " + url[:30]
    originText = Label(extractionOutputFrame, text=ot, bg="#ffffff")
    originText.grid(row=1, column=0, pady=(5,5))

    if os.path.exists("/home/jo/Desktop/ScrapedImages"):
        directoryPath =  "/home/jo/Desktop/ScrapedImages"
    else:
        os.makedirs("/home/jo/Desktop/ScrapedImages")
        directoryPath = "/home/jo/Desktop/ScrapedImages"

    sl = "Following images have been saved at: " + directoryPath
    savedLocation = Label(extractionOutputFrame, text=sl, bg="#ffffff")
    savedLocation.grid(row=2, column=0, pady=(5,3))

    outputData = Label(extractionOutputFrame, text=scrapedImagesList, cursor="hand2", bg="#ffffff", font="Verdana 5")
    outputData.grid(row=3, column=0, padx=(2,0), pady=(5,2))

    try:
        webbrowser.open("/home/jo/Desktop/ScrapedImages", 2)
    except:
        pass