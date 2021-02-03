import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry('200x100')

# Label
var=tk.StringVar()
l = tk.Label(window, text='Test_Label', textvariable=var, bg='green', font=('Arial', 12), width=15, height=2)
l.pack()



# button
b=tk.Botton(window, test='hit me', width=15,height=2,command=hit_me)
window.mainloop()