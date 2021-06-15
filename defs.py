from banco import Banco

#def adiciona_materias():
    #materias = []
    #nome_materia = input('Digite o nome da matéria\n')
    #dia_horario_materia = input('Digite o dia da semana e horário da máteria\n)')
    #campus_materia = input('Digite o local onde ocorrerá a aula ')
    #professor_materia = input("Digite o nome do professor que dará a matéria ")
    #materias.append((nome_materia, dia_horario_materia, professor_materia))
    #cursor.executemany("""INSERT INTO materias (nome_materia, dia_horario_materia, campus_materia, professor_materia) VALUES (?,?,?) """, materias)
    
    #conn.commit()
class Usuarios(object):


    def __init__(self, idMateria = 0, nome_materia = "", dia_horario_materia = "", campus_materia = "", professor_materia = "", nota_av1 = "", nota_av2 = "", nota_avd = "", nota_avds = ""):
        self.info = {}
        self.idMateria = idMateria
        self.nome_materia = nome_materia
        self.dia_horario_materia = dia_horario_materia
        self.campus_materia = campus_materia
        self.professor_materia = professor_materia
        self.nota_av1 = nota_av1
        self.nota_av2 = nota_av2
        self.nota_avd = nota_avd
        self.nota_avds = nota_avds


    def insertUser(self):

        banco = Banco()
        try:
            cursor = banco.conn.cursor()

            cursor.execute("insert into materias (nome_materia, dia_horario_materia, campus_materia, professor_materia, nota_av1, nota_av2, nota_avd, nota_avds) values ('" + self.nome_materia + "', '" + self.dia_horario_materia + "', '" + self.campus_materia + "', '" + self.professor_materia + "', '" + self.nota_av1 + "', '" +  self.nota_av2 + "', '" +  self.nota_avd + "', '" +  self.nota_avds + "' )")

            banco.conn.commit()
            cursor.close()
            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário"
           

    def updateUser(self):

        banco = Banco()
        try:

            cursor = banco.conn.cursor()

            cursor.execute("update materias set nome_materia = '" + self.nome_materia + "',dia_horario_materia = '" + self.dia_horario_materia + "', campus_materia = '" + self.campus_materia +"', professor_materia = '" + self.professor_materia + "', nota_av1 = '" + self.nota_av1 + "', nota_av2 = '" + self.nota_av2 + "', nota_avd = '" + self.nota_avd + "', nota_avds = '" + self.nota_avds +"' where idMateria = " + self.idMateria + " ")

            banco.conn.commit()
            cursor.close()

            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"

    def deleteUser(self):

        banco = Banco()
        try:

            cursor = banco.conn.cursor()

            cursor.execute("delete from materias where idMateria = " + self.idMateria + " ")

            banco.conn.commit()
            cursor.close()

            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"

    def selectUser(self, idMateria):
        banco = Banco()
        try:

            cursor = banco.conn.cursor()

            cursor.execute("select * from materias where idMateria = " + idMateria + "  ")

            for linha in cursor:
                self.idMateria = linha[0]
                self.nome_materia = linha[1]
                self.dia_horario_materia = linha[2]
                self.campus_materia = linha[3]
                self.professor_materia = linha[4]
                self.nota_av1 = linha[5]
                self.nota_av2 = linha[6]
                self.nota_avd = linha[7]
                self.nota_avds = linha[8]

            cursor.close()

            return "Usuário encontrado!"
        except:
            return "Ocorreu um erro na busca do usuário"

