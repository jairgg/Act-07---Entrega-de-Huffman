import pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from collections import Counter

root=Tk()

def leer_texto(f_path):
    with open(f_path, 'r', encoding='utf-8') as f_path: #Aqui se abrira el archivo seleccionado en modo de lectura
        texto=f_path.read()
        #print(texto)
        #ttk.Label(root, text=texto, font=font_style, background="black", foreground="white").place(x=510, y=400) #Muestra el texto en pantalla (no usar en el libro, se traba feo)
    frecuencia = Counter(texto)
    print("Frecuencia de caracteres:")
    for caracter, count in frecuencia.items(): #Se calcula la frecuencia de todos los caracteres usando Counter de la linea anterior 
        print(f"'{caracter}': {count}") #Se imprime la frecuencia de cada carácter


def principal(): #Esta es la funcion principal donde se Mostraran los Botones para elegir el archivo y realizar los procesos
    for widget in root.winfo_children():
        widget.destroy() #Esta funcion borra el contenido del widget
    ttk.Label(root, text="Menú de seleccion de archivo", font=font_style, background="black", foreground="white").place(x=480, y=15) # Etiqueta imprime el titulo en la parte superior
    archivos = ttk.Label(root, text="Seleccione Archivo:", font=font_style, background="black", foreground="white") #Etiqueta de seleccionar archivo
    archivos.place(x=505, y=50) #posicion de la etiqueta archivo
    ttk.Button(root, text="Examinar", command=lambda: explorador(archivos)).place(x=350, y=100) #Boton que nos lleva a elegir el archivo en el del explorador
    ttk.Button(root, text="Cerrar Ventana", command=root.destroy).place(x=660, y=100) #Boton que cierra todo

def explorador(archivos): #Funcion para abrir el explorador de archivos
    f_path = askopenfilename(initialdir="/",
    title="Seleccion de Archivo", filetypes=(("*.txt*","txt"),("Todos los Archivos","*.*")))
    archivos.configure(text="Archivo Abierto: \n"+f_path)#realiza la apertura del explorador de archivos y lo limita a los tipos .txt ademas de mostrar la ruta
    f_path.endswith('.txt')
    leer_texto(f_path)
    ttk.Button(root, text="Comprimir", command=None).place(x=500, y=200) #Este boton continuara el programa hacia el Comprimir
    ttk.Button(root, text="Descomprimir", command=None).place(x=500, y=250) #Este boton continuara el programa hacia el Descomprimir



#Ventana inicial
root.title("Actividad 07 - Frontend") # Titulo de la ventana
root.geometry("1100x700") #Tamaño de la ventana
font_style=("Arial",12) #Fuente de el texto
root.configure(bg="black") #Color de la ventana

#Estilos de boton
style=ttk.Style()
style.configure("TButton",font=font_style, bg="black", fg="black")

principal()

root.mainloop()