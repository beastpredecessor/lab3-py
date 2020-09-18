#Author: xuanyi shen xjs5065@psu.edu
# Collaborator: Zihao Xu     zbx5084@psu.edu
# Collaborator: Jared Cole jcc6066@psu.edu
# Collaborator: Jacob Hallowell jph5997@psu.edu
# Section: 4
# Breakout: 9

def sum_n(n):
  if n==0:
   return 0
  else:
    return n + sum_n(n-1)

def print_n(s,n):
  if n==0:
   return
  else:
     print(s) 
     print_n(s,n-1)

def run():
  n = (int(input("Enter an int: ")))
  print(f"sum is {sum_n(n)}.")
  s = (input("Enter a string: "))
  print_n(s,n)

if __name__ == "__main__":
  run()