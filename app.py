from tkinter import *
from tkinter import ttk
from frames import *
import numpy as np
from chart import chart

rows_left = []
rows_right = []
labels = []
count = 0


def build_chart():
    right_matr = np.zeros((count, count), dtype=float)
    left_matr = np.zeros((count, 4), dtype=float)
    for i in range(count):
        left_matr[i, 0] = float(rows_left[i].entry_n.get())
        left_matr[i, 1] = float(rows_left[i].entry_g.get())
        left_matr[i, 2] = float(rows_left[i].var.get())
        left_matr[i, 3] = float(rows_left[i].entry_k.get())
        for j in range(count):
            right_matr[i, j] = float(rows_right[i].entries[j].get())
    newWindow = Toplevel(win)
    newWindow.grab_set()
    chart(newWindow, count, float(label_time.get()), float(label_step_time.get()), left_matr, right_matr)


def enter():
    global count
    count = int(label_count.get())
    global rows_left, rows_right, labels
    for i in rows_left:
        i.label_frame.pack_forget()
    for i in rows_right:
        i.label_frame.pack_forget()
    for i in labels:
        i.pack_forget()
    rows_right = []
    rows_left = []
    labels = []
    for i in range(count):
        rows_left.append(Row(f'{i}', left_table, i))
        labels.append(Label(right_header, text=f'{i}', width=10, font=('Times 14')))
        labels[-1].pack(side=LEFT)
        rows_right.append(RowR(right_table, count, i))



win = Tk()
win.geometry('1200x800')
win.title('MM2')
#win.resizable(False, False)
wrapper1 = LabelFrame(win)
#wrapper2 = LabelFrame(win)
canvas = Canvas(wrapper1, bg="white", width=1200, height=800)
canvas.pack(side=LEFT)
frame = Frame(canvas)
sb = ttk.Scrollbar(win, orient='vertical', command=canvas.yview)
sb.pack(side=RIGHT, fill='y')
sbv = ttk.Scrollbar(win, orient='horizontal', command=canvas.xview)
sbv.pack(side=BOTTOM, fill='x')
canvas.configure(yscrollcommand=sb.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
canvas.configure(xscrollcommand=sbv.set)
#frame = Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor='nw')
wrapper1.pack(side=BOTTOM, fill='both', expand=True, padx=10, pady=10)

font = ('Times 14')
label_count = FrameLEB("Число видов", "Ввод", frame, enter, 2, ())
label_time = FrameLE("Время", frame, 100)
label_step_time = FrameLE("Шаг", frame, 1)
table_labels = LabelFrame(frame)
left_table = LabelFrame(table_labels)
left_header = LabelFrame(left_table)
left_header.pack(side=TOP)
label1 = Label(left_header, text='№', width=10, font=('Times 14'))
label1.pack(side=LEFT)
label2 = Label(left_header, text='Количество', width=10, font=('Times 14'))
label2.pack(side=LEFT)
label3 = Label(left_header, text='Прирост', width=10, font=('Times 14'))
label3.pack(side=LEFT)
label6 = Label(left_header, text='K', width=10, font=('Times 14'))
label5 = Label(left_header, text='Ограниченность', width=16, font=('Times 14'))
label5.pack(side=LEFT)
label6.pack(side=LEFT)
left_table.pack(side=LEFT)
right_table = LabelFrame(table_labels)
right_header = LabelFrame(right_table)
right_header.pack(side=TOP)
right_table.pack(side=LEFT)
label4 = Label(right_header, text='№', width=6, font=('Times 14'))
label4.pack(side=LEFT)
table_labels.pack(side=TOP, fill='both')
button = Button(frame, text='Построить', font=('Times 14'), command=lambda: build_chart())
button.pack(side=BOTTOM)
enter()


win.mainloop()
