import tkinter as tk
from ttkbootstrap import Style
import random
import time


class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.array = []

        style = Style(theme="darkly")  
        self.root.title(" Algoritmos de Ordenamiento")
        self.canvas = tk.Canvas(self.root, width=800, height=400, bg="pink")
        self.canvas.pack()
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=10)

        tk.Button(self.buttons_frame, text="Generar Lista Aleatoria", command=self.GenerararLista).pack(side=tk.LEFT, padx=5)
        tk.Button(self.buttons_frame, text="Ordenamiento Burbuja", command=self.EjecutarBurbuja).pack(side=tk.LEFT, padx=5)
        tk.Button(self.buttons_frame, text="Ordenamiento Selección", command=self.EjecutarSeleccion).pack(side=tk.LEFT, padx=5)
        tk.Button(self.buttons_frame, text="Reiniciar", command=self.Limpiar).pack(side=tk.LEFT, padx=5)

    def GenerararLista(self):
        self.array = [random.randint(1, 100) for _ in range(30)]
        self.barras()

    def barras(self):
        # dibujo de barras
        self.canvas.delete("all") #limpiar
        bar_width = 800 // len(self.array) #ancho

        for i, value in enumerate(self.array):
            x0 = i * bar_width
            y0 = 400 - (value * 3)  # altura
            x1 = (i + 1) * bar_width
            y1 = 400
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="pink")
            # añadir numeroo
            self.canvas.create_text((x0 + x1) // 2, y0 - 10, text=str(value), fill="white", font=("Arial", 10, "bold"))

    def EjecutarBurbuja(self):
        algoritmos.burbuja(self.array, visualize=self.visualizar)

    def EjecutarSeleccion(self):
        algoritmos.seleccion(self.array, visualize=self.visualizar)

    def visualizar(self, array):
        self.array = array
        self.barras()  # redibuja las barras con los números
        self.root.update_idletasks()  # actu ventana
        time.sleep(0.1)  # Añade un pequeño retraso

    def Limpiar(self):
        # reiniciar el lienzo y la lista
        self.array = []
        self.canvas.delete("all")

class algoritmos:
    @staticmethod
    def burbuja(arr, visualize=None):
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
                    if visualize:
                        visualize(arr)
            if not swapped:
                break

    @staticmethod
    def seleccion(arr, visualize=None):
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            if visualize:
                visualize(arr)

if __name__ == "__main__":
    root = tk.Tk()  # ventana principal
    visualizer = SortingVisualizer(root)
    root.mainloop()  # ciclo principal de tkinter
