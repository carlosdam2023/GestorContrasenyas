import random
import tkinter as tk

#Menu principal
def crearMenu(dimensiones):
    main = tk.Tk()
    main.geometry(dimensiones)
    main.title("Gestor de contraseñas")

    crearBotones(main)

    main.mainloop()

def crearBotones(main):
    button = tk.Button(main, text="Nueva contraseña", command=NotImplemented)
    button.pack()
    
#Menú para insertar una contraseña y su dominio al que pertenece.
def menuNuevaContrasenya():
    return NotImplemented

if __name__ == "__main__":
    crearMenu("500x300")

