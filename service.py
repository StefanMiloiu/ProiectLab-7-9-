from domeniu.entitati import *

class ServiceStudenti:

    def __init__(self, __repo_studenti, __validator_student):
        self.__repo_studenti = __repo_studenti
        self.__validator_student = __validator_student

    def size(self):
        return len(self.__repo_studenti)

    def adauga_student(self, id_student, nume, grup):
        student = Student(id_student, nume, grup)
        self.__validator_student.valideaza(student)
        self.__repo_studenti.adauga_student(student)

    def cauta_student_dupa_id(self, id_student):
        return self.__repo_studenti.cauta_student_dupa_id(id_student)

    def modifica_student(self, id_student, nume, grup):
        student = Student(id_student, nume, grup)
        self.__validator_student.valideaza(student)
        self.__repo_studenti.modifica_student(student)

    def sterge_student_dupa_id(self, id_student):
        self.__repo_studenti.sterge_student_dupa_id(id_student)

    def get_all_studenti(self):
        return self.__repo_studenti.get_all_studenti()

class ServiceProbleme:

    def __init__(self, __repo_probleme, __validator_problema):
        self.__repo_probleme = __repo_probleme
        self.__validator_problema = __validator_problema

    def size(self):
        return len(self.__repo_probleme)

    def adauga_problema(self, Nrlab_Nrproblema, descriere, deadline):
        problema = Problema(Nrlab_Nrproblema, descriere, deadline)
        self.__validator_problema.valideazap(problema)
        self.__repo_probleme.adauga_problema(problema)

    def cauta_problema_dupa_Nrlab_Nrproblema(self, Nrlab_Nrproblema):
        return self.__repo_probleme.cauta_problema_dupa_Nrlaborator_Nrproblema(Nrlab_Nrproblema)

    def modifica_problema(self, Nrlab_Nrproblema, descriere, deadline):
        problema = Problema(Nrlab_Nrproblema, descriere, deadline)
        self.__validator_problema.valideazap(problema)
        self.__repo_probleme.modifica_problema(problema)

    def sterge_problema_dupa_Nrlab_Nrproblema(self, Nrlab_Nrproblema):
        self.__repo_probleme.sterge_student_dupa_id(Nrlab_Nrproblema)

    def get_all_probleme(self):
        return self.__repo_probleme.get_all_probleme()