import tkinter
tmr = 0

def count_up():
    global tmr                  # 関数の外側で定義した変数の値を、関数内で変更するのに必要。
    tmr = tmr + 1
    label["text"] = tmr
    root.after(1000, count_up)

root = tkinter.Tk()

label = tkinter.Label(font=("System", 80))
label.pack()

root.after(1000, count_up)
root.mainloop()
