from paziente import Paziente
from dottore import Dottore

class Fattura:

    def __init__(self, patient: list[Paziente], doctor: Dottore) -> None:
        self.patient: list[Paziente] = patient
        self.doctor: Dottore = doctor

        if doctor.getAge() > 30:
            self.fatture = len(self.patient)
            self.salary: int = 0
        else:
            self.patient = None
            self.doctor = None
            self.fatture = None
            self.salary = None
            print(f"Non è un dottore valido!")
    
    def getSalary(self):
        self.salary += self.doctor.getParc() * len(self.patient)
        return self.salary
    
    def getFatture(self):
        self.fatture = len(self.patient)
    
    def addPatient(self, newPatient: Paziente):
        self.patient.append(newPatient)
        self.getSalary()
        self.getFatture()
        print(f"Alla lista del Dottor {self.doctor.getLastname()} 
              è stato aggiunto il paziente {newPatient.getidCode()}")
    
    def removePatient(self, idCode: int):

        for paziente in self.patient:
            if paziente.getidCode() == idCode:
                self.patient.remove(paziente)
        self.getFatture()
        self.getSalary()
        print(f"Alla lista del Dottor {self.doctor.getLastname()} 
              è stato rimosso il paziente {paziente.getidCode()}")

