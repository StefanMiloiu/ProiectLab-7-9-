from bussines.service import ServiceStudenti
from domeniu.entitati import Student, Problema
from validare.validare import ValidatorStudent, ValidatorProblema
from exceptie.exceptie import ValidationError, RepoError, ValidationErrorProblema
from infrastructura.repository import RepoStudenti, RepoProblema


class Teste(object):

    def __init__(self):
        self.__id_student = 23
        self.__nume = "Jordan"
        self.__grup = 214
        self.__eps = 0.00001
        self.__student = Student(self.__id_student, self.__nume, self.__grup)
        self.__Nrlaborator_Nrproblema = 12
        self.__descriere = "Scrieti un program de gestionare a calatoriiloe"
        self.__deadline = 12122023
        self.__problema = Problema(self.__Nrlaborator_Nrproblema, self.__descriere, self.__deadline)

    def ruleaza_toate_testele(self):
        self.__ruleaza_teste_domeniu()
        print("\nteste domeniu terminate cu succes")
        self.__ruleaza_teste_validare()
        print("teste validare terminate cu succes")
        self.__ruleaza_teste_repo()
        print("teste repo terminate cu succes")
        self.__ruleaza_teste_service_studenti()
        print("teste service terminate cu succes")

    def __ruleaza_teste_domeniu(self):
        #STUDENT
        assert (self.__student.get_id_student()==self.__id_student)
        assert (self.__student.get_nume_student()==self.__nume)
        clona_student=Student(self.__id_student, None, None)
        assert (self.__student==clona_student)
        assert (self.__student.__eq__(clona_student))

        #PROBLEMA
        assert(self.__problema.get_Nrlaborator_Nrproblema() == self.__Nrlaborator_Nrproblema)
        assert(self.__problema.get_deadline() == self.__deadline)
        assert(self.__problema.get_descriere() == self.__descriere)

    def __ruleaza_teste_validare(self):
        #STUDENT
        self.__validator_student=ValidatorStudent()
        self.__validator_student.valideaza(self.__student)
        self.__id_student_invalid = -23
        self.__nume_invalid = ""
        self.__grup_invalid = 0
        self.__student_invalid = Student(self.__id_student_invalid, self.__nume_invalid, self.__grup_invalid)
        try:
            self.__validator_student.valideaza(self.__student_invalid)
            assert False
        except ValidationError as ve:
            assert (str(ve)=="id invalid!\nnume invalid!\ngrup invalid!\n")

        #PROBLEMA
        self.__validator_problema = ValidatorProblema()
        self.__validator_problema.valideazap(self.__problema)
        self.__Nrlaborator_Nrproblema_invalid = 0
        self.__descriere_invalida = ""
        self.__deadline_invalid = 0
        self.__problema_invalida = Problema(self.__Nrlaborator_Nrproblema_invalid, self.__descriere_invalida, self.__deadline_invalid)
        try:
            self.__validator_problema.valideazap(self.__problema_invalida)
            assert False
        except ValidationErrorProblema as ve:
            assert (str(ve) == "Nrlaborator_Nrproblema invalid!\ndescriere invalida!\ndeadline invalid!\n")

    def __ruleaza_teste_repo(self):
        #STUDENTI
        self.__repo_studenti = RepoStudenti()
        assert (len(self.__repo_studenti) == 0)
        self.__repo_studenti.adauga_student(self.__student)
        assert (len(self.__repo_studenti) == 1)
        student_gasit = self.__repo_studenti.cauta_student_dupa_id(self.__id_student)
        assert (student_gasit.get_nume_student() == self.__student.get_nume_student())
        try:
            self.__repo_studenti.adauga_student(self.__student)
            assert False
        except RepoError as re:
            assert (str(re) == "student existent!")
        self.__id_student_inexistent = 24

        try:
            self.__repo_studenti.cauta_student_dupa_id(self.__id_student_inexistent)
            assert False
        except RepoError as re:
            assert (str(re) == "student inexistent!")
        self.__nume_nou = "Gigel"
        self.__grup_nou = 5
        self.__student_modificat = Student(self.__id_student, self.__nume_nou, self.__grup_nou)
        self.__repo_studenti.modifica_student(self.__student_modificat)
        assert (len(self.__repo_studenti) == 1)
        student_gasit = self.__repo_studenti.cauta_student_dupa_id(self.__id_student)
        assert (student_gasit.get_nume_student() == self.__nume_nou)
        self.__student_inexistent = Student(self.__id_student_inexistent, None, None)
        try:
            self.__repo_studenti.modifica_student(self.__student_inexistent)
            assert False
        except RepoError as re:
            assert (str(re) == "student inexistent!")
        self.__alt_student = Student(self.__id_student_inexistent, self.__nume_nou, self.__grup_nou)
        self.__repo_studenti.adauga_student(self.__alt_student)
        assert (len(self.__repo_studenti) == 2)
        studenti = self.__repo_studenti.get_all_studenti()
        assert (len(studenti) == 2)
        self.__repo_studenti.sterge_student_dupa_id(self.__id_student)
        assert (len(self.__repo_studenti) == 1)
        try:
            self.__repo_studenti.sterge_student_dupa_id(self.__id_student)
            assert False
        except RepoError as re:
            assert (str(re) == "student inexistent")

        #PROBLEME
        self.__repo_probleme = RepoProblema()
        assert(len(self.__repo_probleme) == 0)
        self.__repo_probleme.adauga_problema(self.__problema)
        assert(len(self.__repo_probleme) == 1)
        assert (self.__Nrlaborator_Nrproblema == self.__problema.get_Nrlaborator_Nrproblema())
        #problema_gasita = self.__repo_probleme.cauta_problema_dupa_Nrlaborator_Nrproblema(self.__Nrlaborator_Nrproblema)

    def __ruleaza_teste_service_studenti(self):
        #folosim injectarea de dependenta
        #pentru a functiona ServiceStudenti are nevoie de un obiect
        #de tipul RepoStudenti primit prin referinta din constructor

        self.__repo_studenti = RepoStudenti()
        self.__service_studenti = ServiceStudenti(self.__repo_studenti, self.__validator_student)
        assert (self.__service_studenti.size()==0)
        self.__service_studenti.adauga_student(self.__id_student, self.__nume, self.__grup)
        assert (self.__service_studenti.size()==1)
        student_gasit = self.__service_studenti.cauta_student_dupa_id(self.__id_student)
        assert (student_gasit.get_nume_student() == self.__nume)
        try:
            self.__service_studenti.adauga_student(self.__id_student, None, 23)
            assert False
        except RepoError as re:
            assert (str(re)=="student existent!")
        try:
            self.__service_studenti.cauta_student_dupa_id(self.__id_student_inexistent)
            assert False
        except RepoError as re:
            assert (str(re)=="student inexistent!")
        try:
            self.__service_studenti.adauga_student(self.__id_student_invalid, self.__nume_invalid, self.__grup_invalid)
            assert False
        except ValidationError as ve:
            assert (str(ve)=="id invalid!\nnume invalid!\ngrup invalid!\n")
        try:
            self.__service_studenti.modifica_student(self.__id_student_inexistent, None, 23)
            assert False
        except RepoError as re:
            assert (str(re)=="student inexistent!")
        self.__service_studenti.modifica_student(self.__id_student, self.__nume_nou, self.__grup_nou)
        student_gasit = self.__service_studenti.cauta_student_dupa_id(self.__id_student)
        assert (student_gasit.get_nume_student()==self.__nume_nou)
        try:
            self.__service_studenti.sterge_student_dupa_id(self.__id_student_inexistent)
            assert False
        except RepoError as re:
            assert (str(re)=="student inexistent")
        self.__service_studenti.sterge_student_dupa_id(self.__id_student)
        assert (self.__service_studenti)







