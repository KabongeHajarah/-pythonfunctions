def even_number():
 x=range(10)

 for i in x:
  if i%2==0:
   print(i)

def odd_numbers():
 y=range(20)
 for i in y:
  if i%2 !=0:
   print(i)

def divisible_by_five():
 x=range(50)
 for i in x:
  if i%5==0:
   print(f"{i} is divisible by 5")
  else:
   print(f"{i} is not divisible by 5")


def multiple_comparison():
 x=range(50)
 for i in x:
  if i%5==0:
   print(f"{i} is divisble by 5")
  elif i%7==0:
   print(f"{i} is divisble by 7")
  elif i%9==0:
   print(f"{i} is divisble by 9")
  else:
   print(f"{i} is not divisble by 5,7 0r9")


   #combining if statements with logical operators
def odd_or_even():
 x=range(20)
 for i in x:
  if i%2==0 and i%3==0:
   print(f"{i} is divisible by both 2 and 3")
  elif i%2==0 or i%3==0:
   print(f"{i} is divisible by both 2 or 3")
  else:
   print(f"{i} is not divisible by both 2 and 3")

def while_loop():
 x=1
 while x<10:
  print("Hello")
  x+=1

def break_statement():
 x=1
 while x<10:
  print("Hello")
  x+=1
  if x==5:
   break

#continue_Statement
def continue_statement():
 x=0
 while x<=20:
  x+=1
  if x %3 ==0:
   continue 
  print(x)

 