pizza_size=input("Dear coustomer. Please choice of pizza size 'S', 'M' or 'L' :   ")
bill=0
if pizza_size== "S" :
    bill +=12

elif pizza_size== "M" :
    bill +=15

else :
     bill +=18       


add_pepporoni = input(" do you wnat add pepporoni pizza then enter 'Y' else 'N' :")
if add_pepporoni =='Y':
    if pizza_size == 'S':
        bill +=2

    else:
        bill +=3    


add_extracheeg = input("do you want add extra cheeg 'Y' or 'N' :")
if  add_extracheeg =='Y' :
    bill +=3

else :
    bill +=0    

print(f"please pay your bill is ${bill}")    
