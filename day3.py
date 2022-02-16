number = int(input())

if 1<=number and number<=100:
  if number % 2 !=0:
    print("Weird")

  elif 2<=number and number <=5 and number % 2 ==0:
    print("Not Weird")

  elif 6 <= number and number <= 20 and number % 2 == 0:
    print("Weird")

  elif number % 2 == 0 and number > 20:
    print("Not Weird")

  



