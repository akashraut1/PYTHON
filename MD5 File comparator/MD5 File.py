import tkinter
from tkinter import * 
from tkinter import messagebox
from tkinter import filedialog
import hashlib
root=Tk()
root.geometry("500x500")
from distutils.core import setup
import py2exe
main_win = tkinter.Tk()
main_win.geometry("500x500")
file1=""
file2=""
main_win.title("MD5 crossover")
x=[]
def md():
    file1= filedialog.askopenfilename()
    path.config(text=file1)
    x.append(file1)
md = tkinter.Button(main_win, text = "Choose File", command = md)
md.pack(side=LEFT)
path=Label(main_win)
path.pack(side=LEFT)
def md1():
    file2= filedialog.askopenfilename()
    path1.config(text=file2)
    x.append(file2)
md1 = tkinter.Button(main_win, text = "Choose File ", command = md1)
md1.pack(side=RIGHT)
path1=Label(main_win)
path1.pack(side=RIGHT)

def final():
    md5_hash = hashlib.md5()
    with open(x[0],"rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            md5_hash.update(byte_block)
        a=(md5_hash.hexdigest())
    md5_hash = hashlib.md5()
    with open(x[1],"rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            md5_hash.update(byte_block)
        b=(md5_hash.hexdigest())
    if a==b:
        messagebox.showinfo("MD5","it is same file")
    else:
        messagebox.showinfo("MD5","it is different file")
final = tkinter.Button(main_win, text = "GO", command =final)
final.pack(side=BOTTOM)  
main_win.mainloop()
#setup(console=["md..py"])


