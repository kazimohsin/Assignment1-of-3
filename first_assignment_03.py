number = (1,2,3,4,5,6,7,8,9)
even = 0
odd = 0
for a in number:
    if a % 2 ==0:
        even +=1
    else:
        odd +=1
print('even:', even)
print('odd:', odd)