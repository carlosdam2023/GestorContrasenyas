import bcrypt
import random
from model.ComboHash import ComboHash
import tkinter as tk

'''
Lista de ComboHash con hashes y dominios, 
falta por implementar que esa lista se cree con datos deserializados
'''
comboHashes = []

#Menu principal
def crearMenu(dimensiones):
    main = tk.Tk()
    main.geometry(dimensiones)
    main.title("Gestor de contraseñas")

    crearBotones(main)
    entryPass, entryDominio = crearEntrys(main)

    return main

#Función para leer los datos introducidos
def gestionarDatos():
    password, dominio = leerEntrys(entryPass, entryDominio)
    #Objeto ComboHash con la contraseña encriptada y su dominio
    comboHash = encriptarDatos(password, dominio)
    comboHashes.append(comboHash)

def encriptarDatos(password, dominio):
    salt = bcrypt.gensalt()
    hash = bcrypt.checkpw(password.encode('utf-8'), salt)
    return ComboHash(hash, dominio)

def leerEntrys(passw, dom):
    password = passw.get()
    dom = dom.get()
    return password, dom

def crearEntrys(main):
    global entryPass, entryDominio
    labelPass = tk.Label(main, text="Contraseña")
    entryPass = tk.Entry(main, width=30)
    labelDominio = tk.Label(main, text="Dominio")
    entryDominio = tk.Entry(main, width=30)
    labelPass.pack()
    entryPass.pack()
    labelDominio.pack()
    entryDominio.pack()
    return entryPass, entryDominio

def crearBotones(main):
    button = tk.Button(main, text="Nueva contraseña", command=gestionarDatos)
    button.pack()

if __name__ == "__main__":
    main = crearMenu("500x300")

    main.mainloop()

