is_parrot_talk = input("Is the parrot talking (y/n): ")
current_hour = int(input("What is the current hour: "))
if is_parrot_talk == "y" and current_hour < 7 or current_hour > 20:
    print("We're in trouble! ")
else: 
    print("Everything is fine! ")