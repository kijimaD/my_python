import tkinter
import random

def click_btn():
    label["text"]=random.choice(["1", "2", "3", "4", "5"])
    label.update()

root = tkinter.Tk()
root.title("kuji")
root.resizable(False, False)    # 横、縦

# 背景
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()

# 前画像
img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(400, 300, image=img)

# ラベル
label = tkinter.Label(root, text="??", font=("System", 120), bg="white")
label.place(x=380, y=60)
button = tkinter.Button(root, text="draw",
                        font=("System", 36),
                        fg="skyblue",
                        command=click_btn)
button.place(x=360, y=400)

root.mainloop()
