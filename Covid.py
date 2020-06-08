ans = ""
result = 0
print("Enter either YES or NO")
ans = input("Do you have cough?")
if ans == 'yes':
    result = result + 1
elif ans == 'no':
    result == result + 0
else:
    print("Incorrect input")
ans = input("Do you have a runny nose?")
if ans == 'yes':
    result = result + 1
elif ans == 'no':
    result = result + 0
else:
    print("Incorrect input")
ans = input("Do you have diarrhea?")
if ans == 'yes':
    result = result + 1
elif ans == 'no':
    result = result + 0
else:
    print("Incorrect input")    
ans = input("Do you have headache?")
if ans == 'yes':
    result = result + 1
elif ans == 'no':
    result = result + 0
else:
    print("Incorrect input")
ans = input("Do you have bodyache?")
if ans == 'yes':
    result = result + 1
elif ans == 'no':
    result = result + 0
else:
    print("Incorrect input")
ans = input("Do you have sorethroat?")
if ans == 'yes':
    result = result + 1
elif ans == 'no':
    result = result + 0
else:
    print("Incorrect input")
ans = input("Do you have fever?")
if ans == 'yes':
    result = result + 1
elif ans == 'no':
    result = result + 0
else:
    print("Incorrect input")
ans = input("Do you have breathing difficulties?")
if ans == 'yes':
    result = result + 2
elif ans == 'no':
    result = result + 0
else:
    print("Incorrect input")
ans = input("Are you experiencing fatigue?")
if ans == 'yes':
    result = result + 2
elif ans == 'no':
    result = result + 0
else:
    print("Incorrect input")
ans = input("Have you travelled during the last 14 days?")
if ans == 'yes':
    result = result + 2
elif ans == 'no':
    result = result + 0
else:
    print("Incorrect input")
ans = input("Do you have a travel history to any Covid-19 infected area?")
if ans == 'yes':
    result = result + 2
elif ans == 'no':
    result = result + 0
else:
    print("Incorrect input")
ans = input("Do you have direct contact or taking care of an an infected person?")
if ans == 'yes':
    result = result + 2
elif ans == 'no':
    result = result + 0
else:
    print("Incorrect input")
if result <= 2:
    print("May be stress related")
elif result >= 3 and result <= 5:
    print("Hydtrate properly and practice proper personal hygiene")
elif result >= 6 and result <= 12:
    print("Seek a consultation with a doctor")
else:
    print("Call the NCDC HOTLINE")
print("STAY SAFE NIGERIANS")
    
    
