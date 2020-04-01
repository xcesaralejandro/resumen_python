from tkinter import * 

root = Tk()

# Especificar el contenedor padre
mainFrame = Frame(root, width=1027, height=768)

# Pack empaqueta en el elemento en el contenedor, en este caso el padre tomara la resolucion del hijo
mainFrame.pack()

title = Label(mainFrame, text="Primer titulo",font=("25"))
# Place es lo mismo que el .pack(), la diferencia es que respeta el tamano y podemos posicionar el elemento dentro del contenedor
title.place(x=200, y=100)

# Una alternativa mas rapida
Label(mainFrame, text="Sub titulo", fg="gray", font=("18")).place(x=200, y=130)

# Agregar imagen como label (Soporta [GIF / PGM / PPM], para otros formatos debes agregar librerias)
miImagen = PhotoImage(file="tierra.gif")
Label(mainFrame, image=miImagen).place(x=0, y=0)

root.mainloop()
