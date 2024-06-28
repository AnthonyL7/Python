def validate_pin(pin):
    #return true or false
  if len(pin) == 4 and pin.isdigit() or len(pin) == 6 and pin.isdigit(): 
    print(True)
  else: 
    print(False)

validate_pin('-12345')

