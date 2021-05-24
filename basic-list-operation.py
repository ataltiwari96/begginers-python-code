"""
Write a python program to find the smallest & largest number from the list. Print them, 
find their difference, and multiply the complete list with this number and print the result.
Sample Input:
In[0]: 145778386 
#[1,4,5,7,7,8,3,8,6]
Out[0]: Smallest-> 1
Largest-> 8
Difference-> 7
[7,28,35,49,49,56,21,56,42]

"""
li = list(input("Enter the list: "))
print("The entered list is: ",li)
min1=min(li)
print("Smallest ->",min1)
max1=max(li)
print("Largest -> ",max1)

diff = int(max1)-int(min1)
print("Difference -> ",diff)

print([int(i)*diff for i in li])

