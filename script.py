from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
def newfile():
    global file
    root.title("Untitled - Script-pad")
    file=None
    textarea.delete(1.0,END)

def openfile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("all files","*.*"),("text documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+" - Script-pad")
        textarea.delete(1.0,END)
        f=open(file,"r")
        textarea.insert(1.0,f.read())
        f.close()


def savefile():
    global file
    if file == None:
        file=asksaveasfilename(initialfile='Untitled.txt',
                               defaultextension=".txt",
                               filetypes=[("all files","*.*"),("text documents","*.txt")])
        if file == "":
            file=None
        else:
            f=open(file,"w")
            f.write(textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+" - Scriptpad")
            print("file saved")
    else:
        f = open(file, "w")
        f.write(textarea.get(1.0, END))
        f.close()

def quitapp():
    root.destroy()
def cut():
    textarea.event_generate(("<<Cut>>"))
def copy():
    textarea.event_generate(("<<Copy>>"))
def paste():
    textarea.event_generate(("<<Paste>>"))
def about():
    showinfo('INFO','SCRIPT-PAD v1.0')

if __name__ == '__main__':
    root=Tk()

    root.title("Untitled - Script-pad")
    root.geometry("600x650")

    textarea=Text(root,font='lucida 13 bold')
    file=None
    textarea.pack(expand=True,fill=BOTH)
    # ****************************
    # MENU-BAR   START
    # ***********************
    Menubar=Menu(root)
    Filemenu=Menu(Menubar,tearoff=0)

    Filemenu.add_command(label="New",command=newfile)
    Filemenu.add_command(label="open",command=openfile)
    Filemenu.add_command(label="save",command=savefile)

    Filemenu.add_separator()
    Filemenu.add_command(label="Exit",command=quitapp)
    Menubar.add_cascade(label='File',menu=Filemenu)
    root.config(menu=Menubar)
    # *********************
    # MENU-BAR ENDS
    # ******************

    # ***************
    # EDIT MENU START
    # ***************

    editmenu=Menu(Menubar,tearoff=0)
    editmenu.add_command(label='Cut',command=cut)
    editmenu.add_command(label='Copy',command=copy)
    editmenu.add_command(label='Paste',command=paste)

    Menubar.add_cascade(label='Edit',menu=editmenu)

    # ***************
    # EDIT MENU ENDS
    # ***************


    # ***************
    # HELP MENU STARTS
    # ***************

    helpmenu=Menu(Menubar,tearoff=0)
    helpmenu.add_command(label='About script-pad',command=about)
    Menubar.add_cascade(label='Help',menu=helpmenu)


    # ***************
    # ADD SCROLL-BAR
    # ***************

    scroll=Scrollbar(textarea)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand=scroll.set)



    root.mainloop()