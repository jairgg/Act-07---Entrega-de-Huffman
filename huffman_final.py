import tkinter as tk
from tkinter.filedialog import askopenfilename
from collections import Counter

# Variables globales para los archivos comprimidos y descomprimidos, así como la tabla de codificación
archivoComprimido = None
archivoDescomprimido = None
tabla = {}

# Función para crear el árbol de codificación de Huffman a partir del contenido del archivo
def creacionArbol(contenido_archivo):
    ListaNodos = []
    valorTotal = 0
    
    # Definición de la clase para los nodos del árbol
    class Vertice:
        def __init__(self, letra, frecuencia):
            self.letra = letra
            self.frecuencia = frecuencia
            self.left = None
            self.right = None
    
    # Conteo de la frecuencia de los caracteres en el archivo
    frecuencia = Counter(contenido_archivo)
    
    # Creación de nodos para cada carácter y su frecuencia
    for letra, valor in frecuencia.items():
        valorTotal += valor
        vertices = Vertice(letra, valor)
        ListaNodos.append(vertices)

    # Construcción del árbol de Huffman
    while len(ListaNodos) > 1:
        ListaNodos = sorted(ListaNodos, key=lambda x: x.frecuencia)
        nodoUnion = Vertice(None, ListaNodos[0].frecuencia + ListaNodos[1].frecuencia)
        nodoUnion.left = ListaNodos[0]
        nodoUnion.right = ListaNodos[1]
        ListaNodos.append(nodoUnion)
        ListaNodos.pop(0)
        ListaNodos.pop(0)
    
    return ListaNodos

# Función para asignar los códigos de Huffman a cada carácter del árbol
def tablaValores(arbol, codigo, tablaA):
    if arbol.letra is not None:
        tablaA[arbol.letra] = codigo
    if arbol.left is not None:
        arbol2 = arbol.left
        tablaValores(arbol2, codigo + "0", tablaA)
    if arbol.right is not None:
        arbol2 = arbol.right
        tablaValores(arbol2, codigo + "1", tablaA)

# Función para comprimir el contenido del archivo utilizando la tabla de codificación
def comprimir(contenido_archivo):
    valor1 = 0
    listValores = []
    global archivoComprimido
    archivoComprimido = open("archivoComprimido.bin", mode="wb") 
    
    # Asignación de códigos de Huffman a cada carácter
    for claves, valores in tabla.items():
        tabla[claves] = valor1
        valor1 += 1
        
    # Creación de la secuencia de bits comprimida
    for letras in contenido_archivo:
        letras = letras.lower()
        listValores.append(tabla[letras])
    
    archivoComprimido.write(bytearray(listValores))
    archivoComprimido.close()

# Función para descomprimir el archivo comprimido utilizando la tabla de codificación
def descomprimir():
    global archivoDescomprimido
    global tabla
    archivoComprimido = open("archivoComprimido.bin", mode="rb") 
    archivoDescomprimido = open("archivoDescomprimido.txt", mode="w", encoding="UTF-8") 
    
    # Lectura de la secuencia de bits comprimida
    lista = list(archivoComprimido.read())
    for valor in lista:
        # Reconstrucción de los caracteres a partir de los códigos de Huffman
        for claves, valores in tabla.items():
            if valor == valores:
                archivoDescomprimido.write(claves)

    archivoComprimido.close()
    archivoDescomprimido.close()

# Clase para la interfaz gráfica
class Interfaz:
    def __init__(self, ancho=640, alto=480, titulo="Interfaz del Algoritmo de Compresión Huffman"):
        self.contenido_archivo = ""
        self.texto = ""
        self.contador_caracteres = {}
        self.ventana = tk.Tk()
        self.ventana.title(titulo)
        self.ventana.configure(bg="#3296C8")
        self.establecer_dimensiones(ancho, alto)
        self.generar_elementos()
        self.ventana.mainloop()

    # Método para establecer las dimensiones de la ventana
    def establecer_dimensiones(self, ancho, alto):
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()
        posicion_x = (ancho_pantalla - ancho) // 2
        posicion_y = (alto_pantalla - alto) // 2
        self.ventana.geometry(f"{ancho}x{alto}+{posicion_x}+{posicion_y}")

    # Método para generar los elementos de la interfaz
    def generar_elementos(self):
        etiqueta = tk.Label(self.ventana, text="Algoritmo de Compresión Huffman", font=("Comic Sans MS", 30), bg="#3296C8", fg="white")
        etiqueta.pack(pady=20)
        marco = tk.Frame(self.ventana)
        marco.pack(padx=10, pady=10)
        self.texto = tk.Text(marco, wrap="word", width=40, height=10)
        self.texto.pack(side="left", fill="both", expand=True)
        scrollbar = tk.Scrollbar(marco, command=self.texto.yview)
        scrollbar.pack(side="right", fill="y")
        self.texto.config(yscrollcommand=scrollbar.set)
        boton_abrir = tk.Button(self.ventana, text="Examinar", command=self.explorador)
        boton_abrir.pack()
        self.boton_comprimir = tk.Button(self.ventana, text="Comprimir", command=self.comprimir_archivo)
        self.boton_comprimir.pack()
        self.boton_descomprimir = tk.Button(self.ventana, text="Descomprimir", command=descomprimir)
        self.boton_descomprimir.pack()

    # Método para abrir el explorador de archivos y seleccionar un archivo de texto
    def explorador(self):
        global tabla
        ruta_archivo = askopenfilename(initialdir="/", title="Selección de Archivo", filetypes=(("*.txt*","txt"),("Todos los Archivos","*.*")))
        if ruta_archivo.endswith('.txt'):
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                self.contenido_archivo = archivo.read()
                tabla.clear()
                tablaValores(creacionArbol(self.contenido_archivo)[0], "", tabla)
                self.texto.delete(1.0, tk.END)
                frecuencia = Counter(self.contenido_archivo)
                for caracter, conteo in frecuencia.items():
                    frecuencia_texto = f"'{caracter}': {conteo}\n"
                    self.texto.insert(tk.END, frecuencia_texto)
        else:
            print("No se ha seleccionado un archivo de texto.")

    # Método para comprimir el archivo seleccionado
    def comprimir_archivo(self):
        if self.contenido_archivo:
            comprimir(self.contenido_archivo)
        else:
            print("No hay contenido para comprimir")

# Creación de la instancia de la interfaz gráfica
mi_interfaz = Interfaz()
