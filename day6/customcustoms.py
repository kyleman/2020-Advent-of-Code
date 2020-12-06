with open("questions.txt", "r") as questions:
 answers = [q.split() for q in questions.read().split("\n\n")]

master_answers = []

for group in answers:
 group_answers = set()
 for answer in group:
  for a in answer:
   group_answers.add(a)
 master_answers.append(group_answers)

print("{0} total answers without dups.".format(sum([len(master_answers[i]) for i in range(0, len(master_answers))])))