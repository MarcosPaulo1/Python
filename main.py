from defs import Usuarios
import tkinter as tk
from tkinter.messagebox import showwarning
from tkinter import *

class Application:

    #def naoNulo(entrada):
    #    if len(str(entrada)) == 0:
    #        print("Você precisa inserir todos os dados!!!")
    #    else:
    #        return entrada
    
    
    def inserirMateria(self):
        user = Usuarios()
        if self.txtnome_materia.get() == "" or self.txtdia_horario_materia.get() == "" or self.txtcampus_materia.get() == '' or self.txtprofessor_materia.get() == '' or self.txtnota_av1.get() == '' or self.txtnota_av2.get() == '' or self.txtnota_avd.get() == '' or self.txtnota_avds.get() == '':
            resultado = showwarning("Erro", "Por favor, digite todos os  campos.")
        else:
            user.nome_materia = self.txtnome_materia.get()
            user.dia_horario_materia = self.txtdia_horario_materia.get()
            user.campus_materia = self.txtcampus_materia.get()
            user.professor_materia = self.txtprofessor_materia.get()
            user.nota_av1 = self.txtnota_av1.get()
            user.nota_av2 = self.txtnota_av2.get()
            user.nota_avd = self.txtnota_avd.get()
            user.nota_avds = self.txtnota_avds.get()

        self.lblmsg["text"] = user.insertUser()

        self.txtidMateria.delete(0, END)
        self.txtnome_materia.delete(0, END)
        self.txtdia_horario_materia.delete(0, END)
        self.txtcampus_materia.delete(0, END)
        self.txtprofessor_materia.delete(0, END)
        self.txtnota_av1.delete(0, END)
        self.txtnota_av2.delete(0, END)
        self.txtnota_avd.delete(0, END)
        self.txtnota_avds.delete(0, END)


    def alterarMateria(self):
        user = Usuarios()

        user.idMateria = self.txtidMateria.get()
        user.nome_materia = self.txtnome_materia.get()
        user.dia_horario_materia = self.txtdia_horario_materia.get()
        user.campus_materia = self.txtcampus_materia.get()
        user.professor_materia = self.txtprofessor_materia.get()
        user.nota_av1 = self.txtnota_av1.get()
        user.nota_av2 = self.txtnota_av2.get()
        user.nota_avd = self.txtnota_avd.get()
        user.nota_avds = self.txtnota_avds.get()

        self.lblmsg["text"] = user.updateUser()

        self.txtidMateria.delete(0, END)
        self.txtnome_materia.delete(0, END)
        self.txtdia_horario_materia.delete(0, END)
        self.txtcampus_materia.delete(0, END)
        self.txtprofessor_materia.delete(0, END)
        self.txtnota_av1.delete(0, END)
        self.txtnota_av2.delete(0, END)
        self.txtnota_avd.delete(0, END)
        self.txtnota_avds.delete(0, END)   



    def excluirMateria(self):
        user = Usuarios()

        user.idMateria = self.txtidMateria.get()

        self.lblmsg["text"] = user.deleteUser()

        self.txtidMateria.delete(0, END)
        self.txtnome_materia.delete(0, END)
        self.txtdia_horario_materia.delete(0, END)
        self.txtcampus_materia.delete(0, END)
        self.txtprofessor_materia.delete(0, END)
        self.txtnota_av1.delete(0, END)
        self.txtnota_av2.delete(0, END)
        self.txtnota_avd.delete(0, END)
        self.txtnota_avds.delete(0, END)


    def buscarMateria(self):
        user = Usuarios()

        idMateria = self.txtidMateria.get()

        self.lblmsg["text"] = user.selectUser(idMateria)

        self.txtidMateria.delete(0, END)
        self.txtidMateria.insert(INSERT, user.idMateria)

        self.txtnome_materia.delete(0, END)
        self.txtnome_materia.insert(INSERT, user.nome_materia)

        self.txtdia_horario_materia.delete(0, END)
        self.txtdia_horario_materia.insert(INSERT,user.dia_horario_materia)

        self.txtcampus_materia.delete(0, END)
        self.txtcampus_materia.insert(INSERT, user.campus_materia)

        self.txtprofessor_materia.delete(0, END)
        self.txtprofessor_materia.insert(INSERT, user.professor_materia)

        self.txtnota_av1.delete(0, END)
        self.txtnota_av1.insert(INSERT,user.nota_av1)

        self.txtnota_av2.delete(0, END)
        self.txtnota_av2.insert(INSERT,user.nota_av2)

        self.txtnota_avd.delete(0, END)
        self.txtnota_avd.insert(INSERT,user.nota_avd)

        self.txtnota_avds.delete(0, END)
        self.txtnota_avds.insert(INSERT,user.nota_avds)

    def __init__(self, master=None):
        self.fonte = ("Arial", "8")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 5
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["padx"] = 20
        self.container9["pady"] = 5
        self.container9.pack()
        self.container10 = Frame(master)
        self.container10["padx"] = 20
        self.container10["pady"] = 5
        self.container10.pack()
        self.container11 = Frame(master)
        self.container11["padx"] = 20
        self.container11["pady"] = 10
        self.container11.pack()
        self.container12 = Frame(master)
        self.container12["pady"] = 15
        self.container12.pack()

        self.titulo = Label(self.container1, text="Informe os dados :")
        self.titulo["font"] = ("Arial", "9", "bold")
        self.titulo.pack ()


        self.lblidMateria = Label(self.container2,
        text="idMateria:", font=self.fonte, width=10)
        self.lblidMateria.pack(side=LEFT)

        self.txtidMateria = Entry(self.container2)
        self.txtidMateria["width"] = 10
        self.txtidMateria["font"] = self.fonte
        self.txtidMateria.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar",font=self.fonte, width=10)
        
        self.btnBuscar["command"] = self.buscarMateria
        self.btnBuscar.pack(side=RIGHT)
        self.lblnome_materia = Label(self.container3, text="Nome da matéria:",font=self.fonte, width=14)
        self.lblnome_materia.pack(side=LEFT)

        self.txtnome_materia = Entry(self.container3)
        self.txtnome_materia["width"] = 20
        self.txtnome_materia["font"] = self.fonte
        self.txtnome_materia.pack(side=LEFT)

        self.lbldia_horario_materia = Label(self.container4, text="Dia e horario da matéria:",font=self.fonte, width=20)
        self.lbldia_horario_materia.pack(side=LEFT)

        self.txtdia_horario_materia = Entry(self.container4)
        self.txtdia_horario_materia["width"] = 20
        self.txtdia_horario_materia["font"] = self.fonte
        self.txtdia_horario_materia.pack(side=LEFT)

        self.lblcampus_materia= Label(self.container5, text="Campus da matéria",font=self.fonte, width=16)
        self.lblcampus_materia.pack(side=LEFT)

        self.txtcampus_materia = Entry(self.container5)
        self.txtcampus_materia["width"] = 20
        self.txtcampus_materia["font"] = self.fonte
        self.txtcampus_materia.pack(side=LEFT)

        self.lblprofessor_materia= Label(self.container6, text="Professor da matéria:",font=self.fonte, width=14)
        self.lblprofessor_materia.pack(side=LEFT)

        self.txtprofessor_materia = Entry(self.container6)
        self.txtprofessor_materia["width"] = 20
        self.txtprofessor_materia["font"] = self.fonte
        self.txtprofessor_materia.pack(side=LEFT)

        self.lblnota_av1= Label(self.container7, text="Nota av1",font=self.fonte, width=14)
        self.lblnota_av1.pack(side=LEFT)

        self.txtnota_av1 = Entry(self.container7)
        self.txtnota_av1["width"] = 20
        self.txtnota_av1["font"] = self.fonte
        self.txtnota_av1.pack(side=LEFT)

        self.lblnota_av2= Label(self.container8, text="Nota av2",font=self.fonte, width=14)
        self.lblnota_av2.pack(side=LEFT)

        self.txtnota_av2 = Entry(self.container8)
        self.txtnota_av2["width"] = 20
        self.txtnota_av2["font"] = self.fonte
        self.txtnota_av2.pack(side=LEFT)


        self.lblnota_avd = Label(self.container9, text="Nota avd:",font=self.fonte, width=14)
        self.lblnota_avd.pack(side=LEFT)

        self.txtnota_avd = Entry(self.container9)
        self.txtnota_avd["width"] = 20
        self.txtnota_avd["font"] = self.fonte
        self.txtnota_avd.pack(side=LEFT)

        self.lblnota_avds = Label(self.container10, text="Nota avds:",font=self.fonte, width=14)
        self.lblnota_avds.pack(side=LEFT)

        self.txtnota_avds = Entry(self.container10)
        self.txtnota_avds["width"] = 20
        self.txtnota_avds["font"] = self.fonte
        self.txtnota_avds.pack(side=LEFT)



        self.bntInsert = Button(self.container11, text="Inserir", font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirMateria
        self.bntInsert.pack (side=LEFT)

        self.bntAlterar = Button(self.container11, text="Alterar",font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarMateria
        self.bntAlterar.pack (side=LEFT)

        self.bntExcluir = Button(self.container11, text="Excluir",font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirMateria
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container12, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()




root = Tk()
Application(root)
root.mainloop()