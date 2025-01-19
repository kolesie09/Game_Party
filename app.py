import tkinter as ttk
from menu import Menu
from main_frame import Main
from test_frame import Test

class App(ttk.Tk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0], size[1])
        self.frames = {}

        # Tworzenie menu
        self.menu = Menu(self, self.switch_frame)

        # Tworzenie stron
        self.create_pages()

    def create_pages(self):
        # Importowanie stron i umieszczanie ich w głównym oknie
        self.frames["page1"] = Main(self)
        self.frames["page2"] = Test(self)

        # Umieszczanie stron w oknie
        for frame_name, frame in self.frames.items():
            frame.place(x = 200, y=0, relwidth=0.83, relheight=1)

        # Ustawienie domyślnej strony
        self.switch_frame("page1")

        self.mainloop()

    def switch_frame(self, frame_name):
        frame = self.frames.get(frame_name)
        if frame:
            frame.tkraise()


    
