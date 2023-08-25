alice_age = int(input("choose number: "))

if alice_age < 18:
    print("Alice is minor than 18 years.")
elif alice_age >= 18 and alice_age <= 21:
    print("Alice has between 18 and 21 years.")
else:
    print("Alice has more than 21 years.")