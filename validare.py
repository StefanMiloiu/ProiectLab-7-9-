from exceptie.exceptie import ValidationError, ValidationErrorProblema


class ValidatorStudent(object):

    def valideaza(self, student):
        erori = ""
        if student.get_id_student()<0:
            erori += "id invalid!\n"
        if student.get_nume_student() == "":
            erori += "nume invalid!\n"
        if student.get_grup_student()<=0:
            erori += "grup invalid!\n"

        if len(erori)>0:
            raise ValidationError(erori)

class ValidatorProblema(object):

    def valideazap(self, problema):
        erori = ""
        if problema.get_Nrlaborator_Nrproblema() <= 0:
            erori += "Nrlaborator_Nrproblema invalid!\n"
        if problema.get_descriere() == "":
            erori += "descriere invalida!\n"
        if problema.get_deadline() <= 0:
            erori += "deadline invalid!\n"

        if len(erori) > 0:
            raise ValidationErrorProblema(erori)