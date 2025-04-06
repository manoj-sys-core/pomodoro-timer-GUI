
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#ACD3A8"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer =None
from tkinter import *
import math
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer_label.config(text="Timer")
    checkmark_label.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def count(counts):
    count_min = math.floor(counts/60)
    count_sec = counts % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if counts > 0:
        global timer
        timer = window.after(1000, count, counts-1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✔"
        checkmark_label.config(text=mark)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_time = WORK_MIN *60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0 :
        timer_label.config(text="Long Break",foreground=PINK)
        count(long_break)
    elif reps % 2 == 0:
        timer_label.config(text="Short Break",foreground="purple")
        count(short_break)
    else:
        timer_label.config(text="Work Time",foreground="#18230F")
        count(work_time)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(pady=50,padx=100,bg=YELLOW)


canvas = Canvas(width=500,height=500,bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="myimage.png")
canvas.create_image(250 , 250,image=image)
timer_text = canvas.create_text(250,230,text="00.00",fill="#5F8B4C",font=(FONT_NAME,60,"bold"))
canvas.grid(column=2,row=2)

timer_label = Label(text="Timer",font=(FONT_NAME,30),foreground="green",bg=YELLOW)
timer_label.grid(column=2,row=1)

start_button = Button(text="Start",foreground="blue",bg=YELLOW,width=8,command=start_timer)
start_button.grid(column=1,row=3)

checkmark_label = Label(text="",foreground="purple",bg=YELLOW)
checkmark_label.grid(column=2,row=4)

reset_button = Button(text="Reset",foreground="blue",bg=YELLOW,width=8,command=reset)
reset_button.grid(column=3,row=3)

window.mainloop()