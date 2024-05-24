import random

my_schet = 0
computer_schet = 0
vubor = ["камень","ножницы","бумага"]
my_motion = ""
computer_motion = ""

print("Добро пожаловать в игру 'Камень,ножницы,бумага'. Для хода введите цифры: 1-камень, 2-ножницы, 3-бумага")

while (my_schet != 3) and (computer_schet !=3):
    my_motion = int(input())
    if not(0 < my_motion < 4):
        print("Ошибочный ввод. Введите заново.")
        my_motion = int(input())
    computer_motion = random.randint(0, 2)
    if my_motion == 1 and computer_motion == 1:
        my_schet += 1

    if my_motion == 1 and computer_motion == 2:
        computer_schet += 1

    if my_motion == 2 and computer_motion == 0:
        computer_schet += 1

    if my_motion == 2 and computer_motion == 2:
        my_schet += 1

    if my_motion == 3 and computer_motion == 0:
        my_schet += 1

    if my_motion == 3 and computer_motion == 1:
        computer_schet += 1
    if my_motion == 1:
        print('Your choice: камень', '\n' + 'Computer choice:', vubor[computer_motion])
    elif my_motion == 2:
        print('Your choice: ножницы', '\n' + 'Computer choice:', vubor[computer_motion])
    elif my_motion == 3:
        print('Your choice: бумага', '\n' + 'Computer choice:', vubor[computer_motion])
    print('YOU', ":", my_schet, "|", 'COMPUTER', computer_schet)

if my_schet > computer_schet:
    print("Счёт", my_schet, ":", computer_schet, "\n" + "Вы победили")
else:
    print("Счёт", my_schet, ":", computer_schet, "\n" + "Вы проиграли")