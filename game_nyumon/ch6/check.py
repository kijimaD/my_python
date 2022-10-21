import tkinter

root = tkinter.Tk()
root.title("check")
root.geometry("400x200")

cval = tkinter.BooleanVar()
cval.set(True)

btn = tkinter.Checkbutton(text="check",
                          variable=cval) # default true
btn.pack()

root.mainloop()
