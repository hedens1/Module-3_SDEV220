def get_odds():
    for n in range(10):
        if n % 2 ==1:
            yield n 

count = 0
for value in get_odds():
    count += 1 
    if count == 3:
        print(value)
        break