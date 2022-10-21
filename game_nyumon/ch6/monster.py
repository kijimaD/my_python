import tkinter

def click_btn():
    text.insert(tkinter.END, "encounter")

root = tkinter.Tk()
root.title("multiline input")
root.geometry("400x200")

button = tkinter.Button(text="msg",
                        command=click_btn)
button.pack()

text = tkinter.Text()
text.pack()

root.mainloop()
