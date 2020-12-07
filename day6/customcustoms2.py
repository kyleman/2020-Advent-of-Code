def getIntersection(group: [set]) -> set:
 intersection = group[0]
 for g in group:
  intersection = intersection.intersection(g)
  
 return intersection

with open("questions.txt", "r") as questions:
 answers = [[{c for c in a} for a in q.split()] for q in questions.read().split("\n\n")]

master_answers = []

for group in answers:
 group_answers = getIntersection(group)
 master_answers.append(group_answers)

print("{0} total answers without dups.".format(sum([len(master_answers[i]) for i in range(0, len(master_answers))])))