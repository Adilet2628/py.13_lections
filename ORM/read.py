# # import peewee
# # from models import Product, Category

# # def get_all_categories():
# #     return Category.select()

# # def get_all_products():
# #     return Product.select()


# categories = get_all_categories()
# print('Категории в БД: ')
# for x in categories:
#     print(x)
#     print(x.title.title())
#     print(x.created_at.strftime('%Y-%m-%d -> %H:%M:%S'))
#     print()

# product = get_all_products()
# print('Все товары в БД: ')
# sum_price = 0
# for x in product:
#     print(f'{x.title} -> {x.price} -> {x.category_id.title}')
#     print()
#     sum_price += x.price
# print(f'AVG price: {sum_price / len(product)}$')


# products = get_all_products()
# category = int(input('Введите категорию (1-платья 2-джинсыб 3-футболкиб 4-свитерыб 5-обувь): '))
# for x in products:
#     if x.category_id.category_id == category:
#         print(x.title, x.price, x.category_id.title)


# category_name = input('vvedite title catalogii:').lower().strip()
# try:
    
#         category = Category.get(title= category_name)
#         print(category,category.title)
# except peewee.DoesNotExist:
#     print('такой категори нет')
# else:
#     for product in category.products:
#         print(f'title: {product.title},price = {product.price},category:  {product.category_id.title}')














































