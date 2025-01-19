from tkinter import ttk
from entry import Entry

class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(style="Page1.TFrame")
        

     # Używamy grid zamiast pack
        ttk.Label(self, text="Jaka to melodia ?", font=("Arial", 24)).grid(row=0, column=0, columnspan=2, pady=20)
        ttk.Label(self, text="Witaj w grze jaka to melodia ;)\nNa samym początku wybierz kraj", font=("Arial", 16), anchor="center").grid(row=1, column=0, columnspan=2, pady=20)

        self.create_answer()

    def create_answer(self):
        style = ttk.Style()
        style.configure("Custom.TButton", relief="flat")

        # Konfiguracja wiersza i kolumn dla przycisków
        self.grid_rowconfigure((0,1,2), minsize=175)  # Wiersz 0, aby przyciski miały minimalną wysokość
        self.grid_columnconfigure((0,1), minsize=475)  # Kolumna 0, szerokość przycisku

        # Przyciski do odpowiedzi
        button1 = ttk.Button(self, text="Pierwsza odpowiedź", )
        button2 = ttk.Button(self, text="Druga odpowiedź")

        # Umieszczanie przycisków obok siebie w tym samym wierszu, ale różnych kolumnach
        button1.grid(row=2, column=0, sticky='nswe')
        button2.grid(row=2, column=1, sticky='nswe')
        



