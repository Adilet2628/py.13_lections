# работа с файлам
# каретка -указатель - курсор
# open(<путь до файла >)

# file = open("files.py")#относительный путь 
# ~ working -> desktop/bootcamp.05/file/lections/files.py 
# files -> lections/files.py

# base_dir ='/user/adiet

# file = open('files.py')
# data = file.read()
# print(data,type(data))

# file.close()


#режим работы с файлами 
# 1. r/r+/rb - read - для чтения файлов 
# 2. w/w+/wb - write  - для записи данных 
# 3. a/a+ - для добавления данных 
# b,x
# file = open('test.txt')
# print(file.readline())
# print(file.readline())

# file.close()

# file.tell()- возвращает индекс где находится курсор или указатель 

# file.seek() - перемещает курсор на идекс который вы передали 

# file = open('test.txt', 'r')
# print(file.tell)
# data = file.read()
# print(file.tell)
# file.seek(0)
# print(file.tell())
# print (file.read())
# print(file.tell())

# file.close()


# контекстный менеджер  
# with open('test.txt','r') as file: # file = open
#     data = file.read()
#     print(data)
#     print(file, 'inside')

#     print (file).read(), 'outside'



# with open ('test.txt','w') as file:
#     file.write('pervaya stroka')
#     file.write('\nhe is bastard of ned stsrk\n')
#     file.write('fchgdvjbhgnjfkhxcgj \n')
#     file.seek(0)
#     data = ['test 1 stroka,\ntest 2 stroka']
#     file.writelines(data)

# with open('test.txt','a+') as f:
#     f.seek(0)
#     f.write('john snow is fdgk')
#     f.write('\nyou know nortjfn')
#     f.seek(0)
#     f.read()



# from PIL import Image
# import re
# import pytesseract

# def get_imei_code(image: str):
#     string = pytesseract.image_to_string(image)
#     list_of_imei = re.findall(r'IMEI\d+.', string)
#     print(list_of_imei)

#     with open('imei_codes.txt', 'w') as file:
#         file.writelines(f'{x}\n' for x in list_of_imei)
#         # for x in list_of_imei:
#         #     file.write(f'{x}\n')
# base_url = 'Desktop/bootcamp05/files/lection\n'


# image = base_url + 'imei.jpg'
# get_imei_code(image)




























































































































































































