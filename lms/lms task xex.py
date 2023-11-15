# 1
# def reg():
#     s = input("Vvedite text : ")
#     lower_ = list(filter(lambda x: x.islower(),list(s))) 
#     upper_ = list(filter(lambda x: x.isupper(),list(s))) 
#     print('Количество символов в верхнем регистре:', len(upper_)) 
#     print('Количество символов в нижнем регистре:', len(lower_))
# reg()
                                                  
# 2
# def ls(n):
#     wer={}
#     for x in range(1,n+1):
#         wer[x]= x**3    
#     return wer

# print(ls(5))
# 3
# def sum_range(start, end):
#     if start > end:
#         start , end=end , start
#     ls = 0  
#     for num in range(start, end + 1 ):
#         ls += num 
#     print (ls) 
# sum_range(5,2)

# 4

# def is_isogram(word):
#     word = word.lower()
    
#     unique_letters = set()
    
#     for letter in word:
#         if letter in unique_letters:
#             return False
#         unique_letters.add(letter)
    
#     return True

# print(is_isogram('odfghj')) 

# 5

# def counter(s: str) -> dict:
#     d = dict()
#     s = s.replace(',', '').lower()
#     s = s.replace('!', '')
#     s = s.split(' ')
#     for i in s:
#         c = s.count(i)
#         d[i] = c
#     return d

# print(counter('Money, money, money, it’s always sunny, sunny, world in the richmen’s world!'))












 





















































































