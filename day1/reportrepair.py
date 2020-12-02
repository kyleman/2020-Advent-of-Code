with open("report.txt", "r") as report:
 report_data = [int(number.strip()) for number in report] # need int() or list is a list of strings

print("part1")

l = len(report_data)
i = 0

# remember range is 0, l not inclusive
for i in range(0, l):
 j = i + 1
 for j in range(j, l):
  # we don't need to loop through all the numbers the second time because we have already checked half of the numbers
  # a+ b is the same as b + a
  # we can do this in n^2/2 and not n^2
  if report_data[i] + report_data[j] == 2020:
   print("{0} + {1} = 2020".format(report_data[i], report_data[j]))
   print("{0} * {1} = {2}".format(report_data[i], report_data[j], report_data[i] * report_data[j]))

# part1 answer
# 976 + 1044 = 2020
# 976 * 1044 = 1018944

print("part2")

#do this the inefficient way
for i in report_data:
 for j in report_data:
  for k in report_data:
   if i + j + k == 2020:
    print("{0} + {1} + {2} = 2020".format(i, j, k))
    print("{0} * {1} * {2} = {3}".format(i, j, k, i * j * k))
