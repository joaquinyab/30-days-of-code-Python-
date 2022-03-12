class Person:
  def __init__(self, firstName, lastName, idNumber):
    self.firstName = firstName
    self.lastName = lastName
    self.idNumber = idNumber


  def printPerson(self):
    print("Name:", self.lastName + ",", self.firstName)
    print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = map(int,scores)

    def calculate(self):

          x = len(scores)
          n = 0
          for i in range(x):
            n +=scores[i]

          y = int(n)//int(x)

          if 90 <= y <= 100:
              return"O"
          elif 80 <= y <= 90:
              return"E"
          elif 70 <= y <= 80:
              return"A"
          elif 55 <= y <= 70:
              return"P"
          elif 40 <= y < 55:
            return 'D'
          else:
            return 'T'


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
