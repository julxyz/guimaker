from tkinter import Button, Frame, Tk, Label, Entry, OptionMenu, StringVar, TOP, LEFT, BOTH, FLAT
from tkinter.colorchooser import askcolor
from tkinter.font import Font
from os import path

code = []

def getFgColor():
    global fgColor
    fgColor = askcolor(color="#000000")
    fgColor = fgColor[1]

def getBgColor():
    global bgColor
    bgColor = askcolor(color="#FFFFFF")
    bgColor = bgColor[1]

def center(win):
    win.update_idletasks()
    x = (win.winfo_screenwidth() // 2) - (win.winfo_width() // 2)
    y = (win.winfo_screenheight() // 2) - (win.winfo_height() // 2)
    win.geometry('{}x{}+{}+{}'.format(win.winfo_width(), win.winfo_height(), x, y))

def backtomain():
        main.deiconify()

def createbutton(buttonnam, buttontxt, buttoncmd, relief):
        #buttoncode assembler
        buttoncode = ("{0} = Button(text='{1}', command='{2}', fg='{3}', bg='{4}', relief='{5}')\n{0}.pack()".format(buttonnam,buttontxt,buttoncmd,fgColor,bgColor, relief))
        code.append(buttoncode)

def export():
        #exports finished code into code.txt
        f = open("code.txt", "w+")
        exportcode = ("import tkinter as *\nroot = Tk()\n{0}\nroot.mainloop()".format("\n".join(code)))
        f.write(exportcode)
        f.close

def buttonOptions():
    #windowdef
    buttonoptions = Tk()
    buttonoptions.configure(bg="#222222")
    buttonoptions.geometry("250x300")
    buttonoptions.resizable(0,0)
    buttonoptions.title("Button Editor")
    center(buttonoptions)
    main.withdraw()
    buttonoptions.attributes("-topmost", True)
    buttonoptions.attributes("-topmost", False )
    center(buttonoptions)
    #frame def
    buttonframe1 = Frame(buttonoptions,padx="5",pady="5", bg="#222222")
    buttonframe1.pack(side=TOP)
    buttonframe2 = Frame(buttonoptions,padx="5",pady="5", bg="#222222")
    buttonframe2.pack(side=TOP)
    buttonframe2b = Frame(buttonoptions,padx="5",pady="5", bg="#222222")
    buttonframe2b.pack(side=TOP)
    buttonframe3 = Frame(buttonoptions,padx="5",pady="5", bg="#222222")
    buttonframe3.pack(side=TOP)
    buttonframe4 = Frame(buttonoptions,padx="5",pady="5", bg="#222222")
    buttonframe4.pack(side=TOP)
    buttonframe5 = Frame(buttonoptions,padx="5",pady="5", bg="#222222")
    buttonframe5.pack(side=TOP)
    buttonframe6 = Frame(buttonoptions,padx="5",pady="5", bg="#222222")
    buttonframe6.pack(side=TOP)
    #button name
    buttonnamelabel = Label(buttonframe1, text="Name",bg="#444444",fg="#DDDDDD")
    buttonnamelabel.pack(side=LEFT)
    buttonname = Entry(buttonframe1,width=20,bg="#444444",fg="#DDDDDD",relief="flat")
    buttonname.pack(side=LEFT,fill=BOTH)
    #button disp text
    buttontextlabel = Label(buttonframe2, text="Text",bg="#444444",fg="#DDDDDD")
    buttontextlabel.pack(side=LEFT)
    buttontext = Entry(buttonframe2,width=21,bg="#444444",fg="#DDDDDD",relief="flat")
    buttontext.pack(side=LEFT,fill=BOTH)
    #button command
    buttoncommandlabel = Label(buttonframe2b, text="Method",bg="#444444",fg="#DDDDDD")
    buttoncommandlabel.pack(side=LEFT)
    buttoncommand = Entry(buttonframe2b,width=18,bg="#444444",fg="#DDDDDD",relief="flat")
    buttoncommand.pack(side=LEFT,fill=BOTH)
    #relief dropdown
    relief = StringVar(buttonframe3)
    relief.set("flat") # default value
    reliefm = OptionMenu(buttonframe3, relief,"ridge", "groove", "flat", "sunken", "raised")
    reliefm.configure(bg="#444444", fg="#DDDDDD", relief="flat")
    reliefm["menu"].configure(bg="#444444", fg="#DDDDDD", relief="flat")
    reliefm.pack(side=LEFT)
    #text and background color 
    fgColorPicker = Button(buttonframe4, command=getFgColor, bg="#444444", fg="#DDDDDD", text="Text Farbe", relief="flat")
    fgColorPicker.pack(side=LEFT)
    bgColorPicker = Button(buttonframe4, command=getBgColor, bg="#444444", fg="#DDDDDD", text="Button Farbe", relief="flat")
    bgColorPicker.pack(side=LEFT)
    #create button
    create = Button(buttonframe5, command=lambda: createbutton(buttonname.get(), buttontext.get(), buttoncommand.get(), relief.get()), bg="#444444", fg="#DDDDDD", text="done", relief="flat")
    create.pack(side=LEFT)
    #close button
    close = Button(buttonframe6, command=lambda: [buttonoptions.destroy(),backtomain()], bg="#444444", fg="#DDDDDD", text="close", relief="flat")
    close.pack(side=LEFT)
    ####
    buttonoptions.mainloop()

#main window
main = Tk()
main.configure(bg="#222222")
main.geometry("300x100")
main.resizable(0,0)
main.title((path.basename(__file__)).replace(".py",""))
center(main)

makeButton = Button(main, text= "button", command= buttonOptions, relief="flat",  bg="#444444", fg="#DDDDDD")
makeButton.pack()
exportButton = Button(main, text= "export code", command= export, relief="flat",  bg="#444444", fg="#DDDDDD")
exportButton.pack()

main.mainloop()