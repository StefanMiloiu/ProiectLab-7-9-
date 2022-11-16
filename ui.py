from exceptie.exceptie import RepoError, ValidationError, RepoErrorProblema, ValidationErrorProblema


class UI(object):

    def __init__(self, service_student, service_problema):
        self.__service_student = service_student
        self.__service_problema = service_problema
        self.__comenzi = {
            "adauga_student":self.__ui_adauga_student,
            "adauga_problema":self.__ui_adauga_problema,
            "print_studenti":self.__ui_print_studenti,
            "print_probleme":self.__ui_print_problema,
            "modifica_student":self.__ui_modifica_student,
            "modifica_problema":self.__ui_modifica_problema,
            "cauta_student_id":self.__ui_cauta_student_id
            #"cauta_problema":self.__ui_cauta_dupa_nrlab_nrproblema
        }

    def __ui_adauga_student(self):
        if len(self.__params)!=3:
            print("numar parametri invalid!")
            return
        id_student = int(self.__params[0])
        nume = self.__params[1]
        grup = int(self.__params[2])
        self.__service_student.adauga_student(id_student, nume, grup)
        print("studentul a fost adaugat cu succes")

    def __ui_adauga_problema(self):
        if len(self.__params)!=3:
            print("numar parametri invalid!")
            return
        Nrlab_Nrproblema = int(self.__params[0])
        descreire = self.__params[1]
        deadline = int(self.__params[2])
        self.__service_problema.adauga_problema(Nrlab_Nrproblema,descreire, deadline)
        print("problema a fost adaugata cu succes")

    def __ui_print_studenti(self):
        if len(self.__params)!=0:
            print("numar parametri invalid!")
            return
        studenti = self.__service_student.get_all_studenti()
        if len(studenti)==0:
            print("nu exista studenti inregistrati")
            return
        for student in studenti:
            print(f"{student}\n{studenti[student.get_id_student()]}")

    def __ui_print_problema(self):
        if len(self.__params)!=0:
            print("numar parametri invalid!")
            return
        probleme = self.__service_problema.get_all_probleme()
        if len(probleme) == 0:
            print("nu exista studenti inregistrati")
            return
        for problema in probleme:
            print(f"{problema}\n")

    def __ui_modifica_student(self):
        if len(self.__params) != 3:
            print("numar parametri invalid!")
            return
        id_student = int(self.__params[0])
        nume = self.__params[1]
        grup = int(self.__params[2])
        self.__service_student.modifica_student(id_student, nume, grup)

    def __ui_modifica_problema(self):
        if len(self.__params) != 3:
            print("numar parametri invalid!")
            return
        Nrlab_Nrproblema = int(self.__params[0])
        descriere = self.__params[1]
        deadline = int(self.__params[2])
        self.__service_problema.modifica_problema(Nrlab_Nrproblema, descriere, deadline)

    def __ui_cauta_student_id(self):
        if len(self.__params) != 1:
            print("numar parametri invalid!")
            return
        id_student = self.__params[0]
        print(self.__service_student.cauta_student_dupa_id(id_student))
        
    def __ui_cauta_dupa_nrlab_nrproblema(self):
        if len(self.__params) != 1:
            print("numar parametri invalid!")
            return
        Nrlab_Nrproblema = int(self.__params[0])
        print(self.__service_problema.cauta_problema_dupa_Nrlab_Nrproblema(Nrlab_Nrproblema))

    def run(self):
         while True:
            print("\n--------------------------------------------")
            print("Type [print_studenti] for Printing students")
            print("Type [print_probleme] for Printing problems")
            print("Type [adauga_studenti ID, Nume, Grup] for Adding a student")
            print("Type [adauga_problema Nrlaborator_Nrproblema, Descriere, deadline] for Adding a problem")
            print("Type [modifica_student ID, Nume, Grup] for Modifying a student")
            print("--------------------------------------------")
            comanda = input(">>>")
            comanda = comanda.strip()
            if comanda == "":
                continue
            if comanda == "exit":
                return
            parti = comanda.split()
            nume_comanda = parti[0]
            self.__params = parti[1:]
            if nume_comanda in self.__comenzi:
                try:
                    self.__comenzi[nume_comanda]()
                except ValueError as ve:
                    print(ve)
                except ValidationError as ve:
                    print(ve)
                except ValidationErrorProblema as ve:
                    print(ve)
                except RepoError as re:
                    print(re)
                except RepoErrorProblema as re:
                    print(re)
            else:
                print("comanda invalida!")
