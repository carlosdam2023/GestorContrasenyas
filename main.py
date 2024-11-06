import random
import tkinter as tk

def crearMenu(dimensiones):
    main = tk.Tk()
    main.geometry(dimensiones)
    main.title("Gestor de contraseñas")

    crearBotones(main)

    main.mainloop()

def crearBotones(main):
    button = tk.Button(main, text="Nueva contraseña", command=NotImplemented)
    button.pack()
if __name__ == "__main__":
    crearMenu("300x300")