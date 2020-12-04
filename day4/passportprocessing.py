from collections import defaultdict
from copy import deepcopy

valid_passports = 0
passports = []

def validatePassport(passport) -> bool:
 success: bool = True
 valid_passport = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
 for field in valid_passport:
  if not passport[field]:
   success = False
   break
 return success

with open("data.txt", "r") as data:
 passport_list = data.read().split("\n\n")

for passport in passport_list:
 tempdict = defaultdict(lambda: None)
 temp_passport = passport.split()
 for field in temp_passport:
  key = field.split(':')[0]
  value = field.split(':')[1]
  tempdict[key] = value
 passports.append(deepcopy(tempdict))
 if validatePassport(tempdict):
  valid_passports += 1

print("{0} valid passports of {1} total passports".format(valid_passports, len(passports)))