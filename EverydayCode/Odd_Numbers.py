numbers= range(21)
odd_numbers =""

for i in numbers :
    if i % 2 != 0:
        odd_numbers =odd_numbers + str(i) + " "
        
print(odd_numbers)
