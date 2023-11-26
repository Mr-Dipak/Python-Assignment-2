"""
Q 4. Lets say you are running a 5 km race. Write a program that,
 1. Upon completing each 1 km asks you "are you tired?"
 2. If you reply "yes" then it should break and print "you didn't finish the race"
 3. If you reply "no" then it should continue and ask "are you tired" on every km

"""


def is_tired():
    ans = input("Are you tired ?: ")

    return ans.lower() == "yes"

for distance in range(1,6):
    if is_tired():
        print("You did't finish the race.")
        break
    else:
        print(f"You have completed {distance} km.")
    if distance == 5:
        print("You finished the rece. Congratulations!...... ")