# from models import Product,Category

# Обновление данных 
# query = Product.update(price = 500).where(Product.title=='Zara t-shirt')
# print(query)
# query.execute()




# query = Product.update(price =(Product.price+Product.price*0.2))
# print(query)
# query.execute()


# удаление данных 
# query = Product.delete().where(Product.id==17 )
# query.execute()

# удаление через обьект 
# product = Product.get(id=18)
# print(product,product.title)
# product.delete_instance()



# query = Product.delete().where(Product.id>=9)
# print(query)
# query.execute()