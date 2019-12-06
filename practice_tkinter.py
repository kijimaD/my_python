import tkinter as tk
root = tk.Tk()

# root.title("位置指定")
# root.geometry("450x350+350+250")
# root.mainloop()

root.title("部品の作成")
root.geometry("350x150")
# 部品の作成
lb = tk.Label(text="ラベル")
bt = tk.Button(text="ボタン")
# 配置
lb.pack()
bt.pack()
root.mainloop()
