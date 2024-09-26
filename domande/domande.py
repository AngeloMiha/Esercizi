import json
import os

def quiz(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as input_file:
            def unpack(diz: dict, nQuestions, nAnswers, nMathQuestions, nSportQuestions):
                for k, v in diz.items():
                    if type(v) is dict:
                        if k == 'maths':
                            nMathQuestions += len(v)
                        elif k == 'sport':
                            nSportQuestions += len(v)
                        nQuestions, nAnswers, nMathQuestions, nSportQuestions = unpack(v, nQuestions, nAnswers, nMathQuestions, nSportQuestions) #aggiorno le vars partendo da last iteration

                    elif k == 'question':
                        nQuestions += 1
                    elif k == 'options':
                        nAnswers += len(v)
                return nQuestions, nAnswers, nMathQuestions, nSportQuestions

            s = json.load(input_file)
            if type(s) is dict:

                nQuestions, nAnswers, nMathQuestions, nSportQuestions = unpack(s, 0, 0, 0, 0) 

                if nQuestions == 0:
                    return "Errore: Nessuna domanda trovata nel questionario."

                if nQuestions > 0:
                    avg_answers = nAnswers / nQuestions
                else:
                    avg_answers = 0

                return f'Stats \nNumero Totale delle Domande: {nQuestions}\nNumero Totale delle Risposte: {nAnswers}\nNumero medio delle Risposte: {avg_answers}\nNumero delle Domande di Matematica: {nMathQuestions}\nNumero delle Domande di Sport: {nSportQuestions}'
    else:
        return False

print(quiz('quiz.json'))