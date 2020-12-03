runs = list()

with open("mountain.txt", "r") as mountain:
 runs = [[r for r in run.strip()] for run in mountain]

num_trees = 0
x = 0 #position on x axis
y = 0 #the row we are on

while True:
 y += 1
 try:
  l = len(runs[y])
 except IndexError:
  break
 x = (x + 3) %l #loop around if we go off the end of the list because the same pattern repeats
 if runs[y][x] == '#':
  num_trees += 1

print(num_trees)