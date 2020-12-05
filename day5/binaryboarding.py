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

with open("boardingpasses.txt", "r") as boardingpasses:
 passes = boardingpasses.read().split()

max_seat_id = 0

for code in passes:
 row = getRowNumber(code[:7])
 seat = getSeatNumber(code[-3:])
 temp_max = row * 8 + seat
 if temp_max > max_seat_id:
  max_seat_id = temp_max

print(max_seat_id)