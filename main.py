from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 20
reps = 0
text_checkmark="✓"
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer")
    label_check.config(text="")
    global reps
    reps = 0
    start_button.config(state=NORMAL)
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    start_button.config(state=DISABLED)
    global reps
    reps += 1

    work_sec = int(WORK_MIN *60)
    short_break_sec = int(SHORT_BREAK_MIN * 60)
    long_break_sec = int(LONG_BREAK_MIN * 60)

    if reps % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(text="Break", fg=RED)
    #If it's the 2nd/4th/6th rep:
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_timer.config(text="Break", fg=PINK)
    # If it's the 1st/3rd/5th/7th reps
    else:
        count_down(work_sec)
        label_timer.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_second = count % 60

    if count_second < 10:
        count_second = f"0{count_second}"

    if count_second == 0:
        count_second = "00"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += text_checkmark
        label_check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# fg = GREEN


##tomato pic ui
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


#label timer ui
label_timer = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
label_timer.grid(column=1, row=0)

#start and reset button
start_button = Button(text="Start", command=start_timer, font=(FONT_NAME, 15, "bold"))
start_button.grid(column=0, row=2)


end_button = Button(text="Reset", command=reset_timer, font=(FONT_NAME, 15, "bold"))
end_button.grid(column=2, row=2)

#checkmark label
label_check = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
label_check.grid(column=1, row=3)

window.mainloop()