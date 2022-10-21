import tkinter

def click_btn():
    button["text"] = "clicked"

root = tkinter.Tk()
root.title("window")
root.geometry("800x600")

canvas = tkinter.Canvas(root, width=400, height=600, bg="skyblue")
canvas.pack()

label = tkinter.Label(root, text="label",
                      font=("System", 24))
label.place(x=200, y=100)

button = tkinter.Button(root, text="button",
                        font=("System", 24),
                        command=click_btn)
button.place(x=200, y=200)

img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(200, 300, image=img)

root.mainloop()
