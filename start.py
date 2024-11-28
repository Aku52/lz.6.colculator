print('Введите выражение')
user_unput=input()

def addition (a,b):
    return a + b

def difference (a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division  (a,b):
    return a / b



if '+' in user_unput:
    user_unput = user_unput.split('+')
    for i in range (0,len(user_unput)):
        user_unput[i]= float(user_unput[i])
        result= 
        
#addition (сложение)
#subtraction (вычитание) difference(разность)
#multiplication(умножить)
#division (делить)
#user (пользователь)