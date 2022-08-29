#Assignment - 10 Full Stack Web Development using Python MySirG For loop and range
#1. Write a python script to print MySirG N times on the screen
n=int(input("Enter a number="))
for e in range(1,n+1):
    print('MySirG')

#2. Write a python script to print first N natural numbers
[print(e) for e in range(1,int(input("Enter a number:-"))+1)]     

#3. Write a python script to print first N natural numbers in reverse order
[print(e) for e in range(int(input("Enter a number:-")),0,-1)]     

#4. Write a python script to print first N odd natural numbers
[print(e) for e in range(1,(int(input("Enter a number:-")))*2,2)]     

#5. Write a python script to print first N odd natural numbers in reverse order
[print(e) for e in range(((int(input("Enter a number:-")))*2)-1,0,-2)]     

#6. Write a python script to print first N even natural numbers
[print(e) for e in range(2,((int(input("Enter a number:-")))*2)+1,2)]   
#7. Write a python script to print first N even natural numbers in reverse order
[print(e) for e in range(((int(input("Enter a number:-")))*2),0,-2)]     
#8. Write a python script to print squares of first N natural numbers
[print(e**2) for e in range(1,(int(input("Enter a number:-"))+1),1)]     
#9. Write a python script to print cubes of first N natural numbers
[print(e**3) for e in range(1,(int(input("Enter a number:-"))+1),1)]     
#10. Write a python script to print first 10 multiples of N
a=int(input("Enter a number="))
for e in range(1,11):
    print(a*e)    

