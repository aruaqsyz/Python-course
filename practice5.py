def deleteCharacter(s,c):
        temp = ""
        for i in s:
            if(i != c):
                temp += i
        return temp

# task 0
#isPalindrome

def removeSpaces(s):
    temp = ''
    for i in range(len(s)):
        if s[i] != ' ':
            temp += s[i]
    return temp

def isPalindrome(s):
    is_palindrome = True
    for i in range(len(s)//2):
        if s[i] != s[-1-i]:
            is_palindrome = False
    return is_palindrome

a = "q nu"
b = "q            we  rtrewq"
c = "abc"

print(isPalindrome(removeSpaces(a)))
print(isPalindrome(removeSpaces(b)))
print(isPalindrome(removeSpaces(c)))

# task 1
a = input()
def wordsStartWithE(s):
    if s[0] == 'E' or s[0] == 'e':
        return s.count(" e") + 1
    else:
        return s.count(" e")

# task 2
a = input()
print(a.count(':',0,len(a)))
print(a.replace(':','%',len(a)))

# task 3
a = input()
print(a.count('.',0,len(a)))
print(deleteCharacter(a,'.'))

# task 4
a = input()
print(a.count('a',0,len(a)))
print(a.replace('a','o',len(a)))
print(len(a))

# task 5
a = input()
print(a.lower())

# task 6
a = input()
print(a.count('a',0,len(a)))
print(deleteCharacter(a,'a'))

# task 7
c = input()
print(c.replace('n','*',c.count("n",0,len(c)//2)))

# task 8
a = input()
print(a.count(" ",0,len(a)) + 1)

# task 9
wrd = input()
s = input()
print(s.count(wrd,0,len(s)))

#task 10
a = input()
print(a.title())

# task 11
def longestSeqN(s):
    max = -999
    temp = 1
    for i in range(len(s)):
        if s[i] == 'n' and s[i+1] == 'n':
            temp += 1
        else:
            if temp > max:
                max = temp
                temp = 1
    return max
a = input()
print(a.replace('!','.',len(a)))
print(longestSeqN(a))

# task 12
a = input().split()
for i in a:
    if i[-1] == "i":
        print(i)

# task 13
a = input()
n = a.find('(')
ans = ''
for i in range(len(a)):
    if a[i] == ")":
        break
    if i > n:
        ans += a[i]
print(ans)

# task 14
a = input().split()
for i in a:
    if i[0] == "a" and i[-1] == "i":
        print(i)

# task 15
a = input()
print(a.count('t',0,len(a)))