"""
!/usr/bin/env python3
__AUTHOR = "JIMOH IDRIS OLANSHILE"
__DATE = "DEC 2019 - till date."
"""
#TODO add connection page for jshare 3.0
import time, os as gd, subprocess as sp
from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from PIL import ImageTk
port = "4202"
line = "-" * 70
Pth = gd.path.join ("C:\\", "My Files - Important", "virtualenvironment", "J_Hack_Share", "Xendit", "Include", "Images\\")
def abtF ():
    abtP = Tk()
    abtP.title("Xendit@About-Us")
    abtP.geometry("610x350+340+200")
    titLab = Label (abtP, text = "About Us", font = ("times new roman", 15, "bold")).place (x=0,y=15,relwidth=1)
    aboutUs = "Xendit Software is yet another file sharing app with a ridiculously fast transfer fee.\nThis project was written and is still managed by Jimoh Idris Olanshile, a computer programmer and a security & privacy advocate.\n\nXendit was designed to make file sharing from an Android Device to a PC seemless and lightning fast.\nHowever, in order enjoy this full fledged advance software with its incredivly fast algorithm, developer's options and USB debugging has to be enabled.\n\nBegin to use Xendit now to start transfer files between your device and PC for free.\nCONTACT US:\nEmail: xendit@telon.com\nMobile Number: +233203450788\n"
    txt = Text(abtP, width = 70, height = 17, wrap = WORD)
    txt.insert(INSERT, aboutUs)
    txt.place(x=22, y=60)
    abtP.mainloop()
    
def howtF ():
    howtP = Tk()
    howtP.title("Xendit@How-To")
    howtP.geometry("610x350+340+200")
    titLab = Label (howtP, text = "How to iDER", font = ("times new roman", 15, "bold")).place (x=0,y=15,relwidth=1)
    howText = """Hey, I heard you needed my help. This how-to should be simple and straightforward.\n\n1. Find Developer's Options on the device and Enable USB debugging.\nPS: If you can't find Developer's Options simply go to "About Phone" and Tap the text "Build Number" 3 times to enable it.\n\n2. Connect the PC to your phone's Hotspot or just make sure they're both on the same network to transfer wirelessly.\n\n3. Visit www.TeLon.com/xendit/Download to register and download xendit file sharer.\n\n4. Fire up and Login with your credentials.\n\n5. Attach your device with a USB cord and detach it once you've connected to the PC and enjoy sharing."""
    txt = Text(howtP, width = 70, height = 15, wrap = WORD)
    txt.insert(INSERT, howText)
    txt.place(x=25, y=60)
    howtP.mainloop()

def dontF ():
    line = "-" * 70
    dontP = Tk()
    dontP.title("Xendit@Assist-us")
    dontP.geometry("610x350+340+200")
    titLdon = Label (dontP, text = "Assist The Programmer", font = ("times new roman", 15, "bold")).place (x=0,y=25,relwidth=1)
    donText = "I truly appreciate your interest to make a donation as your donation would go a long way in the developnment and the continual improvement of TeLon no matter how little it may be, Thank you in advance.\n\n\n" + line + "\nBank Name: GtBank\nAccount Name: Jimoh Idris Olanshile\nAccount Number: 0202884092\nPhone Number: +2348159344489"
    txt = Text(dontP, width = 70, height = 10, wrap = WORD)
    txt.insert(INSERT, donText)
    txt.place(x=25, y=80)
    dontP.mainloop()
def clr (tt = 0): #create a simple function to clear the terminal; in tt seconds, default is 0; No delay
    gd.system ("cls")

def jsConn():
    def jsMainActivity():
        #create function to create needed dirs
        def mkdirs():
            serialN = devID.get()
            if serialN == "":
                mb.showerror ("Error", "Provide the serial number to continue")
            else:
                try:
                    #create needed dirs for the PC
                    gd.mkdir ("C:/Xendit")
                    gd.mkdir ("C:/Xendit/Others")
                    gd.mkdir ("C:/Xendit/Videos")
                    gd.mkdir ("C:/Xendit/Images")
                    gd.mkdir ("C:/Xendit/Musics")
                    gd.mkdir ("C:/Xendit/App")
                    #create needed dirs for the android device
                    gd.system ("zaglarh -s " + serialN + " shell mkdir sdcard/Xendit/")
                    gd.system ("zaglarh -s " + serialN + " shell mkdir sdcard/Xendit/Others")
                    gd.system ("zaglarh -s " + serialN + " shell mkdir sdcard/Xendit/Videos")
                    gd.system ("zaglarh -s " + serialN + " shell mkdir sdcard/Xendit/Images")
                    gd.system ("zaglarh -s " + serialN + " shell mkdir sdcard/Xendit/Musics")
                    gd.system ("zaglarh -s " + serialN + " shell mkdir sdcard/Xendit/Apps")
                except FileExistsError:
                    mb.showinfo ("Error", "Folder Already Exist")

        def seActivity():
            serialN = devID.get()
            if serialN == "":
                mb.showerror ("Error", "Provide the serial number to continue")
            else:
                seFile = fd.askopenfilenames (title = "Choose file(s) to send")
                seLoc = "/Others" #default storage location
                for i in seFile:
                    i2 = i.rpartition (".")
                    iF = i2 [2]
                    if iF == "mp4" or iF == "mkv" or iF == "3gp":
                        seLoc = "/Videos"
                    elif iF == "jpg" or iF == "png" or iF == "jpeg":
                        seLoc = "/Images"
                    elif iF == "apk":
                        seLoc = "/Apps"
                    elif iF == "mp3":
                        seLoc = "/Musics"
                    else:
                        seLoc = "/OtherS"
                    sp.check_output ("zaglarh -s " + serialN + " push " + "\"" + i + "\"" + " /sdcard/Xendit" + seLoc)
                    mb.showinfo ("Success", "Sent to " + "/sdcard/Xendit" + seLoc)
                #mb.showinfo ("Success", "This works" + " " + dID)

        def puActivity():
            def pullF():
                pLoc = puL.get()
                print (pLoc)
                saveL = fd.askdirectory(title = "Choose download folder")
                try:
                    pOut = sp.check_output ("zaglarh -s " + serialN + " pull " + "\"" + pLoc + "\"" + " " + "\"" + saveL + "\"")
                    pOut2 = str(pOut).rpartition ("(")
                    pOut3 = pOut2 [0]
                    pOut4 = pOut3.rpartition ("'")
                    pOut = pOut4 [2]
                    mb.showinfo ("Success", pOut)
                except sp.CalledProcessError:
                    mb.showerror ("Error", "An error occurred.")
            serialN = devID.get()
            if serialN == "":
                mb.showerror ("Error", "Provide the serial number to continue.")
            else:
                jsMain.destroy()
                puFWin = Tk()
                puFWin.geometry("280x130+540+310")#w*h+x+y
                puL = StringVar()
                puLab = Label (puFWin, text = "File to pull", font = ("times new roman", 12, "bold")).place (x=0,y=20,relwidth=1)
                puEntry = Entry (puFWin, width =30, textvariable = puL, bg = "WHITE", bd = 5).place (x=45, y = 60)
                puconfB = Button (puFWin, command = pullF, text = "Launch", bg = "Red", fg = "WHITE").place (x=115, y=95)
                puFWin.mainloop()

        jsMain = Tk()
        ########create app menu
        menubar = Menu(jsMain)
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Send", command=seActivity)
        filemenu.add_command(label="Pull", command=puActivity)
        filemenu.add_command(label="Folder Setup", command=mkdirs)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=jsMain.quit)

        helpmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="Donate", command=dontF)
        helpmenu.add_command(label="About Us", command=abtF)
        helpmenu.add_command(label="How to use", command=howtF)

        jsMain.config(menu=menubar)
        jsMain.title("Xendit@Transfer Page")
        jsMain.geometry("800x540+290+90")
        bgPic=PhotoImage(file=Pth + "back.png")
        jsMainLogo=PhotoImage(file=Pth + "cn.png")
        jsMainBackground = Label(jsMain, image=bgPic)
        jsMainBackground.place(x=0, y=0, relwidth=1, relheight=1)
        title = Label(jsMain, text = "XENDIT", font = ("ROBOTO", 20, "bold"), bg = "#8e388e", fg = "WHITE", bd = 10, relief = FLAT)
        title.place (x=0,y=20,relwidth=1)
        jsMainFrame = Frame (jsMain, bg="WHITE")
        jsMainFrame.place(x=245, y=260)
        logoL = Label(jsMainFrame, image = jsMainLogo, bg = "white", bd = 0).grid(row = 0, columnspan = 2, padx = 100, pady = 20)
        try:
            #++++++++++++++++++STRING MANIPULATION TO GET REAL IP ADDRESS FROM dumped IP Info#++++++++++++++++++s
            byteIP = sp.check_output("zaglarh shell ip route")
            stringIP = str(byteIP).rpartition("src") #split tuple into 3
            rIP = stringIP[2] #get the third item in the tuple
            rrIP = rIP.rpartition("\\r\\n")
            devName = sp.check_output("zaglarh shell getprop transsion.device.name")
        except sp.CalledProcessError:
            clr()
            mb.showerror("Device Not Attached", "Hey, put it inside me (^~^)")
        clr()
        text = Text(jsMain, width = 70, height = 7, wrap = WORD)
        text1 = sp.check_output("zaglarh devices")
        text2 = "-" * 70
        text3 = "\nKindly Copy and Paste your device ID below to send or receive.\nPS: Use the setup button for a quick folder setup."
        text.insert(INSERT, text1)
        text.insert(INSERT, text2)
        text.insert(INSERT, text3)
        text.place(x=115, y=100)
        devID = StringVar() #Create variable to store the phone type
        ipEntry = Entry (jsMainFrame, bg = "WHITE", width = 30, textvariable = devID).grid (rows = 2, columnspan = 2, pady = 5)
        sBtn = Button(jsMainFrame, relief = FLAT, command = seActivity, text = "Send", bg = "#8e388e", width = 6, fg = "WHITE", font = ("times new roman", 15, "bold")).grid(row = 4, column = 0, pady = 10)           
        pBtn = Button(jsMainFrame, relief = FLAT, text = "Pull", command = puActivity, bg = "#8e388e", width = 6, fg = "WHITE", font = ("times new roman", 15, "bold")).grid(row = 4, column = 1)
        jsMain.mainloop()

    #++++++++++++++++++CREATE THE FUNCTION THAT CONNECTS THE ANDROID DEVICE WITH THE PC using the IPAddress on Port 4204#++++++++++++++++++
    def connIP():
        ipa = str(ip.get()) #get ip address from entry widget
        por = sp.check_output("zaglarh tcpip " + port)
        output = sp.check_output("zaglarh connect " + ipa + ":" + port)
        confOutput = "b'connected to " + ipa + ":" + port + "\\r\\n'"
        if confOutput == str(output):
            time.sleep(5)
            clr()
            res = mb.askokcancel ("Device Connected", "You can pull it out now (^~^)\n Press OK to continue.")
            if res == True:conn.destroy(), jsMainActivity()
        else:mb.showerror("Not Connected", "Try again!!!\n\nPS: Check that the IP ADDRESS is correct.\nAnd also that you're on the same network")

    #++++++++++++++++++CREATE FUNCTION TO SKIP CONNECTION PAGE#++++++++++++++++++
    def skipConn():
        conn.destroy()
        jsMainActivity()

    conn = Tk()
    ########create app menu
    menubar = Menu(conn)
    filemenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=filemenu)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=conn.quit)

    helpmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="Donate", command=dontF)
    helpmenu.add_command(label="About Us", command=abtF)
    helpmenu.add_command(label="How to use", command=howtF)

    conn.config(menu=menubar)
    conn.title("Xendit: Powered by TeLon")
    conn.geometry("800x540+290+90")
    bgPic=PhotoImage(file=Pth + "back.png")
    connBackground = Label(conn, image=bgPic)
    connBackground.place(x=0, y=0, relwidth=1, relheight=1)
    #++++++++++++++++++Set Display Name#++++++++++++++++++
    title = Label(conn, text = "WIRELESS CONNECTION", font = ("ROBOTO", 20, "bold"), bg = "#8e388e", fg = "WHITE", bd = 10, relief = FLAT)
    title.place (x=220,y=30)
    #++++++++++++++++++Create Connection Frame#++++++++++++++++++
    connFrame = Frame (conn, bg="WHITE")
    connFrame.place(x=290, y=320)
    #++++++++++++++++++Handle error that occurs if the device isnt attached with USB#++++++++++++++++++
    try:
        #++++++++++++++++++STRING MANIPULATION TO GET REAL IP ADDRESS FROM dumped IP Info#++++++++++++++++++
        byteIP = sp.check_output("zaglarh shell ip route")
        stringIP = str(byteIP).rpartition("src") #split tuple into 3
        rIP = stringIP[2] #get the third item in the tuple
        rrIP = rIP.rpartition("\\r\\n")
        ipAdd = rrIP[0] #get the first item in the new partition
        devName = sp.check_output("zaglarh shell getprop transsion.device.name")
        #++++++++++++++++++Initialize a text class to insert texts in the current window#++++++++++++++++++
        text = Text(conn, width = 70, height = 10, wrap = WORD)
        text1 = sp.check_output("zaglarh devices")
        text2 = "PS: If you device isnt connected, kindly get your IP Address below and place it in the to box connect. Or skip if your device is present.\n\n" + line
        text3 = byteIP
        text.insert(INSERT, text1)
        text.insert(INSERT, text2)
        text.insert(INSERT, text3)
        text.place(x=115, y=120)
        ip = StringVar() # Create StringVar variable to store the ip address.
        pType = StringVar() #Create variable to store the phone type
        ipEntry = Entry (connFrame, bg = "WHITE", width = 30, textvariable = ip).grid (rows = 2, columnspan = 2, pady = 20)
        spPhone = Spinbox (connFrame, state = "readonly", textvariable = pType, bg = "WHITE", wrap = True, width = 30, values = (devName, "HUAWEI Y7 Prime 2019", "Infinix Note 5 Stylus", "Samsung Galaxy S7 Edge", "Samsung Galaxy S8 Edge", "Nokia ")).grid(row = 3, columnspan = 2, padx = 10, pady = 1)
        btn = Button(connFrame, relief = FLAT, command = connIP, text = "Link", bg = "#8e388e", width = 6, fg = "WHITE", font = ("ROBOTO", 15, "bold")).grid(row = 4, column = 0, pady = 10)           
        btn2 = Button(connFrame, relief = FLAT, text = "Skip", command = skipConn, bg = "#112f6d", width = 6, fg = "WHITE", font = ("ROBOTO", 15, "bold")).grid(row = 4, column = 1)
        conn.mainloop()
    except sp.CalledProcessError:
        clr()
        mb.showerror("Device Not Attached", "Hey, put it inside me (^~^)")
        conn.mainloop ()
jsConn()


