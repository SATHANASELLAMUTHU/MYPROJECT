n=int(input("Enter the number:"))
f=0
s=1
for i in range(n):
  print(s)
  t=f
  f=s
  s=t+s
