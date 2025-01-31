import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("600x900")
root.title("Speed Calculator")
root.resizable(False, False)
root.wm_iconphoto(False, ImageTk.PhotoImage(Image.open('atom.png')))
root.configure(background='darkgreen')

problem = tk.IntVar(value=1)
show_formula = tk.BooleanVar()
show_units = tk.BooleanVar()
resulty = tk.StringVar(value="Answer will be here")
time=tk.StringVar(value="1")
distance=tk.StringVar(value="1")
value_inside = tk.StringVar()

font_e = "Comic Sans MS"

def right1():
    curvalue = int(time.get())
    time.set(str(curvalue+int(value_inside.get())))

def left1():
    if int(time.get())-int(value_inside.get()) < 0:
        pass
    else:
        curvalue = int(time.get())
        time.set(str(curvalue-int(value_inside.get())))

def right2():
    curvalue = int(distance.get())
    distance.set(str(curvalue + int(value_inside.get())))

def left2():
    if int(distance.get()) - int(value_inside.get()) < 0:
        pass
    else:
        curvalue = int(distance.get())
        distance.set(str(curvalue - int(value_inside.get())))

def calculate():
    if int(listbox.curselection()[0])==1:
        res = int(distance.get())*3.281 / int(time.get())
    else:
        res = int(distance.get()) / int(time.get())
    if show_units.get() == False and show_formula.get() == True:
        resulty.set(f"{distance.get()} / {time.get()} = {round(res,3)}")
    elif show_units.get() == True and show_formula.get() == False:
        resulty.set(f"{round(res,3)} {"ft" if int(listbox.curselection()[0])==1 else "m"}/s")
    elif show_units.get() == True and show_formula.get() == True:
        resulty.set(f"{distance.get()} {"ft" if int(listbox.curselection()[0])==1 else "m"} / {time.get()} s = {round(res,3)} {"ft" if int(listbox.curselection()[0])==1 else "m"}/s")
    else:
        resulty.set(f"{res}")

def update():

    history.configure(state="normal")
    history.insert("end", enterhistory.get() + "\n")
    history.configure(state="disabled")


arr = [1, 5, 10, 50, 100]
distances = ["ft", "m"]
menu = tk.OptionMenu(root, value_inside, *arr)
listbox = tk.Listbox(root, height=2, width=100, font=(font_e, 18), background="seagreen")
for i in distances:
    listbox.insert(0,i)

enterhistory = tk.Entry(root,width=12, bg="seagreen", font=(font_e, 18),)
enter = tk.Button(root, text = "UPDATE HISTORY", width=15, height=1, bg="red",font=(font_e, 15), relief="groove",activebackground="lawngreen",command=update)
history = tk.Text(root, width=15, height=7, state="disabled")
check_unit = tk.Checkbutton(root,width=100, onvalue=True, offvalue=False, variable=show_units, text="Show units", font=(font_e, 18), bg="seagreen", relief="groove", activebackground="lawngreen")
check_formula = tk.Checkbutton(root,width=100,onvalue=True, offvalue=False, variable=show_formula, text="Show calculation", font=(font_e, 18), bg="seagreen", relief="groove", activebackground="lawngreen")

valuebut_1var = tk.Label(root, text="Time, s", width=10, height=0, bg="seagreen3", font=(font_e, 15))
valuebut_2var = tk.Label(root, text="Distance", width=10, height=0, bg="seagreen3", font=(font_e, 15))

left_arrow_1var = tk.Button(root, text = "-", width=5, height=0, bg="seagreen2", font=(font_e, 15), activebackground="lawngreen", relief="groove", command=left1)
right_arrow_1var = tk.Button(root, text = "+", width=5, height=0, bg="seagreen2", font=(font_e, 15), relief="groove", activebackground="lawngreen", command=right1)
left_arrow_2var = tk.Button(root, text = "-", width=5, height=0, bg="seagreen2", font=(font_e, 15), activebackground="lawngreen", relief="groove", command=left2)
right_arrow_2var = tk.Button(root, text = "+", width=5, height=0, bg="seagreen2", font=(font_e, 15), relief="groove", activebackground="lawngreen", command=right2)

var1text = tk.Label(root, width=5, bg="seagreen3", font=(font_e, 22),textvariable=time)
var2text = tk.Label(root, width=5, bg="seagreen3", font=(font_e, 22), textvariable=distance)

calculate_button = tk.Button(root, text = "CALCULATE",width=10, height=3, bg="red",font=(font_e, 15), relief="groove",activebackground="lawngreen",command=calculate)

tk.Label(root,width=25, height=0, text = "Calculate Speed",
         bg="darkgreen",
         font=(font_e, 46)).pack()
tk.Label(root,width=25, text = "Settings",
         bg="lightseagreen",
         font=(font_e, 30)).pack()
tk.Label(root,width=100, text = "Choose step:",
         bg="lightseagreen",
         font=(font_e, 15)).pack()
menu.pack()
tk.Label(root,width=100, text = "Choose m or ft.",
         bg="lightseagreen",
         font=(font_e, 15)).pack()
listbox.pack()

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
result.place(relx=0.3, rely=0.7)
calculate_button.place(relx=0.27, rely=0.8)
enterhistory.place(relx=0.5, rely=0.75)
history.place(relx=0.5, rely=0.5)
enter.place(relx=0.5, rely=0.8)
root.mainloop()
