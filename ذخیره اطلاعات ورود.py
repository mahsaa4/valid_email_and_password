import re
import mysql.connectorgit
cnx = mysql.connector.connect(user='root',password='',
                                host='127.0.0.1', database='test')

email = input("Enter your email please: ")
password = input("Enter your password please: ")
email_regex = re.search(r'.+\@.+\..{2,3}', email)
if email_regex == None:
    print("Invalid email")
    print("Valid format: expression@string.string")
    email = input("Enter your email please: ")
    password = input("Enter your password please: ")
password_regex = re.search(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d]{6,}$', password)
if password_regex == None:
    print("Invalid password")
    email = input("Enter your email please: ")
    password = input("Enter your password please: ")
cursor = cnx.cursor()
cursor.execute('INSERT INTO security VALUES (\'%s\', \'%s\')' % (email , password))
cnx.commit()