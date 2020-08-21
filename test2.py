import turtle as tt
import pyautogui as pag
import random

print("Привет!")
print("Как")
print("Дела?")
print("Это Игра!")

tt.speed(10000)

line1 = [0,  0, 0, 0]
line2 = [0,  0, 0, 0]
line3 = [0,  0, 0, 0]

mfn = []
mfk = []

def setka():
    tt.left(90)
    tt.forward(120)
    tt.left(90)
    tt.forward(40)
    tt.left(90)
    tt.forward(120)
    tt.left(90)
    tt.forward(120)
    tt.left(90)
    tt.forward(120)
    tt.left(90)
    tt.forward(120)
    tt.left(90)
    tt.forward(40)
    tt.left(90)
    tt.forward(120)
    tt.right(90)
    tt.forward(40)
    tt.right(90)
    tt.forward(120)
    tt.right(90)
    tt.forward(80)
    tt.right(90)
    tt.forward(80)
    tt.right(90)
    tt.forward(120)

def setka2():
    tt.left(90)
    tt.forward(180)
    tt.left(90)
    tt.forward(60)
    tt.left(90)
    tt.forward(180)
    tt.left(90)
    tt.forward(180)
    tt.left(90)
    tt.forward(180)
    tt.left(90)
    tt.forward(180)
    tt.left(90)
    tt.forward(60)
    tt.left(90)
    tt.forward(180)
    tt.right(90)
    tt.forward(60)
    tt.right(90)
    tt.forward(180)
    tt.right(90)
    tt.forward(120)
    tt.right(90)
    tt.forward(120)
    tt.right(90)
    tt.forward(180)

def CRESTIK():
    tt.forward(20)
    tt.left(180)
    tt.forward(20)

    tt.forward(20)

    tt.left(180)
    tt.forward(20)

    tt.left(90)
    tt.forward(20)
    tt.left(180)
    tt.forward(20)
    tt.forward(20)

def NOLIK0():
    for i in range(100):
        tt.forward(20)
        tt.back(20)
        tt.right(4)

def POS11():
    tt.penup()
    tt.goto(-30, 30)
    tt.pendown()

def POS12():
    tt.penup()
    tt.goto(30, 30)
    tt.pendown()

def POS13():
    tt.penup()
    tt.goto(90, 30)
    tt.pendown()

def POS21():
    tt.penup()
    tt.goto(-30, 90)
    tt.pendown()

def POS22():
    tt.penup()
    tt.goto(30, 90)
    tt.pendown()

def POS23():
    tt.penup()
    tt.goto(90, 90)
    tt.pendown()

def POS31():
    tt.penup()
    tt.goto(-30, 150)
    tt.pendown()

def POS32():
    tt.penup()
    tt.goto(30, 150)
    tt.pendown()

def POS33():
    tt.penup()
    tt.goto(90, 150)
    tt.pendown()

setka2()

'''
POS11()
NOLIK0()
POS12()
CRESTIK()
POS13()
NOLIK0()

POS21()
CRESTIK()
POS22()
NOLIK0()
POS23()
CRESTIK()

POS31()
NOLIK0()
POS32()
CRESTIK()
POS33()
NOLIK0()
'''

while True:
    krestik = pag.prompt(text='Введите код клетки в формате ЛК (Л - Линия, К - Клетка):', title='Код Клетки!' , default='')
    mfk.append(krestik)
    if krestik == "11":
        POS11()
        CRESTIK()
        line1[1] = 1
    elif krestik == "12":
        POS12()
        CRESTIK()
        line1[2] = 1
    elif krestik == "13":
        POS13()
        CRESTIK()
        line1[3] = 1
    elif krestik == "21":
        POS21()
        CRESTIK()
        line2[1] = 1
    elif krestik == "22":
        POS22()
        CRESTIK()
        line2[2] = 1
    elif krestik == "23":
        POS23()
        CRESTIK()
        line2[3] = 1
    elif krestik == "31":
        POS31()
        CRESTIK()
        line3[1] = 1
    elif krestik == "32":
        POS32()
        CRESTIK()
        line3[2] = 1
    elif krestik == "33":
        POS33()
        CRESTIK()
        line3[3] = 1

    #ПРОВЕРКА КРЕСИТИКА
    if mfk.count("11") != 0 and mfk.count("12") != 0 and mfk.count("13") != 0:
        pag.alert("Крестик победил!")
        exit(0)
    elif mfk.count("12") != 0 and mfk.count("22") != 0 and mfk.count("32") != 0:
        pag.alert("Крестик победил!")
        exit(0)
    elif mfk.count("13") != 0 and mfk.count("23") != 0 and mfk.count("33") != 0:
        pag.alert("Крестик победил!")
        exit(0)
    elif mfk.count("11") != 0 and mfk.count("22") != 0 and mfk.count("33") != 0:
        pag.alert("Крестик победил!")
        exit(0)
    elif mfk.count("33") != 0 and mfk.count("22") != 0 and mfk.count("11") != 0:
        pag.alert("Крестик победил!")
        exit(0)
    elif mfk.count("13") != 0 and mfk.count("22") != 0 and mfk.count("31") != 0:
        pag.alert("Крестик победил!")
        exit(0)
    elif mfk.count("31") != 0 and mfk.count("22") != 0 and mfk.count("13") != 0:
        pag.alert("Крестик победил!")
        exit(0)
    elif mfk.count("11") != 0 and mfk.count("21") != 0 and mfk.count("31") != 0:
        pag.alert("Крестик победил!")
        exit(0)
    elif mfk.count("21") != 0 and mfk.count("22") != 0 and mfk.count("23") != 0:
        pag.alert("Крестик победил!")
        exit(0)
    elif mfk.count("31") != 0 and mfk.count("32") != 0 and mfk.count("33") != 0:
        pag.alert("Крестик победил!")
        exit(0)
    #ПРОВЕРКА НОЛИКА
    if mfn.count("11") != 0 and mfn.count("12") != 0 and mfn.count("13") != 0:
        pag.alert("Нолик победил!")
        exit(0)
    elif mfn.count("12") != 0 and mfn.count("22") != 0 and mfn.count("32") != 0:
        pag.alert("Нолик победил!")
        exit(0)
    elif mfn.count("13") != 0 and mfn.count("23") != 0 and mfn.count("33") != 0:
        pag.alert("Нолик победил!")
        exit(0)
    elif mfn.count("11") != 0 and mfn.count("22") != 0 and mfn.count("33") != 0:
        pag.alert("Нолик победил!")
        exit(0)
    elif mfn.count("33") != 0 and mfn.count("22") != 0 and mfn.count("11") != 0:
        pag.alert("Нолик победил!")
        exit(0)
    elif mfn.count("13") != 0 and mfn.count("22") != 0 and mfn.count("31") != 0:
        pag.alert("Нолик победил!")
        exit(0)
    elif mfn.count("31") != 0 and mfn.count("22") != 0 and mfn.count("13") != 0:
        pag.alert("Нолик победил!")
        exit(0)
    elif mfn.count("11") != 0 and mfn.count("21") != 0 and mfn.count("31") != 0:
        pag.alert("Нолик победил!")
        exit(0)
    elif mfn.count("21") != 0 and mfn.count("22") != 0 and mfn.count("23") != 0:
        pag.alert("Нолик победил!")
        exit(0)
    elif mfn.count("31") != 0 and mfn.count("32") != 0 and mfn.count("33") != 0:
        pag.alert("Нолик победил!")
        exit(0)

    nolek = random.randint(1, 3)
    while line1[nolek] != 0:
        nolek = random.randint(1, 3)
    else:
        line1[nolek] = 2
        nolek = "1" + str(nolek)

    mfn.append(nolek)
    if nolek == "11":
        POS11()
        NOLIK0()
    elif nolek == "12":
        POS12()
        NOLIK0()
    elif nolek == "13":
        POS13()
        NOLIK0()
    elif nolek == "21":
        POS21()
        NOLIK0()
    elif nolek == "22":
        POS22()
        NOLIK0()
    elif nolek == "23":
        POS23()
        NOLIK0()
    elif nolek == "31":
        POS31()
        NOLIK0()
    elif nolek == "32":
        POS32()
        NOLIK0()
    elif nolek == "33":
        POS33()
        NOLIK0()

    #ПРОВЕРКА КРЕСИТИКА
    if mfk.count("11") != 0 and mfk.count("12") != 0 and mfk.count("13") != 0:
        pag.alert("Крестик победил!")
        exit(0)
    elif mfk.count("12") != 0 and mfk.count("22") != 0 and mfk.count("32") != 0:
        pag.alert("Крестик победил!")
        exit(0)
    elif mfk.count("13") != 0 and mfk.count("23") != 0 and mfk.count("33") != 0:
        pag.alert("Крестик победил!")
        exit(0)
    elif mfk.count("11") != 0 and mfk.count("22") != 0 and mfk.count("33") != 0:
        pag.alert("Крестик победил!")
        exit(0)
    elif mfk.count("33") != 0 and mfk.count("22") != 0 and mfk.count("11") != 0:
        pag.alert("Крестик победил!")
        exit(0)
    elif mfk.count("13") != 0 and mfk.count("22") != 0 and mfk.count("31") != 0:
        pag.alert("Крестик победил!")
        exit(0)
    elif mfk.count("31") != 0 and mfk.count("22") != 0 and mfk.count("13") != 0:
        pag.alert("Крестик победил!")
        exit(0)
    elif mfk.count("11") != 0 and mfk.count("21") != 0 and mfk.count("31") != 0:
        pag.alert("Крестик победил!")
        exit(0)
    elif mfk.count("21") != 0 and mfk.count("22") != 0 and mfk.count("23") != 0:
        pag.alert("Крестик победил!")
        exit(0)
    elif mfk.count("31") != 0 and mfk.count("32") != 0 and mfk.count("33") != 0:
        pag.alert("Крестик победил!")
        exit(0)
    #ПРОВЕРКА НОЛИКА
    if mfn.count("11") != 0 and mfn.count("12") != 0 and mfn.count("13") != 0:
        pag.alert("Нолик победил!")
        exit(0)
    elif mfn.count("12") != 0 and mfn.count("22") != 0 and mfn.count("32") != 0:
        pag.alert("Нолик победил!")
        exit(0)
    elif mfn.count("13") != 0 and mfn.count("23") != 0 and mfn.count("33") != 0:
        pag.alert("Нолик победил!")
        exit(0)
    elif mfn.count("11") != 0 and mfn.count("22") != 0 and mfn.count("33") != 0:
        pag.alert("Нолик победил!")
        exit(0)
    elif mfn.count("33") != 0 and mfn.count("22") != 0 and mfn.count("11") != 0:
        pag.alert("Нолик победил!")
        exit(0)
    elif mfn.count("13") != 0 and mfn.count("22") != 0 and mfn.count("31") != 0:
        pag.alert("Нолик победил!")
        exit(0)
    elif mfn.count("31") != 0 and mfn.count("22") != 0 and mfn.count("13") != 0:
        pag.alert("Нолик победил!")
        exit(0)
    elif mfn.count("11") != 0 and mfn.count("21") != 0 and mfn.count("31") != 0:
        pag.alert("Нолик победил!")
        exit(0)
    elif mfn.count("21") != 0 and mfn.count("22") != 0 and mfn.count("23") != 0:
        pag.alert("Нолик победил!")
        exit(0)
    elif mfn.count("31") != 0 and mfn.count("32") != 0 and mfn.count("33") != 0:
        pag.alert("Нолик победил!")
        exit(0)

print(line1)
print(line2)
print(line3)

#pag.alert("А кто победил - мне пофиг!!!!!!!!!!!!!!!!! Решайте сами!!!!!!!!!!!!!!!!!!")
tt.exitonclick()