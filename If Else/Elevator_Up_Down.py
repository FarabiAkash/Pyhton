current_floor = 0 # This is just a starting point
user_floor = 0 # This is just a starting point

user_floor = 6

while user_floor != "exit"  :
    difference = user_floor - current_floor
     
    if difference < 0 : 
        current_floor = user_floor
        print ( " Move down ")
 
    if difference > 0 : 
        current_floor = user_floor
        print ( " Move up ")    
         
    if difference == 0 : 
        current_floor = user_floor
        print ( " Open door ")            
         
    user_floor = input()
    if user_floor != "exit" :
        user_floor = int(user_floor)
