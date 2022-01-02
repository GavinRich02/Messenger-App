import socket
import threading
from tkinter import *
from tkinter import messagebox
import tkinter.scrolledtext
import tkinter.simpledialog as simpledialog

socketClient = socket.socket()

host = socket.gethostname()
port = 5000

socketClient.connect((host, port))

def send():
    if messageField.get()!="":
        data = username+": "+messageField.get()
        socketClient.send(data.encode())
        messageField.delete(0, END)

usernamescr=Tk()
usernamescr.withdraw()

username=simpledialog.askstring("Username","Enter a Username",parent=usernamescr)
usernamescr.destroy()


root=Tk()
root.title("Totally Rad Messaging App")
root.configure(background='blue')

messageView=tkinter.scrolledtext.ScrolledText(root)
messageView.pack(pady=25)
messageView.config(state='disabled')

messageField=Entry(root)
messageField.pack()

sendButton=Button(root,text='Send',command=send)
sendButton.pack(pady=10)

root.geometry('600x500')


def receive():
    while(True):
        data = socketClient.recv(512).decode()
        data+="\n"
        messageView.config(state='normal')
        messageView.insert('end',data)
        messageView.yview('end')
        messageView.config(state='disabled')

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.quit()
        root.destroy()
        socketClient.close()

root.protocol("WM_DELETE_WINDOW", on_closing)

#t1 = threading.Thread(target = send)
thread = threading.Thread(target = receive)

#t1.start()
thread.start()

'''t1.join()
t2.join()'''

root.mainloop()