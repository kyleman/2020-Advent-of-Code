def getRowNumber(code: str) -> int:
 row: int = 0
 i = 6
 for x in code:
  if x == "B":
   row +=2**i
  i -= 1
 return row

def getSeatNumber(code: str) -> int:
 seat: int = 0
 i = 2
 for x in code:
  if x == "R":
   seat +=2**i
  i -= 1
 return seat

seats = [False for i in range(0, 896)]

with open("boardingpasses.txt", "r") as boardingpasses:
 passes = boardingpasses.read().split()

for code in passes:
 row = getRowNumber(code[:7])
 seat = getSeatNumber(code[-3:])
 seats[(row - 1) * 8 + (seat - 1)] = True

for i in range(1, 895):
 if not seats[i]and (seats[i - 1] and seats[i + 1]):
  print("your seat id is {0}".format(i + 9))