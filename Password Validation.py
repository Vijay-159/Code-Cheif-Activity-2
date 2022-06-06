import re
while True:
  print("Please enter password should be \n1) One Capital Letter\n2) Special Character\n3) One Number \n4) Length Should be 8-18: ")
  pswd = input()
  reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
  match_re = re.compile(reg)
  res = re.search(match_re, pswd)
  if res:
    print("Valid Password")
    break
  else:
    print("Invalid Password Try again")
    continue
  
   
   


