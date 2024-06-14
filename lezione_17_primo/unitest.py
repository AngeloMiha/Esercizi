import unittest
from persona import Persona
from dottore import Dottore
from paziente import Paziente
from fattura import Fattura

class TestPersona(unittest.TestCase):
    def setUp(self):
        self.persona = Persona("Mario", "Rossi")

    def test_initialization(self):
        self.assertEqual(self.persona.getName(), "Mario")
        self.assertEqual(self.persona.getLastname(), "Rossi")
        self.assertEqual(self.persona.getAge(), 0)

    def test_setName(self):
        self.persona.setName("Luigi")
        self.assertEqual(self.persona.getName(), "Luigi")

    def test_setLastName(self):
        self.persona.setLastName("Bianchi")
        self.assertEqual(self.persona.getLastname(), "Bianchi")

    def test_setAge(self):
        self.persona.setAge(30)
        self.assertEqual(self.persona.getAge(), 30)

class TestDottore(unittest.TestCase):
    def setUp(self):
        self.dottore = Dottore("Anna", "Verdi", "Cardiologia", 150, 35)

    def test_initialization(self):
        self.assertEqual(self.dottore.getName(), "Anna")
        self.assertEqual(self.dottore.getLastname(), "Verdi")
        self.assertEqual(self.dottore.setSpec, "Cardiologia")
        self.assertEqual(self.dottore.getParc(), 150)
        self.assertEqual(self.dottore.getSpec(), 35)

    def test_isValidDoctor(self):
        self.assertTrue(self.dottore.isAValidDoctor())
        self.dottore.setAge(25)
        self.assertFalse(self.dottore.isAValidDoctor())

class TestPaziente(unittest.TestCase):
    def setUp(self):
        self.paziente = Paziente("Giorgio", "Neri", "P123")

    def test_initialization(self):
        self.assertEqual(self.paziente.getName(), "Giorgio")
        self.assertEqual(self.paziente.getLastname(), "Neri")
        self.assertEqual(self.paziente.getidCode, "P123")
        self.assertEqual(self.paziente.getAge(), 0)

class TestFattura(unittest.TestCase):
    def setUp(self):
        self.dottore = Dottore("Anna", "Verdi", "Cardiologia", 150, 35)
        self.pazienti = [
            Paziente("Giorgio", "Neri", "P123"),
            Paziente("Maria", "Bianchi", "P124")
        ]
        self.fattura = Fattura(self.dottore, self.pazienti)

    def test_initialization(self):
        self.assertEqual(self.fattura.doctor, self.dottore)
        self.assertEqual(self.fattura.patient, self.pazienti)
        self.assertEqual(self.fattura.getSalary(), 300)

    def test_calculateTotalFee(self):
        self.assertEqual(self.fattura.getSalary, 300)
        self.fattura.patient.append(Paziente("Luigi", "Rossi", "P125"))
        self.assertEqual(self.fattura.getSalary, 450)

    def test_addPatient(self):
        new_patient = Paziente("Luigi", "Rossi", "P125")
        self.fattura.addPatient(new_patient)
        self.assertIn(new_patient, self.fattura.patient)
        self.assertEqual(self.fattura.getSalary(), 450)

    def test_removePatient(self):
        patient_to_remove = self.pazienti[0]
        self.fattura.removePatient(patient_to_remove)
        self.assertNotIn(patient_to_remove, self.fattura.patient)
        self.assertEqual(self.fattura.getSalary(), 150)

if __name__ == '__main__':
    unittest.main()
