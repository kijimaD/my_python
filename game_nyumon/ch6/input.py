import tkinter

def click_btn():
    txt = entry.get()
    button["text"] = txt

root = tkinter.Tk()
root.title("input")
root.geometry("400x200")

entry = tkinter.Entry(width=20)
entry.place(x=10, y=10)

button = tkinter.Button(text="get",
                        command=click_btn)
button.place(x=20, y=100)
root.mainloop()
