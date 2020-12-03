runs = list()

with open("mountain.txt", "r") as mountain:
 runs = [[r for r in run.strip()] for run in mountain]

num_trees = 0
x = 0 #position on x axis

for run in runs:
 l = len(run)
 if run[x] == '#':
  num_trees += 1
 else:
  x = (x + 3) % l #loop around if we go off the end of the list because the same pattern repeats

print(num_trees)