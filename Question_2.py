"""
Q 1. After flipping a coin 10 times you got this result,
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

Using for loop figure out how many times you got heads


"""
coin_result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

head_count = 0

for outcome in coin_result:
    if  outcome == "heads":
        head_count= head_count +1

    
print(head_count)
