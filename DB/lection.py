# PostgreSQL - система управления базами данных(СУБД\DBMS)
# Это ряд программ и инструментов  позволяющих создавать БД, управлять ею и манипулировать данными внутри (CRUD)


# Postgres - сама база данных, она объектно реляционная, то есть данные хранятся в виде таблицы, и таблицы имеют связи между собой 



# SQL (Structured Query language) - декларативный язык стркутурированных запросов, он применяется для создания и получения данных при помощи запросов в БД


# --------------------------------------------------------------------------------------------
# командв для входа в бд через юзера Postgres:
# sudo -u Postgres psql


# команда для входа в своего юзера  psql

# командадля выхода в своего юзера 
# \q
# exit


# создание суперюзера 
# CREATE ROLE 'username' WITH PASSWORD '1';

# изменение пароля 
# ALTER USER 'username' WITH PASSWORD '1';

# создание бд 
# CREATE DATABASE 'name';

# \l -список всех бд 

# \du все юзеры 
# \dt - все таблицы (нужно подключиться к бд заранее  )
# \d  подробная информация про таблицу (нужно подключиться к бд заранее )
# \ с 'name' - команда для подключения к бд

# -----------------------------------------------------============================================================================
# типы полей в Postgresql
# Numeric Types(числовые типы)
    # a. smallint(2 bytes) - > -32767 to 32767
    # b. integer( 4 bytes) -> -2.147... to 2.147...
    # c. bigint( 8 bytes)-> ...
    # d. real (4 bytes)-> число с плавающей точкой, вещественное 
    # f. double precision (8 bytes)-> real но только с двойной точностью 
    # d.serial(4 bytes)-> int, auto-incriment


# Charecter types (символьные типы (строковые )):
    # a. vachar (кол-во символов) - если мы укажем 50, а заполним 10, то остальные будут свободны. Макс 255
    # b. char(кол-во символов) - если мы укажем 50, а заполним 10, то остальные будут заполнены пробелом. Макс 255
    # с. text()-  неограниченное количество символов 

# Boolean Type
    # a. boolean(1 bytes)-> True/False

# date -> календарная дата (год.месяц.день)

# location -> координатная точка (x, y)- (245,-12)


# enumerate types:
#     ('a','b','c')
#     CREATE TYPE <any name> AS ENUM ('Happy', 'Sad', 'Mad')

# -----================-------------===-------------=-----------------------------========------------=======------------========----
# ====================================================================================================================================



# создание бд 
# CREATE DATABASE name; recomended
# create database name;

# команда для создания таблицы 
# CREATE TABLE <tableName>(
#     <column> <type> [<>constraint]
#     <column> <type> [<>constraint]
# )

# CREATE TABLE filme(
#     id serial,
#     code char(5),
#     title varchar(100),
#     date date,
#     genre varchar(50),
#     budget bigint,
#     country vachar(50)
# );


# DROP TABLE <name> - удаление таблицы 


# команда для добавления данных 
# INSTERT INTO <tablename> (columns) VALUES (data), (data);

# INSTERT INTO filme (code, title data, genre, budget,country)VALUES('AU56', 'Game of Thrones','2015-05-31','Fantasy',1000000,'USA')

# команда для обновления данных 
# UPDATE (table) SET <column> = <new_value> WHERE<column> = <value>;
# UPDATE filme SET genre = 'Adventure' WHERE code 'het5'

# КОМАНДА ДЛЯ УДАЛЕНИЯ 
# DELETE FROM <table> WHERE <column> = <value>;



# ==================================================================================================
# ORDER BY: Позволяет нам сотриторвать выводяще данные по убыванию или по возрастанию. ASC(по возрастанию) и DESC (ПО убыванию)
# синтаксис: SELECT <row> FROM <tablename> ORDER BY <row> [ASC/DESC]
# ----------------------------------------------------------------------------------
# WHERE : используется для фильтрации по полям. будут выводиться только те данные которые соответствуют условию оператора WHERE
# синтаксис: SELECT <row> FROM <tablename> WHERE <row>  = 'чему либо';

# BETWEEN : УСЛОВИЕ МЕЖДУ 
# SELECT * FROM films WHERE id BETWEEN 3 and  

# -----------------------------------------------------------------------------
# LIKE: Выводит результат который соответствует введенному шаблонуf -- для строк. 
# Чувствителен к регистру 
# ILIKE : ТОЖЕ САМОЕ ТОЛЬКО НЕЗАВИСИТ ОТ РЕГИСТРА 
# Синтаксис: SELECT <row> FROM <tablename> WHERE <row> LIKE/ILIKE 'чему либо';


# ---------------------------------------------------
# Экспорт бд(дамп):
# pg_dump -U <username> -d 'dbname' > 'file.sql'

# импорт:
# psql -U <username> -d 'dbname' -f <filename>


##---------------##---------------##---------------##---------------##---------------##---------------
                                    # Группировка

# SELECT count(product_name), c.category_name FROM products as p, categories as c WHERE p.category_id = c.category_id GROUP BY c.category_name;





# JOIN: выборка данных из двух таблицб соединение таблиц, соединение таблиц

# LEFT JOIN: выборка будет содержать все строки из левой таблицы

# RIGHT JOIN: выборка будет содержать все таблицы из правой таблицы

# SELECT p1.title, p1.price, o1.quality, p1.price * o1.quality as total_sum FROM product p1, orders o1 WHEREp1.id = o1.product_id; - Запрос сразу после в де таблицы

# SELECT p1.title, p1.price, o1.quality, p1.price * o1.quality as total_sum FROM product p1 JOIN orders ON p1.id = o1.product_id;










# Напишите следующие запросы:
# 1. Найдите 10 самых часто встречающихся слов.

# shacspire_db=# SELECT plaintext,occurences  FROM  wordform limit 10;
#  plaintext | occurences 
# -----------+------------
#  the       |      28932
#  and       |      27296
#  i         |      21120
#  to        |      20136
#  of        |      17169
#  a         |      14943
#  you       |      13989
#  my        |      12950
#  in        |      11512
#  that      |      11487
# (10 rows)


# 2. Найдите все слова, которые начинаются с буквы ‘a’, регистр не должен иметь
# значения.a’, регистр не должен иметь значения. 
#  plaintext     
# -------------------
# SELECT plaintext FROM wordform WHERE plaintext  ILIKE 'a%';
#  and
#  a
#  as
#  all
#  are
#  at
#  am
#  an
#  art
#  away
#  any
#  again
#  ay
#  against

# 
# 3. Найдите все произведения,
# которые относятся к жанру ‘a’, регистр не должен иметь значения.p’.
# shacspire_db=# SELECT *  FROM  work WHERE genretype !='p';
#      workid     |           title           |                 longtitle                 | year | genretype | notes |  source   | totalwords | totalparagraphs 
# ----------------+---------------------------+-------------------------------------------+------+-----------+-------+-----------+------------+-----------------
#  12night        | Twelfth Night             | Twelfth Night, Or What You Will           | 1599 | c         |       | Moby      |      19837 |            1031
#  allswell       | All's Well That Ends Well | All's Well That Ends Well                 | 1602 | c         |       | Moby      |      22997 |            1025
#  antonycleo     | Antony and Cleopatra      | Antony and Cleopatra                      | 1606 | t         |       | Moby      |      24905 |            1344
#  asyoulikeit    | As You Like It            | As You Like It                            | 1599 | c         |       | Gutenberg |      21690 |             872
#  comedyerrors   | Comedy of Errors          | The Comedy of Errors                      | 1589 | c         |       | Moby      |      14692 |             661
#  coriolanus     | Coriolanus                | Coriolanus                                | 1607 | t         |       | Moby      |      27577 |            1226
#  cymbeline      | Cymbeline                 | Cymbeline, King of Britain                | 1609 | h         |       | Moby      |      27565 |             971
#  hamlet         | Hamlet                    | Tragedy of Hamlet, Prince of Denmark, The | 1600 | t         |       | Gutenberg |      30558 |            1275
#  henry4p1       | Henry IV, Part I          | History of Henry IV, Part I               | 1597 | h         |       | Moby      |      24579 |             884
#  henry4p2       | Henry IV, Part II   
# 
# 
# 4. Найдите среднее количество параграфов в произведения жанра ‘a’, регистр не
# должен иметь значения.t’.
#shacspire_db=# SELECT AVG(totalparagraphs)  FROM  work WHERE genretype ='t';
#           avg          
# -----------------------
#  1070.8181818181818182
# (1 row)

# 


# #  5. Выведите все произведения, в которых количество слов выше среднего.
# # 
# SELECT title FROM work WHERE (SELECT AVG(totalwords) FROM work) < totalwords ;
#            title           
# ---------------------------
#  All's Well That Ends Well
#  Antony and Cleopatra
#  As You Like It
#  Coriolanus
#  Cymbeline
#  Hamlet
#  Henry IV, Part I
#  Henry IV, Part II
#  Henry V
#  Henry VI, Part I
#  Henry VI, Part II
#  Henry VI, Part III
#  Henry VIII
#  King John
#  King Lear
#  Love's Labour's Lost
#  Measure for Measure
#  Merchant of Venice
#  Merry Wives of Windsor
#  Much Ado about Nothing
#  Othello
#  Richard II
#  Richard III
#  Romeo and Juliet
#  Taming of the Shrew
#  Titus Andronicus
#  Troilus and Cressida
#  The Winter's Tale
# (28 rows)


# 
# 6. Выведите имя героя, количество его реплик, и произведение, в котором
# этот герой встречается.
# 
# 
# 7. Выведите среднее количество реплик героев в произведении ‘a’,
# регистр не должен иметь значения.Romeo and Juliet’. 
# 
# 
# 8. Выведите общее
# количество слов в каждой из секций в таблице paragraph. 
# 
# 
# 9. Выведите
# всех героев, которые имеют от 15 до 30 реплик.
# 
# 
# 
# 10. Выведите все произведения, которые были написаны в 17 веке
# 
# 
# 
# 11. Найдите все произведения, которые имею в полном названии
# слово ‘a’, регистр не должен иметь значения.the’ 12. Выведите все























































































































































































