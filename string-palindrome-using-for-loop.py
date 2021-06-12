s = str(input())
k=""
for i in range(len(s)-1, -1, -1):
    k+=s[i]
if(s == k):
    print("String Palindrome")
else:
    print("Not String Palindrome")
