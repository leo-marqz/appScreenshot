import pyautogui
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
import time

def crearWidgets():
  etiquetaGuardar = Label(vn, text = 'Guardar como: ' , font = ('',10, 'bold')) #, bg = "darkslategrey")
  etiquetaGuardar.grid(row = 1, column = 0, padx = 5, pady = 5)
  
  vn.textoGuardar = Entry(vn, width = 30)
  vn.textoGuardar.grid(row = 1, column = 1, padx = 5, pady = 5)
  
  btnGuardar = Button(vn, text='Navegar', width = 10, command = navegar)
  btnGuardar.grid(row = 1, column = 2, padx = 5, pady = 10)
  
  btnCaptura = Button(vn, text = 'Captura', width = 10, command = captura)
  btnCaptura.grid(row = 2, column = 1, padx = 5, pady = 10)
  
  # "C:\\Users\\FUJITSU\\Downloads"
  
def navegar():
  vn.archivoNombre = filedialog.asksaveasfilename(title = "Guardar como", defaultextension = ".pgn",
                                                  filetypes = (("Archivo Png", "*.png"), ("Todos los archivos", "*.*")))
  vn.textoGuardar.insert("1",vn.archivoNombre)

def captura():
  vn.withdraw()
  time.sleep(0.5)
  captura = pyautogui.screenshot()
  captura.save(vn.archivoNombre)
  messagebox.showinfo("Exito", message = "Screenshot Guardada") #mensaje
  vn.deiconify()                                          

vn = tk.Tk()
vn.title("Screenshot")
crearWidgets()
vn.mainloop()