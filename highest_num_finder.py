#Using "If Statement Only", find and print the highest number entered.

#Define the Variables
def find_the_highest(var1, var2, var3, var4, var5):

#Since we will only use the "If Statement ONLY" suppose the var1 is the highest.
    highest_number = var1

#Using var1 as the highest, we can now compare it with other variables. 
    if var2 > highest_number:
        highest_number = var2
    
    if var3 > highest_number:
        highest_number = var3
    
    if var4 > highest_number:
        highest_number = var4
    
    if var5 > highest_number:
        highest_number = var5

    return highest_number
