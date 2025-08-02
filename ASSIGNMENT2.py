#Module 3: Control Structures in Python
#Task 1: Check if a Number is Even or Odd
#Task 2: Sum of Integers from 1 to 50 Using a Loop

#Task 1: Check if a Number is Even or Odd
number_input=int(input("number:")) # taking input from user using int and integer value so use int first
if number_input %2==0: #used if else condition\ input division result equal to 0 mean even
    print(str(number_input) +" is even number") # if input even then it will print
else:
    print(str(number_input)+" is odd number") #if odd number this will print

#Sum of Integers from 1 to 50 Using a Loop
number=int(input("number:"))

#Task 2: Sum of Integers from 1 to 50 Using a Loop
i = 0 #take i as variable to start number from 0
j = 0 #another variable starting from 0 to show summation output
while i < 51: #run while loop condition , number under 51 men upto 50  it will run
    j=j+i #one by one loop j will add with value of i
    i += 1 # i value will increment by 1 upto 50
    #print(j) # if we want to print every loop sum numbers
    if i == 51: break # Exit the loop when count is 51 mean 0 to 50 loop
print("sum of the numbers from 0 to 50 is",str(j)) # print string + string
