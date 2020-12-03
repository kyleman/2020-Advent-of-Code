runs = list()

with open("mountain.txt", "r") as mountain:
 runs = [[r for r in run.strip()] for run in mountain]

def getTreeCollisions(x_step: int, y_step: int) -> int:
 num_trees = 0
 x = 0 #position on x axis
 y = 0 #the row we are on
 while True:
  y += y_step
  try:
   l = len(runs[y])
  except IndexError:
   break
  x = (x + x_step) % l #loop around if we go off the end of the list because the same pattern repeats
  if runs[y][x] == '#':
   num_trees += 1
 return num_trees 

route1 = getTreeCollisions(1, 1)
print(route1)
route2 = getTreeCollisions(3, 1)
print(route2)
route3 = getTreeCollisions(5, 1)
print(route3)
route4 = getTreeCollisions(7, 1)
print(route4)
route5 = getTreeCollisions(1, 2)
print(route5)

print( route1 * route2 * route3 * route4 * route5)