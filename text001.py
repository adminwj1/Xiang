from tkinter import *

# create canvas
root = Tk()
root.title("Aktieköp")
root.configure(background="white")
frame=Frame(root, width=1100, height=1000)
frame.grid(row=0, column=0)
canvas=Canvas(frame,bg="white",width=1100,height=1000)

# my photo
# photo = PhotoImage(file="aktier.gif")
label0 = Label(frame, bg="white"). grid(row=0, column=0)

# create scrollbar

scrollbar=Scrollbar(frame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
scrollbar.config(command=canvas.yview)
frame.config(width=1100,height=1000)
frame.config(yscrollcommand=scrollbar.set)
frame.pack(side=RIGHT,expand=True,fill=Y)

root.mainloop()
