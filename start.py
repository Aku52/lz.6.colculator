print('Введите выражение')
user_input=input()

def add (a,b):
    return a + b

def subtrac (a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide (a,b):
    return a / b


# split - разделяет вфражение
if '+' in user_input:
    user_input = user_input.split('+')
    result = float(user_input[0])
    for i in range (0,len(user_input)):
        user_input[i]= float(user_input[i])
        result= add(result,user_input[i])
    print(result)
    result = 0


elif '-' in user_input:
    user_input = user_input.split('-')
    result = float(user_input[0])
    for i in range (1,len(user_input)):
        user_input[i]= float(user_input[i])
        result= subtrac(result,user_input[i])
    print(result)
    result = 0


elif '*' in user_input:
    user_input = user_input.split('*')
    result =  float(user_input[0])
    for i in range (1,len(user_input)):
        user_input[i]= float(user_input[i])
        result= multiply(result,user_input[i])
    print(result)
    result = 0

    
elif '/' in user_input:
    user_input = user_input.split('*')
    result =  float(user_input[0])
    for i in range (1,len(user_input)):
        user_input[i]= float(user_input[i])
        result= divide(result,user_input[i])
    print(result)
    result = 0



# add(сложить)
# subtrac (вычитать)
# multiply(умножить)
# divide(делить)
#user (пользователь), quantity - количество