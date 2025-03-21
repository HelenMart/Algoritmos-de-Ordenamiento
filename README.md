### Descripción
El siguiente programa permite visuaizar los algoritmos de ordenamiento, conocidos como Metodo de burbuja optimizado y seleccion, utilizando una interfaz que permita al usuario interactuar con los metodos

 Principales caracteristias
- Creacion de numeros aletorios
- Ordenamiento por burbuja
- Ordenamiento por seleccion
- Interfaz intuitiva 
- Creacion de metodos visibles

### Librerias utilizadas
- import tkinter as tk
```python
import tkinter as tk
```
Esta libreria nos permite crear una interfz grafica que pueda ser visual y interactiva para el usuario.
- from ttkbootstrap import Style
```python
from ttkbootstrap import Style
```
Nos permite mejorar los acabados en la interfaz grafica

- import random
```python
import random
```
Esta libreria nos facilita la creacion de numeros aleatoreos .
- import time
```python
import time
```
En este caso nos sirve para poder dar un retraso en la ejecucion de los metodos de ordenamiento para que el usuario visualice los intercambios

### Interfaz Grafica
#### Creacion de ventana principal
```python
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
        tk.Button(self.buttons_frame, text="Ordenamiento Burbuja",command=self.EjecutarBurbuja).pack(side=tk.LEFT, padx=5)
        tk.Button(self.buttons_frame, text="Ordenamiento Selección",command=self.EjecutarSeleccion).pack(side=tk.LEFT, padx=5)
        tk.Button(self.buttons_frame, text="Reiniciar", command=self.Limpiar).pack(side=tk.LEFT, padx=5)

```
#### Creacion de barras
```python
def barras(self):
        # dibujo de barras
        self.canvas.delete("all") #limpiar
        bar_width = 800 // len(self.array) #ancho

        for i, value in enumerate(self.array):
            x0 = i * bar_width#coordenada inicial
            y0 = 400 - (value * 3)  # altura
            x1 = (i + 1) * bar_width #final
            y1 = 400#base
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="pink")
            # añadir numeroo
            self.canvas.create_text((x0 + x1) // 2, y0 - 10, text=str(value), fill="white", font=("Arial", 10, "bold"))
```
## Funciones principales
Ordenamiento por burbuja 
```python
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

```

Ordenamiento por seleccion
```python
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

```
Creacion de numeros aleatorios
```python
def GenerararLista(self):
        self.array = [random.randint(1, 100) for _ in range(30)]
        self.barras()
```
