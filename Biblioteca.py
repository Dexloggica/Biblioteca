#!/usr/bin/env python
# -*- coding: utf-8 -*-
#hola
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
        #recupero los datos dentro de los campos de texto
        print("registrar")
        titulo=self.titulo.get()
        print(titulo)
        print(type(titulo))
        numero=self.numero.get()
        print(numero)
        print(type(numero))
        paginas=self.paginas.get()
        print(paginas)
        print(type(paginas))
        fecha=self.fecha.get()
        print(fecha)
        print(type(fecha))
        #fecha="2012-12-01"
        isbn=self.isbn.get()
        print(isbn)
        print(type(isbn))
        imagen=self.imagen.get()
        print(imagen)
        print(type(imagen))
        link=self.link.get()
        print(link)
        print(type(link))
        #pais=IntVar()
        pais=1
        print(pais)
        print(type(pais))
       # editorial=IntVar()
        editorial=1
        print(editorial)
        print(type(editorial))
       # cantidad_pedidas=IntVar()
        cantidad_pedidas=0
        print(cantidad_pedidas)
        print(type(cantidad_pedidas))
        #0 esta 1 no esta en la biblioteca
       # estado=IntVar()
        estado=0
        print(estado)
        print(type(estado))
        
        #♥titulo=self.titulo.get()
        #numero=self.tomo.get()
        #paginas=self.cantidad.get()
        #abro la conexion
        connect = self.conectar()
        #creo el puntero
        cursor=connect.cursor()
        #realizar consulta sql
        print("entrando a consulta")
        #sql="INSERT INTO libro (Titulo,Numero,Paginas,ISBN,LinkImagen,LinkDescarga,Pais_idPais,Editorial_idEditorial,CantidadVecesPedidas,Estado) VALUES ('%s','%d','%d','%s','%s','%s','%d','%d','%d','%d')" % (titulo,numero,paginas,isbn,imagen,link,pais,editorial,cantidad_pedidas,estado)
        sql="INSERT INTO libro (Titulo,Numero,Paginas,FechaPublicacion,ISBN,LinkImagen,LinkDescarga,Pais_idPais,Editorial_idEditorial,CantidadVecesPedidas,Estado) VALUES ('%s','%d','%d','%s','%s','%s','%s','%d','%d','%d','%d')" % (titulo,numero,paginas,fecha,isbn,imagen,link,pais,editorial,cantidad_pedidas,estado)
        try:
            print("try")
            cursor.execute(sql)
            #cerrar puntero
            connect.commit()
        except:
            print("except")
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
        self.numero=tk.IntVar()
        self.entrytomo=ttk.Entry(self.labelframe1, textvariable=self.numero)
        self.entrytomo.grid(column=1, row=1, padx=4, pady=4)
        #CANTIDAD DE PAGINAS
        self.label1=ttk.Label(self.labelframe1, text="Cantidad de Paginas:")
        self.label1.grid(column=0, row=2, padx=4, pady=4)
        self.paginas=tk.IntVar()
        self.entrytomo=ttk.Entry(self.labelframe1, textvariable=self.paginas)
        self.entrytomo.grid(column=1, row=2, padx=4, pady=4)
        #FECHA DE PUBLICACION
        self.label1=ttk.Label(self.labelframe1, text="Fecha de Publicacion:")
        self.label1.grid(column=0, row=3, padx=4, pady=4)
        self.fecha=tk.StringVar()
        self.entrytomo=ttk.Entry(self.labelframe1, textvariable=self.fecha)
        self.entrytomo.grid(column=1, row=3, padx=4, pady=4)
        #ISBN
        self.label1=ttk.Label(self.labelframe1, text="ISBN:")
        self.label1.grid(column=0, row=4, padx=4, pady=4)
        self.isbn=tk.StringVar()
        self.entrytomo=ttk.Entry(self.labelframe1, textvariable=self.isbn)
        self.entrytomo.grid(column=1, row=4, padx=4, pady=4)
        #IMAGEN
        self.label1=ttk.Label(self.labelframe1, text="Link de Imagen:")
        self.label1.grid(column=0, row=5, padx=4, pady=4)
        self.imagen=tk.StringVar()
        self.entrytomo=ttk.Entry(self.labelframe1, textvariable=self.imagen)
        self.entrytomo.grid(column=1, row=5, padx=4, pady=4)
        #LINK DESCARGA
        self.label1=ttk.Label(self.labelframe1, text="Link de Descarga:")
        self.label1.grid(column=0, row=6, padx=4, pady=4)
        self.link=tk.StringVar()
        self.entrytomo=ttk.Entry(self.labelframe1, textvariable=self.link)
        self.entrytomo.grid(column=1, row=6, padx=4, pady=4)
        
        
        #Boton para confirmar registro
        self.boton1=ttk.Button(self.labelframe1, text="Registrar",command=self.registrar)
        self.boton1.grid(column=0, row=7, padx=4, pady=4, columnspan=2)

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
        cursor.execute("SELECT idLibro,Titulo,Numero,Paginas,FechaPublicacion,ISBN,LinkImagen,LinkDescarga,Pais_idPais,Editorial_idEditorial,CantidadVecesPedidas,Estado FROM libro")

        for idLibro,Titulo,Numero,Paginas,FechaPublicacion,ISBN,LinkImagen,LinkDescarga,Pais_idPais,Editorial_idEditorial,CantidadVecesPedidas,Estado in cursor.fetchall():
            print("{0} {1}".format(idLibro,Titulo,Numero,Paginas,FechaPublicacion,ISBN,LinkImagen,LinkDescarga,Pais_idPais,Editorial_idEditorial,CantidadVecesPedidas,Estado))
            self.scrolledtext1.insert(tk.END, "id:"+str(idLibro)+"\nTitulo:"+str(Titulo)+"\nNumero:"+str(Numero)+"\nPaginas:"+str(Paginas)+"\nFechaPublicacion:"+str(FechaPublicacion)+"\nISBN:"+str(ISBN)+"\nLinkImagen:"+str(LinkImagen)+"\nLinkDescarga:"+str(LinkDescarga)+"\nidPais:"+str(Pais_idPais)+"\nidEditorial:"+str(Editorial_idEditorial)+"\nCantidadVecesPedidas:"+str(CantidadVecesPedidas)+"\nEstado:"+str(Estado)+"\n____________________\n")
        cursor.close()
        connect.commit()
        connect.close()
main_window = tk.Tk()
app = Application(main_window)
app.mainloop()
