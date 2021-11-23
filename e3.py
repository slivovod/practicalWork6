str = input()
c = str[0]
str = str[1:].replace(c ,"$")
print(c + str)