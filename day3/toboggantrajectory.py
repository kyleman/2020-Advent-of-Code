runs = list()

with open("mountain.txt", "r") as mountain:
 runs = [[r for r in run.strip()] for run in mountain]

