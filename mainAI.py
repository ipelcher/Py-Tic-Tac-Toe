import turtle as tt
import pyautogui as pag

print("Привет!")
print("Как")
print("Дела?")
print("Это Игра!")

tt.speed(10000)

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

krestik = pag.prompt(text='Введите код клетки в формате ЛК (Л - Линия, К - Клетка):', title='Код Клетки!' , default='')
mfk.append(krestik)
if krestik == "11":
    POS11()
    CRESTIK()
elif krestik == "12":
    POS12()
    CRESTIK()
elif krestik == "13":
    POS13()
    CRESTIK()
elif krestik == "21":
    POS21()
    CRESTIK()
elif krestik == "22":
    POS22()
    CRESTIK()
elif krestik == "23":
    POS23()
    CRESTIK()
elif krestik == "31":
    POS31()
    CRESTIK()
elif krestik == "32":
    POS32()
    CRESTIK()
elif krestik == "33":
    POS33()
    CRESTIK()

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

nolek = pag.prompt(text='Введите код клетки в формате ЛК (Л - Линия, К - Клетка):', title='Код Клетки!' , default='')
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

krestik2 = pag.prompt(text='Введите код клетки в формате ЛК (Л - Линия, К - Клетка):', title='Код Клетки!' , default='')
mfk.append(krestik2)
if krestik2 == "11":
    POS11()
    CRESTIK()
elif krestik2 == "12":
    POS12()
    CRESTIK()
elif krestik2 == "13":
    POS13()
    CRESTIK()
elif krestik2 == "21":
    POS21()
    CRESTIK()
elif krestik2 == "22":
    POS22()
    CRESTIK()
elif krestik2 == "23":
    POS23()
    CRESTIK()
elif krestik2 == "31":
    POS31()
    CRESTIK()
elif krestik2 == "32":
    POS32()
    CRESTIK()
elif krestik2 == "33":
    POS33()
    CRESTIK()

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

nolek2 = pag.prompt(text='Введите код клетки в формате ЛК (Л - Линия, К - Клетка):', title='Код Клетки!' , default='')
mfn.append(nolek2)
if nolek2 == "11":
    POS11()
    NOLIK0()
elif nolek2 == "12":
    POS12()
    NOLIK0()
elif nolek2 == "13":
    POS13()
    NOLIK0()
elif nolek2 == "21":
    POS21()
    NOLIK0()
elif nolek2 == "22":
    POS22()
    NOLIK0()
elif nolek2 == "23":
    POS23()
    NOLIK0()
elif nolek2 == "31":
    POS31()
    NOLIK0()
elif nolek2 == "32":
    POS32()
    NOLIK0()
elif nolek2 == "33":
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

krestik3 = pag.prompt(text='Введите код клетки в формате ЛК (Л - Линия, К - Клетка):', title='Код Клетки!' , default='')
mfk.append(krestik3)
if krestik3 == "11":
    POS11()
    CRESTIK()
elif krestik3 == "12":
    POS12()
    CRESTIK()
elif krestik3 == "13":
    POS13()
    CRESTIK()
elif krestik3 == "21":
    POS21()
    CRESTIK()
elif krestik3 == "22":
    POS22()
    CRESTIK()
elif krestik3 == "23":
    POS23()
    CRESTIK()
elif krestik3 == "31":
    POS31()
    CRESTIK()
elif krestik3 == "32":
    POS32()
    CRESTIK()
elif krestik3 == "33":
    POS33()
    CRESTIK()

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

nolek3 = pag.prompt(text='Введите код клетки в формате ЛК (Л - Линия, К - Клетка):', title='Код Клетки!' , default='')
mfn.append(nolek3)
if nolek3 == "11":
    POS11()
    NOLIK0()
elif nolek3 == "12":
    POS12()
    NOLIK0()
elif nolek3 == "13":
    POS13()
    NOLIK0()
elif nolek3 == "21":
    POS21()
    NOLIK0()
elif nolek3 == "22":
    POS22()
    NOLIK0()
elif nolek3 == "23":
    POS23()
    NOLIK0()
elif nolek3 == "31":
    POS31()
    NOLIK0()
elif nolek3 == "32":
    POS32()
    NOLIK0()
elif nolek3 == "33":
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

krestik4 = pag.prompt(text='Введите код клетки в формате ЛК (Л - Линия, К - Клетка):', title='Код Клетки!' , default='')
mfk.append(krestik4)
if krestik4 == "11":
    POS11()
    CRESTIK()
elif krestik4 == "12":
    POS12()
    CRESTIK()
elif krestik4 == "13":
    POS13()
    CRESTIK()
elif krestik4 == "21":
    POS21()
    CRESTIK()
elif krestik4 == "22":
    POS22()
    CRESTIK()
elif krestik4 == "23":
    POS23()
    CRESTIK()
elif krestik4 == "31":
    POS31()
    CRESTIK()
elif krestik4 == "32":
    POS32()
    CRESTIK()
elif krestik4 == "33":
    POS33()
    CRESTIK()

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

nolek4 = pag.prompt(text='Введите код клетки в формате ЛК (Л - Линия, К - Клетка):', title='Код Клетки!' , default='')
mfn.append(nolek4)
if nolek4 == "11":
    POS11()
    NOLIK0()
elif nolek4 == "12":
    POS12()
    NOLIK0()
elif nolek4 == "13":
    POS13()
    NOLIK0()
elif nolek4 == "21":
    POS21()
    NOLIK0()
elif nolek4 == "22":
    POS22()
    NOLIK0()
elif nolek4 == "23":
    POS23()
    NOLIK0()
elif nolek4 == "31":
    POS31()
    NOLIK0()
elif nolek4 == "32":
    POS32()
    NOLIK0()
elif nolek4 == "33":
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

krestik5 = pag.prompt(text='Введите код клетки в формате ЛК (Л - Линия, К - Клетка):', title='Код Клетки!' , default='')
mfk.append(krestik5)
if krestik5 == "11":
    POS11()
    CRESTIK()
elif krestik5 == "12":
    POS12()
    CRESTIK()
elif krestik5 == "13":
    POS13()
    CRESTIK()
elif krestik5 == "21":
    POS21()
    CRESTIK()
elif krestik5 == "22":
    POS22()
    CRESTIK()
elif krestik5 == "23":
    POS23()
    CRESTIK()
elif krestik5 == "31":
    POS31()
    CRESTIK()
elif krestik5 == "32":
    POS32()
    CRESTIK()
elif krestik5 == "33":
    POS33()
    CRESTIK()

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

#pag.alert("А кто победил - мне пофиг!!!!!!!!!!!!!!!!! Решайте сами!!!!!!!!!!!!!!!!!!")
tt.exitonclick()