a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

print("Add,Sub,Multiplication,Div write which you want to do.")
x=input("Enter input:").capitalize()
 
if(x=='Add'):
   print("result:", a+b)

elif(x=='Sub'):
   print("result:", a-b)

elif(x=='Multiplication'):
   print("result:", a*b)


elif(x=='Div'):
 if b!=0:
   print("result:", a/b)
 else:
   print("Error:Div by zero")
else:
 print("Invalid")
      


# Simple calculator for freshers using python.Its not complicated. Start your journey from here. We will move advance calculator soon.
  


  

