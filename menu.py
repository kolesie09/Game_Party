from tkinter import ttk

class Menu(ttk.Frame):
    def __init__(self, parent, switch_frame_func):
        super().__init__(parent)
        self.place(x=0, y=0, width=200, height=600)
        self.switch_frame_func = switch_frame_func
        self.create_widgets()

    def create_widgets(self):

        style = ttk.Style()
        style.configure("Custom.TButton", relief = "flat")

        # Ustawienie minimalnej wysokości wiersza
        self.grid_rowconfigure((0,1,2),minsize=50)  # minimalna wysokość 50 pikseli
        self.grid_columnconfigure((0,1,2),minsize=200)  # minimalna szerokość 200 pikseli

        button1 = ttk.Button(self, text="yyyyyyyyyyyyyy", style="Custom.TButton",command=lambda: self.switch_frame_func("page1"))
        button2 = ttk.Button(self, text="Strona 2", style="Custom.TButton", command=lambda: self.switch_frame_func("page2"))
        button3 = ttk.Button(self, text="Strona 3", style="Custom.TButton", command=lambda: self.switch_frame_func("page3"))

        button1.grid(row=0, column=0, sticky='nswe') 
        button2.grid(row=1, column=0, sticky='nswe')
        button3.grid(row=2, column=0, sticky='nswe')
    
