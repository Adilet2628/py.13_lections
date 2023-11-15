# dict()- словарь-> упорядочоная колекция элементов (piton 3.7 -> ordered). каждый элемент внутри словаря хранится в виде пары -->{ключ :значение}
# aссоциативный масив, hash table, object (js)== dictin

# thistict={
# 'brand': 'ford',
# 'model': 'Mustang ',
# 'years':1967,
# }

# print(thistict,type(thistict))

# print(thistict['brand'],thistict['model'],thistict['years'])


# thistict['motor']= 'b12 turbo'

# print(thistict['motor'])

# thistict['color']= 'yellow'
# print(thistict)
# =========
# print(dir(dict))
# #  items,keys,values

# user_info = {
#     'frist_name ':'john',
#     'last_name ':'snow',
#     'age': 24,
#     'email':'johnsnow@gmail.com',
#     'role ': 'admin',
#     }
# k=user_info.keys()    
# print(k,type(k))
# ls= list(k)
# print(ls,ls[0],ls[3:])
# # ======
# ls=list(user_info.values() )   
# print(ls,type(ls))
# ls= list(ls)
# print(ls,ls[0],ls[3:])
# # ====
# el=user_info.items()
# print(user_info)
# print(el)
# for k,v in user_info
# a,b,c=1,2,3
# =============
# изменение элементов
# dict_= {'name': ' jack', ' age':'17'}
# print(dict_)#{'name': ' jack', ' age': '17'}
# dict_['name ']= 'john'
# dict_['age']=24
# print(dict_)#'name ': 'john', 'age': 24}
# dict_.update({'name ':'tirion','addres':'westeros'})
# print(dict_)
# # ==============

# получение данных со словаря 
# # get
# dict_={1:'pizza',2 :'burger', 3 : 'steak',}
# print(dict_[5],'!!!')#KeyError
# print(dict_.get(5))#None



# setdefault- работает также как и get,но если нет такого ключа то создает новую пару из этого ключа 
# d={1:'pizza',2 :'burger', 3 : 'steak',}
# print(d)
# print(d.setdefault(5,'manty'))
# print(d)
# ==========================
# fromkeys

# ls=list(range(1,100))
# print(ls)
# new_d=dict.fromkeys('12345','wf')
# print(new_d)
# =================
# удаление элементов 
# pop,popitem

# pop(<key>)-  удаляет пару по ключу
# print('\n\n\n')

# dict_={'name ':'john','ls_name':'snow'}
# print(dict_)
# removed = dict_.popitem( )
# print(removed)
# print(dict_)

# popitem- удаляет и возвращает последнюю пору 

#========================================================================\\\



roles={
    1:'admin',
    2:'costumer',
    3:'vendor'
}
product={
    'id':31,
    'title':'macbook air m1',
    'description': 'lorem ipsum',
    'price':900
}
users= {
    16:{'username':'johnsnow_12',
    'password':'bastsrd123',
    'role': roles[1]},


    34:{'username':'tirion_small',
    'password':'short21',
    'role': roles[3]},

    54:{'username':'terminator',
    'password':'terminator123',
    'role': roles[2]},


}
print(product)
print(users)
username = input('введите ваш username :').lower()
user_exists=False
for key,dict_ in users.items():
    # print(dict_,'!!!')
    if username == dict_['username']:
        id= key
        user_exists=True
        
if not user_exists:
    raise ValueError('username not found!')        
password=input('введите ваш password :').lower()

if users [id]['password']!=password:
    raise ValueError('Password did not match!')
if users[id]['role']==roles[1]:
    product['description']= input('Vvedite novoe opisaniye: ')    
else: 
    raise Exception('you do not have permissions !')

    print(product)


