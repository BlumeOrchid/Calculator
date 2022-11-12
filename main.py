print("Simple Calculator")
print("operators : +,-,*,/")
operation=input("Enter Operation you want to perform :")

#Seperation of operations at different levels

#if condition for sum
if operation=='+':
   numeral_a=float(input("Enter First Number :"))
   numeral_b=float(input("Enter Second Number :"))
   output_sum=(numeral_a+numeral_b)
   print("The Sum of",numeral_a,"and",numeral_b,"is :",output_sum)
#elif condition for subtraction  
elif operation=='-':
   numeral_c=float(input("Enter First Number :"))
   numeral_d=float(input("Enter Second Number :"))
   output_subtraction=(numeral_c/numeral_d)
   print("The Subtraction of",numeral_c,"and",numeral_d," is :",output_subtraction)
#elif condition for division
elif operation=='/':
   numeral_e=float(input("Enter First Number :"))
   numeral_f=float(input("Enter Second Number :"))
   output_division=(numeral_e/numeral_f)
   print("The Division of ",numeral_e,"and",numeral_f,"is :",output_division)
#elif condition for product
elif operation=='*':
   numeral_g=float(input("Enter First Number :"))
   numeral_h=float(input("Enter Second Number :"))
   output_product=numeral_g*numeral_h
   print("The Product of ",numeral_g,"and",numeral_h,"is :",output_product)
#else for condition if all values are not true
else:
  print("invalid Operation")
