from tkinter import *


def validate_entry(symbol):
    return True


class FrameLEB:

    def __init__(self, name_label, name_button, fr, func, val, args):
        self.label_frame = LabelFrame(fr)
        self.label = Label(self.label_frame, text=name_label, width=15, font=('Times 14'))
        self.entry = Entry(self.label_frame, validate="key", validatecommand=(fr.register(validate_entry), "%S"))
        self.button = Button(self.label_frame, text=name_button, font=('Times 14'), command=lambda: func(*args))
        self.entry.insert(END, val)
        self.label.pack(side=LEFT, ipadx=5, padx=5)
        self.entry.pack(side=LEFT, ipadx=5, padx=5)
        self.button.pack(side=LEFT, ipadx=5, padx=5)
        self.label_frame.pack(side=TOP, fill='both')

    def get(self):
        return self.entry.get()


class FrameLE:

    def __init__(self, name_label, fr, val):
        self.label_frame = LabelFrame(fr)
        self.label = Label(self.label_frame, text=name_label, width=15, font=('Times 14'))
        self.entry = Entry(self.label_frame, validate="key", validatecommand=(fr.register(validate_entry), "%S"))
        self.label.pack(side=LEFT, ipadx=5, padx=5)
        self.entry.pack(side=LEFT, ipadx=5, padx=5)
        self.label_frame.pack(side=TOP, fill='both')
        self.entry.insert(END, val)

    def get(self):
        return self.entry.get()


class Row:
    def __init__(self, name, fr, i):
        self.label_frame = LabelFrame(fr)
        self.entry_n = Entry(self.label_frame, validate="key", validatecommand=(fr.register(validate_entry), "%S"), width=13)
        self.entry_g = Entry(self.label_frame, validate="key", validatecommand=(fr.register(validate_entry), "%S"), width=13)
        self.entry_k = Entry(self.label_frame, validate="key", validatecommand=(fr.register(validate_entry), "%S"),
                             width=13)
        self.var = DoubleVar()
        self.var.set(False)
        self.check = Checkbutton(self.label_frame, variable=self.var, onvalue=1., offvalue=.0)
        self.entry_n.insert(END, f'{(i + 1) * 100}')
        self.entry_k.insert(END, f'{(i + 1) * 1000}')
        if i > 0:
            self.entry_g.insert(END, f'{-0.01}')
        else:
            self.entry_g.insert(END, f'{0.01}')
        self.label = Label(self.label_frame, text=name, width=8, font=('Times 14'))
        self.label.pack(side=LEFT, ipadx=5, padx=5)
        self.entry_n.pack(side=LEFT, ipadx=5, padx=5)
        self.entry_g.pack(side=LEFT, ipadx=5, padx=5)
        self.check.pack(side=LEFT, ipadx=70, padx=5)
        self.entry_k.pack(side=LEFT, ipadx=5, padx=5)
        self.label_frame.pack(side=TOP, fill='both')


class RowR:
    def __init__(self, fr, n, cur):
        self.label_frame = LabelFrame(fr)
        self.entries = []
        self.label = Label(self.label_frame, text=f'{cur}', width=4, font=('Times 14'))
        self.label.pack(side=LEFT, ipadx=5, padx=5)
        for i in range(n):
            self.entries.append(Entry(self.label_frame, validate="key", validatecommand=(fr.register(validate_entry), "%S"), width=13))
            self.entries[-1].pack(side=LEFT, ipadx=0, padx=13)
            if i == cur:
                self.entries[-1].insert(END, f'{0}')
            elif i > cur:
                self.entries[-1].insert(END, f'{-0.0001}')
            else:
                self.entries[-1].insert(END, f'{0.0001}')
        self.label_frame.pack(side=TOP, fill='both')
