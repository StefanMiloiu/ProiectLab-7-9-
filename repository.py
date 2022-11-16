from exceptie.exceptie import RepoError, RepoErrorProblema
from domeniu.entitati import *

class RepoStudenti(object):

    def __init__(self):
        self.__studenti = {}

    def __len__(self):
        return len(self.__studenti)

    def adauga_student(self, student):
        if student.get_id_student() in self.__studenti:
            raise RepoError("student existent!")
        self.__studenti[student.get_id_student()]=student

    def cauta_student_dupa_id(self, id_student):
        if id_student not in self.__studenti:
            raise RepoError("student inexistent!")
        return self.__studenti[id_student]

    def modifica_student(self, student):
        if student.get_id_student() not in self.__studenti:
            raise RepoError("student inexistent!")
        self.__studenti[student.get_id_student()] = student

    def get_all_studenti(self):
        r = []
        for id_student in self.__studenti:
            student = self.__studenti[id_student]
            r.append(student)
        return r

    def sterge_student_dupa_id(self, id_student):
        if id_student not in self.__studenti:
            raise RepoError("student inexistent")
        del self.__studenti[id_student]

class RepoProblema(object):

    def __init__(self):
        self.__probleme = {}

    def __len__(self):
        return len(self.__probleme)

    def adauga_problema(self, problema):
        if problema.get_Nrlaborator_Nrproblema() in self.__probleme:
            raise RepoErrorProblema("problema existenta!")
        self.__probleme[problema.get_Nrlaborator_Nrproblema]=problema

    def cauta_problema_dupa_Nrlaborator_Nrproblema(self, Nrlaborator_Nrproblema):
        if Nrlaborator_Nrproblema not in self.__probleme:
            raise RepoErrorProblema("problema inexistenta!")
        return self.__probleme[Nrlaborator_Nrproblema]

    def modifica_problema(self, problema):
        if problema.get_Nrlaborator_Nrproblema() not in self.__probleme:
            raise RepoErrorProblema("problema inexistenta!")
        self.__probleme[problema.get_Nrlaborator_Nrproblema()] = problema

    def get_all_probleme(self):
        r = []
        for Nrlab_Nrproblema in self.__probleme:
            problema = self.__probleme[Nrlab_Nrproblema]
            r.append(problema)
        return r

    def sterge_problema_dupa_Nrlab_Nrproblema(self, Nrlab_Nrproblema):
        if Nrlab_Nrproblema not in self.__probleme:
            raise RepoErrorProblema("problema inexistenta!")
        del self.__probleme[Nrlab_Nrproblema]