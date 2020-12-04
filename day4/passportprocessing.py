from collections import defaultdict
from copy import deepcopy

valid_passports = 0
passports = []

def validateBirthYear(byr:str) -> bool:
 valid: bool = False
 if byr.isnumeric() and len(byr) >= 4:
  birthyear = int(byr)
  if birthyear >= 1920 and birthyear <= 2002:
   valid = True
 return valid

def validateIssueYear(iyr: str) -> bool:
 valid: bool = False
 if iyr.isnumeric() and len(iyr) >= 4:
  issueyear = int(iyr)
  if issueyear >= 2010 and issueyear <= 2020:
   valid = True
 return valid

def validateExpirationYear(eyr: str) -> bool:
 valid: bool = False
 if eyr.isnumeric() and len(eyr) >= 4:
  expirationyear = int(eyr)
  if expirationyear >= 2020 and expirationyear <= 2030:
   valid = True
 return valid

def validateheight(hgt: str) -> bool:
 valid: bool = False
 return valid

def validateHairColor(hcl: str) -> bool:
 valid: bool = False
 return valid

def validateEyeColor(ecl: str) -> bool:
 valid: bool = False
 return valid

def validatePassportID(pid: str) -> bool:
 valid: bool = False
 return valid

def validatePassport(passport) -> bool:
 success: bool = True
 valid_passport = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
 for field in valid_passport:
  if not passport[field]:
   success = False
   break
  else:
   if field == "byr":
    if not validateBirthYear(passport[field]):
     success = False
     break
   if field == "iyr":
    if not validateIssueYear(passport[field]):
     success = False
     break
   if field == "eyr":
    if not validateExpirationYear(passport[field]):
     success = False
     break
   if field == "hgt":
    if not validateHeight(passport[field]):
     success = False
     break
   if field == "hcl":
    if not validateHairColor(passport[field]):
     success = False
     break
   if field == "ecl":
    if not validateEyeColor(passport[field]):
     success = False
     break
   if field == "pid":
    if not validatePassportID(passport[field]):
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