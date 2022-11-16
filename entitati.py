class Student(object):

    def __init__(self, id_student, nume, grup):
        self.__id_student = id_student
        self.__nume = nume
        self.__grup = grup

    def get_id_student(self):
        return self.__id_student

    def get_nume_student(self):
        return self.__nume

    def get_grup_student(self):
        return self.__grup

    def set_nume_student(self, value):
        self.__nume = value

    def __eq__(self, other):
        return self.__id_student == other.__id_student

    def __str__(self):
        return f"ID: {self.__id_student}\nNume: {self.__nume}\nGrup: {self.__grup}"

class Problema(object):

    def __init__(self, Nrlaborator_Nrproblema, descriere, deadline):
        self.__Nrlaborator_Nrproblema = Nrlaborator_Nrproblema
        self.__descriere = descriere
        self.__deadline = deadline

    def get_Nrlaborator_Nrproblema(self):
        return self.__Nrlaborator_Nrproblema

    def get_descriere(self):
        return self.__descriere

    def get_deadline(self):
        return self.__deadline

    def get_zi_deadline(self): # 12 12 2022
        return self.__deadline // 1000000

    def get_luna_deadline(self): # 12 11 2022
        return (self.__deadline // 10000) % 100

    def get_an_deadline(self):
        return self.__deadline % 10000

    def __str__(self):
        return f"NrLab_NrProblema: {self.__Nrlaborator_Nrproblema // 10}_{self.__Nrlaborator_Nrproblema % 10}\nDescriere: {self.__descriere}\nDeadline: {self.__deadline}"


