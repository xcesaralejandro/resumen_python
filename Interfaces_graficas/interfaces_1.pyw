# Importamos la libreria de interfaces graficas 
# OBS: la extensión pyw permite que la aplicación sea ejecutada por pythonw.exe y no python.exe
#      la ventaja de pythonw es que no mantiene la consola abierta, lo que es ideal para ejecutar aplicaciones
#      que poseen interfaz grafica. 

from tkinter import * 
raiz = Tk()
raiz.title("Mi primera ventana")

# Definir el tamano de la ventana 
raiz.geometry("1024x768")

# Limitar el estiramiento de la ventana por ancho o alto
raiz.resizable(True,True)

# Cambiar el icono de la barra (Solo formato .ico y el nombre en realidad es la ruta hacia el archivo)
raiz.iconbitmap("sol.ico")

# Configuraciones (Revisar parametros aceptados)
raiz.config(bg="green")
miFrame = Frame()
miFrame.pack(fill="both", expand="True")
miFrame.config(bg="red")
miFrame.config(width = "650", height = "200")

raiz.mainloop()
