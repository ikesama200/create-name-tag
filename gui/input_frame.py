import tkinter as tk

class InputFrame(tk.Frame):
    def __init__(self, master, data):
        super().__init__(master)
        self.data = data

        tk.Label(self, text="入力値").pack()
        self.entry = tk.Entry(self)
        self.entry.pack()

        tk.Button(self, text="保存", command=self.save).pack()

    def save(self):
        self.data.value = self.entry.get()
