import random
import re
from time import sleep

sim = ("123456")

kos = ""
koss = ""

while True:	
	igr = input("Сколько игроков? " + " \n ")
	if not re.match("[1,2]", igr):
		print("Ошибка! Вы должны указать количество игроков (1, 2)")
		sleep(0.5)
		continue
	else:
		break


if igr == "1":
	print("Бросок ")
	sleep(0.5)
	print(".")
	sleep(0.5)
	print(".")
	sleep(0.5)
	print(".")
	sleep(0.5)
	kos += random.choice(sim)
	print("Выпало число: " + kos)
elif igr == "2":
	a = input("Игрок 1, введите своё имя: ")
	b = input("Игрок 2, введите своё имя: ")
	print("Бросает " + a)
	sleep(0.5)
	print(".")
	sleep(0.5)
	print(".")
	sleep(0.5)
	print(".")
	sleep(0.5)
	kos += str(random.randint(1, 6))
	print("Выпало число: " + kos)
	input("Нажмите Enter")
	print("Бросает " + b)
	sleep(0.5)
	print(".")
	sleep(0.5)
	print(".")
	sleep(0.5)
	print(".")
	sleep(0.5)
	koss += str(random.randint(1, 6))
	print("Выпало число: " + koss)
	sleep(0.5)
	if koss > kos:
		print(b + " победил. Поздравляем!")
	elif koss < kos:
		print(a + " победил. Поздравляем!")
	elif koss == kos:
		print("Ничья")
input()
	





