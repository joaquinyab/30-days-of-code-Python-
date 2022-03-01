
numberOfTimes = int(input())

dictt = {}


for _ in range(numberOfTimes):
  text = input().split()

  dictt[text[0]] = text[1]


for i in range(numberOfTimes):
  nameInDictionary = str(input())
  if nameInDictionary in dictt:
    print(nameInDictionary + "=" + dictt[nameInDictionary])

  else:
    print("Not found")





  




