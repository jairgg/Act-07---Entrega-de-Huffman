# Act-07---Entrega-de-Huffman

Introducción.
El algoritmo de Huffman es un algoritmo que nos da un método que nos permite comprimir información usando la recodificación de bytes. La técnica consiste en asignar a cada byte un código binario compuesto por una cantidad de bits lo más corta posible. Esta cantidad será variable y dependerá de la probabilidad de ocurrencia del byte.
Objetivos.
Crear un programa en Python que comprima un archivo de texto utilizando el algoritmo de compresión de Huffman.


Desarrollo.
 
Aquí definimos las librerías necesarias para el funcionamiento, además creamos la ventana principal root. (Se usa tkinter como ttk ya que de este modo el aspecto visual tiene un aspecto más moderno).
 
Debajo de las funciones declaramos los estilos de la ventana como el título, tamaño, fuente, y color, de texto asi como de botón. Después llamamos a la función principal y corremos la interfaz gráfica con mainloop.
 
En la función principal se tiene un for que limpia el widget en caso de tener algo antes, Después imprime la etiqueta que nos dice que se trata del menú de selección de archivos, se nos invita a abrir un archivo y tenemos los botones de abrir archivo o examinar y cerrar ventana.
 
Después se nos envía a la función explorador la cual comienza con la parte que se encargara de abrir el archivo desde el explorador usando askopenfilename, limita los archivos a solo .txt y al elegir uno se nos muestra el mensaje de archivo abierto además de la ruta de este mismo, Seguido de esto nos envía a la función de leer texto y se imprimen los botones de Comprimir y Descoprimir. 
 
En la función de leer texto, se necesitan los datos del archivo abierto que se encuentran en f_path después usamos esto para usar la función open, y leer f_path en modo lectura. Lo guardaremos en texto y seguido de esto guardamos la frecuencia de los caracteres en “frecuencia” para contarlos usando Counter de la librería collections, por ultimo los imprimiremos en la consola con un for para comprobar que los leyó de manera correcta.
