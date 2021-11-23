str = input()
if(len(str) < 2):
    print()
else:
    s = str[0:2] + str[-2:]
    print(s)