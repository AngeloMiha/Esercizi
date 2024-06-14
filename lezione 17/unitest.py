import unittest
from persona import Persona
from dottore import Dottore
from paziente import Paziente
from fattura import Fattura

class TestPersona(unittest.TestCase):
    def setUp(self):
        self.persona = Persona("Mario", "Rossi")

    def test_initialization(self):
        self.assertEqual(self.persona.first_name, "Mario")
        self.assertEqual(self.persona.last_name, "Rossi")
        self.assertEqual(self.persona.age, 0)

    def test_setName(self):
        self.persona.setName("Luigi")
        self.assertEqual(self.persona.first_name, "Luigi")

    def test_setLastName(self):
        self.persona.setLastName("Bianchi")
        self.assertEqual(self.persona.last_name, "Bianchi")

    def test_setAge(self):
        self.persona.setAge(30)
        self.assertEqual(self.persona.age, 30)

class TestDottore(unittest.TestCase):
    def setUp(self):
        self.dottore = Dottore("Anna", "Verdi", "Cardiologia", 150, 35)

    def test_initialization(self):
        self.assertEqual(self.dottore.first_name, "Anna")
        self.assertEqual(self.dottore.last_name, "Verdi")
        self.assertEqual(self.dottore.specialization, "Cardiologia")
        self.assertEqual(self.dottore.fee, 150)
        self.assertEqual(self.dottore.age, 35)

    def test_isValidDoctor(self):
        self.assertTrue(self.dottore.isValidDoctor())
        self.dottore.setAge(25)
        self.assertFalse(self.dottore.isValidDoctor())

class TestPaziente(unittest.TestCase):
    def setUp(self):
        self.paziente = Paziente("Giorgio", "Neri", "P123")

    def test_initialization(self):
        self.assertEqual(self.paziente.first_name, "Giorgio")
        self.assertEqual(self.paziente.last_name, "Neri")
        self.assertEqual(self.paziente.patient_id, "P123")
        self.assertEqual(self.paziente.age, 0)

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
        self.assertEqual(self.fattura.patients, self.pazienti)
        self.assertEqual(self.fattura.total_fee, 300)

    def test_calculateTotalFee(self):
        self.assertEqual(self.fattura.calculateTotalFee(), 300)
        self.fattura.patients.append(Paziente("Luigi", "Rossi", "P125"))
        self.assertEqual(self.fattura.calculateTotalFee(), 450)

    def test_addPatient(self):
        new_patient = Paziente("Luigi", "Rossi", "P125")
        self.fattura.addPatient(new_patient)
        self.assertIn(new_patient, self.fattura.patients)
        self.assertEqual(self.fattura.total_fee, 450)

    def test_removePatient(self):
        patient_to_remove = self.pazienti[0]
        self.fattura.removePatient(patient_to_remove)
        self.assertNotIn(patient_to_remove, self.fattura.patients)
        self.assertEqual(self.fattura.total_fee, 150)

if __name__ == '__main__':
    unittest.main()
