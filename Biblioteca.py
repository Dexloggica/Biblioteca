#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#Biblioteca por Dex Loggica
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import codigo_bbdd

#no deberian ir fijas
pais=1
editorial=1
cantidad_pedidas=0
estado=0

class FormularioBiblioteca:
    def __init__(self):
        self.conexion=codigo_bbdd.conector()

        #creo la ventana
        self.ventana1=tk.Tk()
        self.ventana1.title("Biblioteca")
          
        # Crear el panel de pestañas.
        self.notebook = ttk.Notebook(self.ventana1)
        # Crear el contenido de cada una de las pestañas.
        self.carga_libros()
        self.listado_completo()
        self.modificar()
        self.borrado()
        #determino el tamaño
        self.notebook.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()
    
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
        #####
        datos=(self.titulo.get(), self.numero.get(), self.paginas.get(), self.fecha.get(), self.isbn.get(), self.imagen.get(), self.link.get(), pais, editorial, cantidad_pedidas, estado )
       # datos=(str(self.titulo.get()), self.numero.get(), self.paginas.get(), str(self.fecha.get()), str(self.isbn.get()), str(self.imagen.get()), str(self.link.get()), pais, editorial, cantidad_pedidas, estado )
        print(datos)
        ######
        self.conexion.alta(datos)
        #mb.showinfo("Información", "Los datos fueron cargados")
        #self.titulo.set("")
        #self.numero.set("")
        #self.paginas.set("")
        #self.fecha.set("")
        #self.isbn.set("")
        #self.imagen.set("") 
        #self.link.set("")
        
    def consulta_por_titulo(self):
        self.pagina2 = ttk.Frame(self.notebook)
        self.notebook.add(self.pagina2, text="Consulta por titulo")
        self.labelframe1=ttk.LabelFrame(self.pagina2, text="Libro")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe1, text="Titulo:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.titulo=tk.StringVar()
        #boton para realizar consulta
        self.boton1=ttk.Button(self.labelframe1, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)

    def consultar(self):
        datos=(self.titulo.get(), )
        respuesta=self.conexion.consulta(datos)
        #es necesario instanciar estas variables antes de usarlas
        self.pais=tk.StringVar()
        self.editorial=tk.StringVar()
        self.veces=tk.StringVar()
        self.estado=tk.StringVar()
        if len(respuesta)>0:
            self.titulo.set(respuesta[0][0])
            self.numero.set(respuesta[0][1])
            self.paginas.set(respuesta[0][2])
            self.fecha.set(respuesta[0][3])
            self.isbn.set(respuesta[0][4])
            self.imagen.set(respuesta[0][5])
            self.link.set(respuesta[0][6])
            self.pais.set(respuesta[0][7])
            self.editorial.set(respuesta[0][8])
            self.veces.set(respuesta[0][9])
            self.estado.set(respuesta[0][10])
        else:
            self.titulo.set('')
            self.numero.set('')
            self.paginas.set('')
            self.fecha.set('')
            self.isbn.set('')
            self.imagen.set('')
            self.link.set('')
            self.pais.set('')
            self.editorial.set('')
            self.veces.set('')
            self.estado.set('')
            mb.showinfo("Información", "No existe un libro con dicho titulo")

    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.notebook)
        self.notebook.add(self.pagina3, text="Listado completo")
        self.labelframe1=ttk.LabelFrame(self.pagina3, text="Busqueda")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.boton1=ttk.Button(self.labelframe1, text="Listado completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.labelframe1, width=30, height=10)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)

    def listar(self):
        respuesta=self.conexion.recuperar_todos()
        print(f'respuesta 166 {respuesta}')
        self.scrolledtext1.delete("1.0", tk.END)        
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "idLibro:"+str(fila[0])+
                                              "\ntitulo:"+str(fila[1])+
                                              "\nnumero:"+str(fila[2])+
                                              "\npaginas:"+str(fila[3])+
                                              "\nfecha:"+str(fila[4])+
                                              "\nisbn:"+str(fila[5])+
                                              "\nimagen:"+str(fila[6])+
                                              "\ndescarga:"+str(fila[7])+
                                              "\npais:"+str(fila[8])+
                                              "\neditorial:"+str(fila[9])+
                                              "\nveces:"+str(fila[9])+
                                              "\nestado:"+str(fila[10])+"\n\n")   

    def borrado(self):
        self.pagina4 = ttk.Frame(self.notebook)
        self.notebook.add(self.pagina4, text="Borrado de libros")
        self.labelframe1=ttk.LabelFrame(self.pagina4, text="Libro")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe1, text="idLibro:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.idlibro=tk.IntVar()
        self.entryborra=ttk.Entry(self.labelframe1, textvariable=self.idlibro)
        self.entryborra.grid(column=1, row=0, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe1, text="Borrar", command=self.borrar)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)

    def borrar(self):
        datos=(self.idlibro.get(), )
        cantidad=self.conexion.baja(datos)
        if cantidad==1:
            mb.showinfo("Información", "Se borró el artículo con dicho código")
        else:
            mb.showinfo("Información", "No existe un artículo con dicho código")

    def modificar(self):
        self.pagina5 = ttk.Frame(self.notebook)
        self.notebook.add(self.pagina5, text="Modificar libro")
        self.labelframe1=ttk.LabelFrame(self.pagina5, text="Libro")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        #idLibro
        self.label1=ttk.Label(self.labelframe1, text="idLibro:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.idlibromod=tk.IntVar()
        self.entrytitulo=ttk.Entry(self.labelframe1, textvariable=self.idlibromod)
        self.entrytitulo.grid(column=1, row=0, padx=4, pady=4)

        #TITULO
        self.label1=ttk.Label(self.labelframe1, text="Titulo:")
        self.label1.grid(column=0, row=1, padx=4, pady=4)
        self.titulomod=tk.StringVar()
        self.entrytitulo=ttk.Entry(self.labelframe1, textvariable=self.titulomod)
        self.entrytitulo.grid(column=1, row=1, padx=4, pady=4)
        #NUMERO DE TOMO
        self.label1=ttk.Label(self.labelframe1, text="Numero de tomo:")
        self.label1.grid(column=0, row=2, padx=4, pady=4)
        self.numeromod=tk.IntVar()
        self.entrytomo=ttk.Entry(self.labelframe1, textvariable=self.numeromod)
        self.entrytomo.grid(column=1, row=2, padx=4, pady=4)
        #CANTIDAD DE PAGINAS
        self.label1=ttk.Label(self.labelframe1, text="Cantidad de Paginas:")
        self.label1.grid(column=0, row=3, padx=4, pady=4)
        self.paginasmod=tk.IntVar()
        self.entrytomo=ttk.Entry(self.labelframe1, textvariable=self.paginasmod)
        self.entrytomo.grid(column=1, row=3, padx=4, pady=4)
        #FECHA DE PUBLICACION
        self.label1=ttk.Label(self.labelframe1, text="Fecha de Publicacion:")
        self.label1.grid(column=0, row=4, padx=4, pady=4)
        self.fechamod=tk.StringVar()
        self.entrytomo=ttk.Entry(self.labelframe1, textvariable=self.fechamod)
        self.entrytomo.grid(column=1, row=4, padx=4, pady=4)
        #ISBN
        self.label1=ttk.Label(self.labelframe1, text="ISBN:")
        self.label1.grid(column=0, row=5, padx=4, pady=4)
        self.isbnmod=tk.StringVar()
        self.entrytomo=ttk.Entry(self.labelframe1, textvariable=self.isbnmod)
        self.entrytomo.grid(column=1, row=5, padx=4, pady=4)
        #IMAGEN
        self.label1=ttk.Label(self.labelframe1, text="Link de Imagen:")
        self.label1.grid(column=0, row=6, padx=4, pady=4)
        self.imagenmod=tk.StringVar()
        self.entrytomo=ttk.Entry(self.labelframe1, textvariable=self.imagenmod)
        self.entrytomo.grid(column=1, row=6, padx=4, pady=4)
        #LINK DESCARGA
        self.label1=ttk.Label(self.labelframe1, text="Link de Descarga:")
        self.label1.grid(column=0, row=7, padx=4, pady=4)
        self.linkmod=tk.StringVar()
        self.entrytomo=ttk.Entry(self.labelframe1, textvariable=self.linkmod)
        self.entrytomo.grid(column=1, row=7, padx=4, pady=4)

        #Codigo de Pais
        self.label1=ttk.Label(self.labelframe1, text="Codigo Pais:")
        self.label1.grid(column=0, row=8, padx=4, pady=4)
        self.paismod=tk.IntVar()
        self.entrytomo=ttk.Entry(self.labelframe1, textvariable=self.paismod)
        self.entrytomo.grid(column=1, row=8, padx=4, pady=4)
        #Editorial
        self.label1=ttk.Label(self.labelframe1, text="Editorial:")
        self.label1.grid(column=0, row=9, padx=4, pady=4)
        self.editorialmod=tk.IntVar()
        self.entrytomo=ttk.Entry(self.labelframe1, textvariable=self.editorialmod)
        self.entrytomo.grid(column=1, row=9, padx=4, pady=4)
        #Cantidad de veces pedidas
        self.label1=ttk.Label(self.labelframe1, text="Veces pedidas:")
        self.label1.grid(column=0, row=10, padx=4, pady=4)
        self.cantidad_pedidasmod=tk.IntVar()
        self.entrytomo=ttk.Entry(self.labelframe1, textvariable=self.cantidad_pedidasmod)
        self.entrytomo.grid(column=1, row=10, padx=4, pady=4)
        #Estado 0 si es prestado 1 esta en biblioteca
        self.label1=ttk.Label(self.labelframe1, text="Estado:")
        self.label1.grid(column=0, row=11, padx=4, pady=4)
        self.estadomod=tk.IntVar()
        self.entrytomo=ttk.Entry(self.labelframe1, textvariable=self.estadomod)
        self.entrytomo.grid(column=1, row=11, padx=4, pady=4)
        
        #llamada al metodo para modificar por idLibro
        self.boton1=ttk.Button(self.labelframe1, text="Consultar", command=self.consultar_mod)
        self.boton1.grid(column=2, row=0, padx=4, pady=4)

        self.boton1=ttk.Button(self.labelframe1, text="Modificar", command=self.modifica)
        self.boton1.grid(column=1, row=12, padx=4, pady=4)
    
    def modifica(self):
        datos=(self.titulomod.get(), self.numeromod.get(), self.paginasmod.get(), self.fechamod.get(), self.isbnmod.get(), self.imagenmod.get(), self.linkmod.get(), self.paismod.get(), self.editorialmod.get(), self.cantidad_pedidasmod.get(), self.estadomod.get(), self.idlibromod.get(),)
        print(f'datos 284 {datos}')
        #me aseguro que modifique algun dato del libro
        #self.conexion.modificacion(datos)
        cantidad=self.conexion.modificacion(datos)
        #type(f'tipo de cantidad{cantidad}')
        if cantidad==1:
            mb.showinfo("Información", "Se modificó el libro")
        else:
            mb.showinfo("Información", "No existe un libro con dicho titulo")
    
    def consultar_mod(self):
        datos=self.idlibromod.get()
        respuesta=self.conexion.consulta(datos)
        print(f'respuesta 305 {respuesta}')
        if len(respuesta)>0:
            self.idlibromod.set(respuesta[0][0])
            self.titulomod.set(respuesta[0][1])
            self.numeromod.set(respuesta[0][2])
            self.paginasmod.set(respuesta[0][3])
            self.fechamod.set(respuesta[0][4])
            self.isbnmod.set(respuesta[0][5])
            self.imagenmod.set(respuesta[0][6])
            self.linkmod.set(respuesta[0][7])

            self.paismod.set(respuesta[0][8])
            self.editorialmod.set(respuesta[0][9])
            self.cantidad_pedidasmod.set(respuesta[0][10])
            self.estadomod.set(respuesta[0][11])
        else:
            self.idlibromod.set('')
            self.titulomod.set('')
            self.numeromod.set('')
            self.paginasmod.set('')
            self.fechamod.set('')
            self.isbnmod.set('')
            self.imagenmod.set('')
            self.linkmod.set('')

            self.paismod.set('')
            self.editorialmod.set('')
            self.cantidad_pedidasmod.set('')
            self.estadomod.set('')
            mb.showinfo("Información", "No existe un libro con dicho titulo")


aplicacion1=FormularioBiblioteca()
