"""
Online status
The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.
For example, consider the following dictionary:
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
In this case, the number of people online is 2.
Write a function named online_count that takes one parameter.
The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
Your function should return the number of people who are online.


"""
def online_status(statuses):
    count = 0
    for name,status in statuses.items():
        if status == "online":
            count += 1
    return count





statuses = {"Alice": "online","Bob": "offline","Eve": "online",
}


print(online_status(statuses))