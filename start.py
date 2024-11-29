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
    result = 0
    user_input = user_input.split('+') 
    for i in range (0,len(user_input)):
        user_input[i]= float(user_input[i])
        result= add(result,user_input[i])
    print(result)
    result = 0


elif '-' in user_input:
    result = 0
    user_input = user_input.split('-')
    for i in range (0,len(user_input)):
        user_input[i]= float(user_input[i])
        result= subtrac(result,user_input[i])
    print(result)


elif '*' in user_input:
    result = 1
    user_input = user_input.split('*')
    for i in range (0,len(user_input)):
        user_input[i]= float(user_input[i])
        result= multiply(result,user_input[i])
    print(result)

    
elif '/' in user_input:
    result = 1
    user_input = user_input.split('*')
    for i in range (0,len(user_input)):
        user_input[i]= float(user_input[i])
        result= divide(result,user_input[i])
    print(result)


'''quan_list = [] # список для элементов

quan = 0
for i in range (0,len(user_input)):
    quan += user_input[i]
    quan_list.append(quan)'''




# add(сложить)
# subtrac (вычитать)
# multiply(умножить)
# divide(делить)
#user (пользователь), quantity - количество