from tkinter import ttk

class Entry(ttk.Frame):
    def __init__(self, parent, label_text, button_text, label_background):
        super().__init__(parent)

        # Tworzenie widżetów Entry
        label = ttk.Label(self, text=label_text, background=label_background)
        button = ttk.Button(self, text=button_text)

        # Układ widżetów
        label.pack(expand=True, fill='both')
        button.pack(expand=True, fill='both', pady=10)

        # Układ ramki
        self.pack(side='left', expand=True, fill='both', padx=20, pady=20)
