mylist = []

print("Enter a series of values (99999 to quit): ")
x = 0

while x != 99999:
    x = int(input(''))
    if x <= 0:
        continue
    mylist.append(x)
    
mylist.remove(99999)

l = len(mylist)
s = sum(mylist)
a = s/l

print("The average of the positive values is", a)
