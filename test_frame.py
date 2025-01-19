from tkinter import ttk
from entry import Entry

class Test(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Tworzenie instancji Entry
        Entry(self, 'Entry 1', 'Button 1', 'blue')
        Entry(self, 'Entry 2', 'Button 2', 'blue')
        Entry(self, 'Entry 3', 'Button 3', 'green')