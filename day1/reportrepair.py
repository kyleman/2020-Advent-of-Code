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

print("part2")

i = 0

# same algorithm for part1 one just in 3d
for i in range(0, l):
 j = i + 1
 for j in range(j, l):
  k = j + 1
  for k in range(k, l):
   if report_data[i] + report_data[j] + report_data[k] == 2020:
    print("{0} + {1} + {2} = 2020".format(report_data[i], report_data[j], report_data[k]))
    print("{0} * {1} * {2} = {3}".format(report_data[i], report_data[j], report_data[k], report_data[i] * report_data[j] * report_data[k]))

# part1
# 976 + 1044 = 2020
# 976 * 1044 = 1018944
# part2
# 1692 + 312 + 16 = 2020
# 1692 * 312 * 16 = 8446464
