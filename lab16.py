from tkinter import *
from math import *

root = Tk()
xx_max, yy_max = 800, 600
root.geometry(f"{xx_max}x{yy_max}")
root.resizable(False, False)
xx0, yy0 = xx_max//2, yy_max//2
func = Canvas(root, width=xx_max, height=yy_max, bg="white")
func.create_line(0, yy0, xx_max, yy0, width=1,arrow=LAST)
func.create_line(xx0, yy_max, xx0, 0, width=1,arrow=LAST)

dt = 0.001  # Щільність ідеальна, швидко шукає графік.
kx, ky = 100, 250  # Масштаб ідеальний.
t = -10

while (t<10):
    x = sin(t+pi/2)+cos(t) # Функція x(t)
    y = sin(x*t/4) # Функція y(t)
    xx = kx*x+xx0
    yy = ky*y*(-1)+yy0
    func.create_oval(xx, yy, xx, yy, fill="black")
    t=t+dt

for i in range(-3, 4):
    x = xx0 + i * kx
    y = yy0 - i * ky
    func.create_line(x, yy0 - 5, x, yy0 + 5, width=1)
    func.create_text(x, yy0 + 15, text=str(i), font=("Arial", 10))
    func.create_line(xx0 - 5, y, xx0 + 5, y, width=1)
    func.create_text(xx0 - 15, y, text=str(i), font=("Arial", 10))

func.pack()
Label(root,text="Ковальчук Адам Андрійович").place(relx=0, rely=0)
root.mainloop()
