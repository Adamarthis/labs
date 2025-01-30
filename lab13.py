import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("600x900")
root.title("Speed Calculator")
root.resizable(False, False)
root.wm_iconphoto(False, ImageTk.PhotoImage(Image.open('atom.png')))
root.configure(background='darkgreen')
problem = tk.IntVar(value=0)
show_formula = tk.BooleanVar()
show_units = tk.BooleanVar()
resulty = tk.StringVar(value="Answer will be here")
time=tk.StringVar(value="1")
distance=tk.StringVar(value="1")

def right1():
    curvalue = int(time.get())
    time.set(str(curvalue+problem.get()))
def left1():
    if int(time.get())-problem.get() < 0:
        pass
    else:
        curvalue = int(time.get())
        time.set(str(curvalue-problem.get()))
def right2():
    curvalue = int(distance.get())
    distance.set(str(curvalue + problem.get()))
def left2():
    if int(distance.get()) - problem.get() < 0:
        pass
    else:
        curvalue = int(distance.get())
        distance.set(str(curvalue - problem.get()))
def calculate():
    res = int(distance.get()) / int(time.get())
    if show_units.get() == False and show_formula.get() == True:
        resulty.set(f"{distance.get()} / {time.get()} = {res}")
    elif show_units.get() == True and show_formula.get() == False:
        resulty.set(f"{res} m/s")
    elif show_units.get() == True and show_formula.get() == True:
        resulty.set(f"{distance.get()} m / {time.get()} s = {res} m/s")
    else:
        resulty.set(f"{res}")
        print(resulty.get())
font_e = "Comic Sans MS"

add1 = tk.Radiobutton(root, width=100,value=1,variable=problem, text = "-1+", bg="darkseagreen", font=(font_e, 24), relief="groove", activebackground="lawngreen")
add5 = tk.Radiobutton(root,width=100,value=5,variable=problem, text = "-5+", bg="darkseagreen", font=(font_e, 24), relief="groove", activebackground="lawngreen")
add10 = tk.Radiobutton(root,width=100,value=10,variable=problem, text = "-10+", bg="darkseagreen", font=(font_e, 24), relief="groove", activebackground="lawngreen")

check_unit = tk.Checkbutton(root,width=100, onvalue=True, offvalue=False, variable=show_units, text="Show units", font=("font_e", 18), bg="seagreen", relief="groove", activebackground="lawngreen")
check_formula = tk.Checkbutton(root,width=100,onvalue=True, offvalue=False, variable=show_formula, text="Show calculation", font=("font_e", 18), bg="seagreen", relief="groove", activebackground="lawngreen")

valuebut_1var = tk.Label(root, text="Time, s", width=10, height=0, bg="seagreen3", font=(font_e, 15))
valuebut_2var = tk.Label(root, text="Distance, m", width=10, height=0, bg="seagreen3", font=(font_e, 15))
left_arrow_1var = tk.Button(root, text = "-", width=5, height=0, bg="seagreen2", font=(font_e, 15), activebackground="lawngreen", relief="groove", command=left1)
right_arrow_1var = tk.Button(root, text = "+", width=5, height=0, bg="seagreen2", font=(font_e, 15), relief="groove", activebackground="lawngreen", command=right1)
left_arrow_2var = tk.Button(root, text = "-", width=5, height=0, bg="seagreen2", font=(font_e, 15), activebackground="lawngreen", relief="groove", command=left2)
right_arrow_2var = tk.Button(root, text = "+", width=5, height=0, bg="seagreen2", font=(font_e, 15), relief="groove", activebackground="lawngreen", command=right2)

var1text = tk.Label(root, width=5, height=1, bg="seagreen3", font=(font_e, 22), compound="center",textvariable=time)
var2text = tk.Label(root, width=5, height=1, bg="seagreen3", font=(font_e, 22), compound="center", textvariable=distance)

calculate_button = tk.Button(root, text = "CALCULATE", width=10, height=3, bg="red", font=(font_e, 15), relief="groove", activebackground="lawngreen", command=calculate)

tk.Label(root,width=25, height=0, text = "Calculate Speed", bg="darkgreen", font=(font_e, 46)).pack()
tk.Label(root,width=25, text = "Settings", bg="lightseagreen", font=(font_e, 30)).pack()

add1.pack()
add5.pack()
add10.pack()

check_unit.pack()
check_formula.pack()

valuebut_1var.pack(side="top", anchor="w")
right_arrow_1var.pack(side="top", anchor="w")
var1text.pack(side="top", anchor="w")
left_arrow_1var.pack(side="top", anchor="w")
valuebut_2var.pack(side="top", anchor="nw")
right_arrow_2var.pack(side="top", anchor="nw")
var2text.pack(side="top", anchor="nw")
left_arrow_2var.pack(side="top", anchor="nw")

result = tk.Label(root, textvariable=resulty, font=(font_e, 22), background="darkgreen")
result.pack()
calculate_button.pack()

root.mainloop()
