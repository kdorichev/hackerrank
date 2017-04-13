""" https://www.hackerrank.com/challenges/30-inheritance
Sample input:

Heraldo Memelli 8135627
2
100 80
"""
class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    def calculate(self):
        avrg = sum(self.scores)/len(self.scores)
        if avrg < 40:
            return 'T'
        elif avrg <55:
            return 'D'
        elif avrg <70:
            return 'P'
        elif avrg <80:
            return 'A'
        elif avrg <90:
            return 'E'
        elif avrg <=100:
            return 'O'

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
