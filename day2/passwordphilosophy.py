with open("passwords.txt", "r") as passwords:
 password_list = [pws.strip() for pws in passwords]

correct_password_count = 0

for pw in password_list:
 scheme = pw.split()
 min = int(scheme[0].split("-")[0])
 max = int(scheme[0].split("-")[1])
 char = scheme[1].strip(":")
 occurences = scheme[2].count(char)
 if occurences >= min and occurences <= max:
  print(pw)
  correct_password_count += 1

print("{0} valid passwords".format(correct_password_count))
