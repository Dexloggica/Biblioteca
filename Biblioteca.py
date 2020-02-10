#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Biblioteca por Dex Loggica 
from tkinter import *
import pymysql
from math import *
from tkinter import ttk
import tkinter as tk
from tkinter import scrolledtext as st

class Application(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Biblioteca")
        # Crear el panel de pestañas.
        self.notebook = ttk.Notebook(self)
        # Crear el contenido de cada una de las pestañas.
        self.carga_libros()
        
        self.busqueda_libros()
        self.notebook.pack(padx=10, pady=10)
        self.pack()
    def conectar(self):
        connection = pymysql.connect(host='localhost',user='root',password='', db='20181020_version1')
        return connection

    def registrar(self):
        #print(self.titulo.get())
        #print(self.tomo.get())
        #print(self.paginas.get())
        titulo=self.titulo.get()
        tomo=self.tomo.get()
        paginas=self.paginas.get()
        #♥titulo=self.titulo.get()
        #numero=self.tomo.get()
        #paginas=self.cantidad.get()
        #abro la conexion
        connect = self.conectar()
        #creo el puntero
        cursor=connect.cursor()
        #realizar consulta sql
        sql="INSERT INTO libro (Titulo,Numero,Paginas,Pais_idPais,Editorial_idEditorial,Estado) VALUES ('%s', '%d','%d', '%d', '%d', '%d')" % (titulo,tomo,paginas,1,1,1)
        try:
            #print("try")
            cursor.execute(sql)
            #cerrar puntero
            connect.commit()
        except:
        #       print("except")
                #en el caso de error
                connect.rollback()
        cursor.close()
        connect.close()
    def carga_libros(self):
        self.pagina1 = ttk.Frame(self.notebook)
        self.notebook.add(self.pagina1, text="Carga de libros")
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Libro")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        #TITULO
        self.label1=ttk.Label(self.labelframe1, text="Titulo:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.titulo=tk.StringVar()
        self.entrytitulo=ttk.Entry(self.labelframe1, textvariable=self.titulo)
        self.entrytitulo.grid(column=1, row=0, padx=4, pady=4)
        #NUMERO DE TOMO
        self.label1=ttk.Label(self.labelframe1, text="Numero de tomo:")
        self.label1.grid(column=0, row=1, padx=4, pady=4)
        self.tomo=tk.IntVar()
        self.entrytomo=ttk.Entry(self.labelframe1, textvariable=self.tomo)
        self.entrytomo.grid(column=1, row=1, padx=4, pady=4)
        #CANTIDAD DE PAGINAS
        self.label1=ttk.Label(self.labelframe1, text="Cantidad de Paginas:")
        self.label1.grid(column=0, row=2, padx=4, pady=4)
        self.paginas=tk.IntVar()
        self.entrytomo=ttk.Entry(self.labelframe1, textvariable=self.paginas)
        self.entrytomo.grid(column=1, row=2, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe1, text="Confirmar",command=self.registrar)
        self.boton1.grid(column=0, row=3, padx=4, pady=4)
    def busqueda_libros(self):
        self.pagina1 = ttk.Frame(self.notebook)
        self.notebook.add(self.pagina1, text="Busqueda de libros")
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Busqueda")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.boton1=ttk.Button(self.labelframe1, text="Listado completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.labelframe1, width=30, height=10)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)
    def listar(self):
        connect = self.conectar()
        cursor=connect.cursor()
        cursor.execute("SELECT idLibro, Titulo, Numero FROM libro")

        for idLibro, Titulo, Numero in cursor.fetchall():
            print("{0} {1}".format(Titulo, Numero))
            self.scrolledtext1.insert(tk.END, "id:"+str(idLibro)+"\nTitulo:"+Titulo+"\nNumero:"+str(Numero)+"\n\n")
        cursor.close()
        connect.commit()
        connect.close()
main_window = tk.Tk()
app = Application(main_window)
app.mainloop()
