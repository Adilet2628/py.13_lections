# num = int(input ('введите число : '))
# if num % 2 ==0:

#      print('even!')
# else:
#     print('odd')
# print('even'if num %2==0 else "odd")    
# res=('even'if num %2==0 else "odd")    

# print(res)
# =========================================================================================
# ternary operators (тенарный оператор )- это конструкция которая по своему действию аналогична конструкции if/else, но при этом записывается в одну строчку 
# <выражение если True> if < условие > else < выражение если False>

# sentence = input(' введите предложение : ')
# if sentence [-1]=='?':
#     res='vvoprositelnoe'
# else:
#     res =' normal one '

# res1='vvoprositelnoe'if sentence [-1]=='?'else ' normal one '
# print(res,res1)
# ============================================
# ls= [23,43,35,33,65,78,99,20]
# print(ls)
# choice = input('введите min\max:').lower().strip()
# res=max(ls) if choice=='max'else min (ls)if choice=='min' else 'incorre'
# print(res)

# ===========================================================
# flag=True
# symvols='0123456789'+'-'+'.'

# while flag:
#     num1 = input('введите первое число : ')
#     is_correct = True
#     for x in num1:
#         if x not in symvols:
#             print('вы ввели неправильно число')
#             is_correct= False
#             break

#     if not is_correct:
#             continue
#     num2 = input('введите второе  число : ')
#     is_correct = True
#     for x in num2:
#         if x not in symvols:
#             print('вы ввели неправильно число')
#             is_correct= False
#             break
#     if not is_correct:
#             continue    


#     num1= float(num1) if '.'in num1 else int (num1) 
#     num2= float(num2) if '.'in num2 else int (num2) 
#     # print(num1,type(num1 ))
#     # print(num2,type(num2 ))
#     operator= input('введите операцию (+,-,*,/): ').strip()
#     if operator=='+':
#         print(f'результат: {num1 + num2 }')
#     elif operator== '-':
#          print(f'результат: {num1 - num2 }')    
#     elif operator== '*':
#          print(f'результат: {num1 * num2 }') 
#     elif operator== '/':
#          print(f'результат: {num1 /num2 }' if num2!=0 else 'на ноль делить нельзя ')
#     else:
#         print('вы ввели неправильный оператор ')
#     choise = input('хотите продолжить (yes/no):')
#     if choise.lower().strip()!='yes':
#         flag= False
#         print('пока пока ')




    # if num1.isdigit():
    #     num1= int (num1)
    # else:
    #     print('invalid')    
    # print(num1)



comprehensions












































































































































































































