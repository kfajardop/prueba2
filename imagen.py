import tkinter as tk
from tkinter import PhotoImage  # Importa PhotoImage para manejar imágenes
from ortools.linear_solver import pywraplp
import os

class TransportProblemSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg="#F0F8FF")  # Cambia el color de fondo de la ventana
        self.root.title("Modelo de Optimización")
        self.solution_count = 1  # Variable para contar las soluciones 

        # Agregar una imagen
        img = PhotoImage(file="C:\\Users\\keisy\\OneDrive\\Desktop\\UMG\\6o. Ciclo\\Operaciones\\Prueba1\\3.png") 
        img_label = tk.Label(root, image=img, bg="#F0F8FF")
        img_label.image = img  
        img_label.grid(row=0, column=4, rowspan=2, padx=10, pady=10, sticky='e')  

    
    
if __name__ == "__main__":
    root = tk.Tk()
    app = TransportProblemSolverGUI(root)
    root.mainloop()
