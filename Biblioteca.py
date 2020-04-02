#!/usr/bin/env python
# -*- coding: utf-8 -*-
#hola
#Biblioteca por Dex Loggica
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
#from tkinter import *
import pymysql
#from math import *
import conexion_base_datos

class Application(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Biblioteca")

        self.conexion=conexion_base_datos.Libros
        # Crear el panel de pestañas.
        self.notebook = ttk.Notebook(self)
        # Crear el contenido de cada una de las pestañas.
        self.carga_libros()
        self.listado_completo()
        #self.modificar()
        self.borrado()

        self.notebook.pack(padx=10, pady=10)
        self.pack()

    

    def carga_libros(self):
        #Este es el formulario para cargar libros
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
        self.boton1=ttk.Button(self.labelframe1, text="Registrar",command=self.agregar)
        self.boton1.grid(column=0, row=7, padx=4, pady=4, columnspan=2)

    def agregar(self):
        #recupero los datos dentro de los campos de texto del formulario de carga_libros()
        print("registrar")

        #estas variables hay que editarlas en el formulario para tener un select por codigos numericos
        #no deberian ir fijas
        pais=1
        editorial=1
        cantidad_pedidas=0
        estado=0
        
        #####
        datos=(self.titulo.get(), self.numero.get(), self.paginas.get(), self.fecha.get(), self.isbn.get(), self.imagen.get(), self.link.get(), pais, editorial, cantidad_pedidas, estado )
        ######
        self.conexion.alta(datos)
        mb.showinfo("Información", "Los datos fueron cargados")
        self.titulo.set("")
        self.numero.set("")
        self.paginas.set("")
        self.fecha.set("")
        self.isbn.set("")
        self.imagen.set("") 
        self.link.set("")
        pais
        editorial
        cantidad_pedidas
        estado

    def consulta_por_codigo(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por código")
        self.labelframe1=ttk.LabelFrame(self.pagina2, text="Artículo")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe1, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigo=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelframe1, textvariable=self.codigo)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe1, text="Descripción:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.descripcion=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe1, textvariable=self.descripcion, state="readonly")
        self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe1, text="Precio:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.precio=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.precio, state="readonly")
        self.entryprecio.grid(column=1, row=2, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe1, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)

    def listado_completo(self):
        self.pagina1 = ttk.Frame(self.notebook)
        self.notebook.add(self.pagina1, text="Listado completo")
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

    def consultar(self):
        datos=(self.codigo.get(), )
        respuesta=self.articulo1.consulta(datos)
        if len(respuesta)>0:
            self.descripcion.set(respuesta[0][0])
            self.precio.set(respuesta[0][1])
        else:
            self.descripcion.set('')
            self.precio.set('')
            mb.showinfo("Información", "No existe un artículo con dicho código")

    def borrado(self):
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Borrado de artículos")
        self.labelframe1=ttk.LabelFrame(self.pagina4, text="Artículo")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe1, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigoborra=tk.StringVar()
        self.entryborra=ttk.Entry(self.labelframe1, textvariable=self.codigoborra)
        self.entryborra.grid(column=1, row=0, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe1, text="Borrar", command=self.borrar)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)

    def borrar(self):
        datos=(self.codigoborra.get(), )
        cantidad=self.articulo1.baja(datos)
        if cantidad==1:
            mb.showinfo("Información", "Se borró el artículo con dicho código")
        else:
            mb.showinfo("Información", "No existe un artículo con dicho código")

main_window = tk.Tk()
app = Application(main_window)
app.mainloop()
