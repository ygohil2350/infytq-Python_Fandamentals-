#lex_auth_012693813706604544157

def find_max(num1, num2):
    max_num=-1
    g = [max_num]
    if num1<num2:
         for num in range(num1,num2+1):
            if len(str(num)) == 2:
                sum = 0
                for dig in str(num):
                    sum = sum + int(dig)
                if sum%3==0:
                    if num%5==0:
                        g.append(num)
    return max(g)


#Provide different values for num1 and num2 and test your program.
max_num=find_max(10,15)
print(max_num)
