def sum_n(n):
  if n==1:
   return n
  else:
    return n + sum_n(n-1)

def print_n(s,n):
  if n==1:
   print(s)
  else:
     print(s) 
     print_n(s,n-1)

def run():
  n = (int(input("Enter an int: ")))
  print(f"sum is {sum_n(n)}")
  s = (input("Enter a string: "))
  print_n(s,n)

if __name__ == "__main__":
  run()