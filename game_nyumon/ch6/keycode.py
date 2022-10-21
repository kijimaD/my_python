import tkinter

key = 0
sym = ""

def key_down(e):
    global key, sym
    key = e.keycode
    sym = e.keysym

def main_proc():
    label["text"] = str(key) + " (" + sym + ")"
    root.after(100, main_proc)

root = tkinter.Tk()
root.title("key input")
root.bind("<KeyPress>", key_down)

label = tkinter.Label(font=("System", 80))
label.pack()

main_proc()
root.mainloop()
