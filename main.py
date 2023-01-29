from enum import Enum
import random
import csv

class Question:

    def __init__(self, question, ans_true, ans2, ans3, ans4):
        self.question = question;
        self.ans_true = ans_true;
        self.answers = [ans_true, ans2, ans3, ans4]
        random.shuffle(self.answers)

    def is_ok(self, answer):
        return answer == self.ans_true;

    def is_ok_index(self, answers):
        for i in range(len(answers)):
            if (self.is_ok(answers[i])):
                return i

class Questions():

    def __init__(self):
        file = open('choices2.csv')
        csvreader = csv.reader(file)
        next(csvreader)
        self.questions = []
        for row in csvreader:
            self.questions.append(
                Question(row[0], row[1], row[2], row[3], row[4])
            )
        random.shuffle(self.questions)


def main():
    for q in Questions().questions:
        answers = q.answers
        print(q.question)

        for i in range(len(answers)):
            print(str((i+1)) + ": " + answers[i])

        opt = int(input("Elegi una opcion: "))

        if (q.is_ok(answers[opt-1])):
            print("====> OK\n\n")
        else:
            print("====> ERROR! Era la " + str(q.is_ok_index(answers) + 1) + "\n\n")
    return 0

if __name__ == '__main__':
    main()