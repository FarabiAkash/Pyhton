previous_no = 0
next_no = 1
count =10

print( "for")
for i in range(count):
    print(previous_no, end=" ")
    next = next_no + previous_no
    previous_no = next_no
    next_no= next
    
print()
print("while")
while True:
    print(previous_no, end=" ")
    next = next_no + previous_no
    previous_no = next_no
    next_no= next
    count -=1
    if count<0:
        break
