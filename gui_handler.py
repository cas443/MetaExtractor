import base, scraper
import os
from tkinter import *
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from tkinter import filedialog

textToSave = ""
location1 = ""

def openFile():
    location = askopenfilename( initialdir="/home/jo/Desktop", title="Select image for metadata extraction", filetypes=(("Image Files", "*.jpg"), ("Image Files", "*.png")) )
    base.start(location)

def saveFile():
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt", initialfile='METAEX_metadata.txt',)
    f.write(textToSave)
    f.close()

def about():
    ABOUT_TEXT = """

    About


    This tool has been created as a summer project. Its intended 
    purpose is to educate as to what type of information is 
    stored within image files.
    
    This software comes with no guarantee. Use at your own risk.    
    """

    top = Toplevel()
    label = Label(top, text=ABOUT_TEXT, heigh=0, width=60)
    label.configure(background="#ffffff")
    label.pack()

def usage():
    USAGE_TEXT = """
    
    OPEN NEW:
    
    Go to File->Open New... and choose the image you want to extract 
    metadata for.

    The data should appear in the "Image Metadata" box in the main 
    window.
    
    
    SAVE CURRENT METADATA TO FILE:
    
    To save the metadata go to File->Save Meta to file... and choose 
    the location and the name you would like to save the data under.
    
    
    SCRAPING:
    
    In order to scrape either:
    a) as soon as the program starts press the "Scrape by Webpage" button or
    b) in the navigation bar go to Scrape> By URL
    
    place the URL you're interested in into the text area and 
    press the "Scrape" button. A new window should appear detailing 
    the image URLs that were found on the URL te user psses in.
    A secondary window should also open to the folder where the 
    images have been downloaded into. 
    
    
    """
    top = Toplevel()
    label = Label(top, text=USAGE_TEXT, heigh=0, width=65)
    label.configure(background="#ffffff")
    label.pack()

def terminology():
    TEXT_WHAT_IT_IS = """
    
                Metadata:
                
                Data that is stored within an image that is the image itself.
                An example would be Exif data which would contain the date and 
                the timestamp of when the image was taken. Other data such as 
                camera make and model, geolocation, how the image was edited as
                well as different tags, copyrights or creators can also be seen
                although their occurance is rarer.
                
                
                Image Scraping:
                
                Scraping is the extraction of data from a source without having 
                direct access to it. In this case the URL (Uniform Resource Locator)
                is provided by the user and all the images that are contained
                on the site pointed at are being downloaded onto users machine.
                
                 

            """

    top = Toplevel()
    label = Label(top, text=TEXT_WHAT_IT_IS, heigh=0, width=65)
    label.configure(background="#ffffff")


    label.pack()

def goto_scrape():
    scraper.scrape_url()

def gui(metadata_ord, metadata_xml, location, filename):
    global location1
    global textToSave

    location1 = location
    textToSave = "" # if a new image is opened then this will allow its metadata to be saved to file as opposed to the previous one

    CMAIN = "#ffffff"  #a5d6a7"
    CLOGO="#00695C"

    master = Tk()
    #master.iconbitmap("/home/jo/Repos/MetaExtractor/favicon.ico")
    master.title("MetaEx: Image Metadata Extraction Tool")
    master.configure(background=CMAIN)
    master.pack_propagate(0)
    master.geometry("+{}+{}".format(int(100), int(100)))
    master.resizable(False, False)


    # ----MENU----
    menubar = Menu(master)
    menubar.configure(background="#ffffff")

    # create a pulldown menu, and add it to the menu bar
    filemenu = Menu(menubar, tearoff=0)
    filemenu.configure(background="#ffffff")
    filemenu.add_command(label="Open New...", command=openFile)
    filemenu.add_command(label="Save Meta to file...", command=saveFile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=master.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    # create more pulldown menus
    editmenu = Menu(menubar, tearoff=0)
    editmenu.configure(background="#ffffff")
    editmenu.add_command(label="By URL", command=goto_scrape)
    menubar.add_cascade(label="Scrape", menu=editmenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.configure(background="#ffffff")
    helpmenu.add_command(label="About", command=about)
    helpmenu.add_command(label="How to use", command=usage)
    helpmenu.add_command(label="Terminology", command=terminology)
    menubar.add_cascade(label="Help", menu=helpmenu)

    # display the menu
    master.config(menu=menubar)

    # ----LEFT----
    left = Frame(master, width=150, height=500, highlightthickness=0, bg=CMAIN)
    left.grid(row=0, column=0, padx=10, pady=2, sticky=N + S)

    logo = Label(left, text="MetaEx", fg=CLOGO, bg=CMAIN, font="Verdana 30 bold", underline=True)
    logo.grid(row=0, column=0, padx=10, pady=30)

    image = Image.open(location)
    image = image.resize((250, 200), Image.ANTIALIAS)
    imageEx = ImageTk.PhotoImage(image, master=master)

    i = Label(left, image=imageEx)
    i.grid(row=1, column=0, padx=40, pady=15)

    extra_information = "Filename: " + filename
    info = Label(left, text=extra_information, font="Verdana 7", bg=CMAIN, fg="#00897B")
    info.grid(row=3, column=0, sticky="nw", padx=40)

    extra_information2 = "Path: " + location[:location.find(filename)]
    info2 = Label(left, text=extra_information2, font="Verdana 7", bg=CMAIN, fg="#00897B")
    info2.grid(row=4, column=0, sticky="nw", padx=40)

    # ----MIDDLE----
    # separator = ttk.Separator(master, orient="vertical")
    # separator.grid(row=0, column=1, sticky="sn", rowspan=2)

    # ----RIGHT----
    right = Frame(master, bg=CMAIN, highlightthickness=0, highlightbackground=CMAIN)
    right.grid(row=0, column=2, padx=0, pady=0)

    intro = Label(right, text="Image Metadata", fg="#ffffff", bg="#1ba1e2", font="Verdana 10 bold", height=2, width=57)
    intro.grid(row=0, column=0, padx=0, pady=20)

    table = Frame(right, bg=CMAIN, highlightthickness=0, highlightbackground=CMAIN)
    table.grid(row=1, column=0, padx=(10, 40), pady=(0, 40), sticky="ns")

    canvas = Canvas(table, width=500, height=350, background=CMAIN, highlightbackground=CMAIN)
    scrolly = Scrollbar(table, orient='vertical', command=canvas.yview)

    i = 0
    for key, value in metadata_xml.items():
        if "0" not in value and "http" not in value:
            l = len(key)
            if l < 9:
                tab = "\t\t\t"
            elif l < 20:
                tab = "\t\t"
            elif l < 30:
                tab = "\t"
            else:
                tab = ""

            myText = key + ": " + tab + value
            label = Label(canvas, text=myText)
            canvas.create_window(0, i * 22, anchor='nw', window=label, height=15)
            label.configure(background=CMAIN)
            textToSave += myText + "\n"
            i += 1

    for j in metadata_ord:
        label = Label(canvas, text=j)
        canvas.create_window(0, i * 22, anchor='nw', window=label, height=15)
        label.configure(background=CMAIN)
        textToSave += j + "\n"
        i += 1


    if "a" not in textToSave or "e" not in textToSave or "i" not in textToSave or "o" not in textToSave or "u" not in textToSave:
        textToSave = "There is no Metadata available for this image."
        label = Label(canvas, text=textToSave)
        canvas.create_window(0, 22, anchor='nw', window=label, height=15)
        label.configure(background=CMAIN)

    canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scrolly.set, background=CMAIN)
    # canvas.config(width=600, height=440)
    canvas.pack(fill='both', expand=True, side='left')
    scrolly.configure(bg="#ffffff")
    scrolly.pack(fill='y', side='right')

    master.mainloop()
