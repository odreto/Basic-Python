print ("""***********************

    <Calculate Program>
    
    
   
   
1.Plus  +
2.Minus −
3.Multiplication *
4.Division /

**********************""")

a = int(input("1st:"))
b = int(input("2nd:"))

sum = input("Choose Symbol:")

if (sum == "1"):
  print("{} and {} sum {}".format(a,b,a+b))
 
elif(sum == "2"):
  print("{} and {} sum {}".format(a,b,a-b))
  
elif(sum == "3"):
  print("{} and {} sum {}".format(a,b,a*b))
  
elif(sum == "4"):
  print("{} and {} sum {}".format(a,b,a/b))
  
else:
  print("Mistake")
