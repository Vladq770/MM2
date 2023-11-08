import matplotlib as mpl
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button
import tkinter.filedialog as fd
from calculations import *
mpl.use('TkAgg')


def chart(window, n, time, step, left_matr, right_matr):
    res = calculate_populations(n, time, step, left_matr, right_matr)
    count_steps = int(time / step) + 1
    lin_t = [i * step for i in range(count_steps)]
    fig = plt.Figure(figsize=(10, 6), dpi=100)
    colors = ["red", "blue", "green", "black", "orange", "peru", "aqua", "pink", "olive", "lime"]
    plt1 = fig.add_subplot(1, 1, 1)
    for i in range(n):
        plt1.plot(lin_t, res[i, :], color=colors[i % len(colors)], label=f'Вид {i}, {int(res[i, -1])} ос.')
    plt1.set_title(f'Всего особей = {int(res[:, -1].sum())}\nВремя моделирования = {time}')
    plt1.legend(fontsize="small")

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()

    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()

    canvas.get_tk_widget().pack()
