# Попросите пользователя ввести два числа с клавиатуры и попросите чтобы он ввел арифметическое действие (+, -, *, /).
# В зависимости от введенного символа выполните математические действия над числами от пользователя.
# Решение задания:

a = float(input("Первое число: "))
b = float(input("Второе число: "))
math_symbol = input("Математическое действие: ")
if math_symbol == "+":
	print ("Получается: ", a + b)
elif math_symbol == "-":
	print ("Получается: ", a - b)
elif math_symbol == "*":
	print ("Получается: ", a * b)
elif math_symbol == "/":
	print ("Получается: ", a / b)
else:
	print ("Вы ввели что-то не то!")





# Попросите пользователя ввести три числа с клавиатуры.
# На основе этих чисел создайте программу, которая будет объединять три значения в список и отдельно в кортеж
# Данные должны объединены через запятую.
# Решение задания:

a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))

lis = [] # Изначально пустой список

lis.append(a)
lis.append(b)
lis.append(c) # Добавление значений в список
print(lis)

tup = (a, b, c) # Создание кортежа
print(tup)




# 1) Выведите числа от 100 до 1 с пропуском чисел 50 и 99. Сделайте это при помощи цикла while.
#
# 2) У вас есть список из чисел:
#
# lis = [1, 34, 8, 0, -5, 7, 32, 74, 59, 92, 41, 10, -2]
# Найдите самый маленький элемент списка и удалите его.
# После этого, если число было меньше 0, то поместите его в конец списка, иначе в начало списка.

i = 100
while i >= 1:
	if i == 50 or i == 99:
		i -= 1
		continue

	print (i)
	i -= 1

# Решение второго задания:

lis = [1, 34, 8, 0, -5, 7, 32, 74, 59, 92, 41, 10, -2]
min = lis[0]
for i in lis:
	if i < min:
		min = i

print ("Минимальное число: ", min)
print ("Список до удаления: ", lis)
lis.remove (min)
print ("Список после удаления: ", lis)
if min < 0:
	lis.append (min)
else:
	lis.insert (0, min)
print ("Список с добавленным элементом: ", lis)




# Создайте функцию с параметрами по умолчанию.
# Вызовите эту функцию и передайте в нее не все параметры.
# Функция должна вернуть деление всех чисел.
# При этом добавьте проверку при делении на ноль.
#Решение задания:

def delenie(a, b, c = 2): # c - необязательный аргумент
	if b != 0 and c != 0:
		return a / b / c # Если все не ноль
	else:
		print ("Деление на ноль!")
		return a

print (delenie (23, 8))




# Создайте файл "example.txt" и впишите туда текст "Привет" после чего закройте его.
# Теперь постарайтесь открыть этот же файл при помощи команды "x", которая открывает файл для чтения, если такого нет.
# Вам будет выдана ошибка, которую вы должны обработать в исключении. Ошибка будет называться FileExistsError.
#Решение задания:

# f = open('example.txt', 'wt')
# f.write('Привет')
# f.close()
#
# try:
# 	f = open('example.txt', 'x')
# 	f.close()
# except FileExistsError:
# 	f = open('example.txt', 'a')
# 	f.close()
# 	print("Сработает открытие через 'a'")
#
# f = open('example.txt', 'wt')
# f.write('Привет')
# f.close()




# При помощи модуля random создайте случайное число.
# В цикле просите пользователя ввести число, если оно не совпадает со случайным числом, то вы должны давать пользователю подсказки.
# Если число является большим, то вы должны написать: «Число что вы пытаетесь угадать больше», - или же наоборот.
# Решение задания:

from random import randint

print('Здравствуйте, попробуйте угадать число  от 0 до 50')

rand = randint(0, 50)
user_try = int(input("Введите число от 0 до 50: "))

while user_try != rand:
	print("Вы не угадали!")
	if user_try > rand:
		print('Число которое вы пытаетесь угадать меньше')
	else:
		print('Число которое вы пытаетесь угадать больше')
	user_try = int(input("Введите число от 0 до 50: "))

print("Вы угадали!")


# Создайте класс Автомобиль. В этом классе создайте несколько переменных, которые будут отвечать за характеристики автомобиля.
# Создайте метод, который будет присваивать значения всем переменным и метод, который будет выводить все переменные на экран.
# Создайте два объекта и используйте оба метода для объектов.
# Решение задания:

class Car:
	brand = ""
    drive_unit = ""
    type_of_drive = ""
    car_body_type = ""
    color = ""

    def __init__(self, brand, drive_unit, type_of_drive, car_body_type, color):
        self.brand = brand
        self.drive_unit = drive_unit
        self.type_of_drive = type_of_drive
        self.car_body_type = car_body_type
        self.color = color

    def printAll(self):
        print('Характеристики автомобиля: \n', 'Марка автомобиля: ', self.brand, '\n Тип привода: ',
              self.drive_unit, '\n Тип трансмиссии: ', self.type_of_drive,  '\n Тип кузова: ', self.car_body_type,
              '\n Цвет машины: ', self.color)


Evo9 = Car('Mitsubishi evolution 9', 'Полный привод', 'Механическая', 'Седан', 'Серый')
Evo9.printAll()

BmwM5 = Car('BMW M5', 'Полный привод', 'Автоматическая', 'Седан', 'Черный')
BmwM5.printAll()




# Сделайте теперь класс Мотоцикл и сделайте его наследником класса Автомобиль.
# Добавьте в него методы, а также свои собственные переменные.
# Создайте объект на основе нового класса и через этот объект обратитесь к методам главного класса Автомобиль.
# Решение задания:


class Car: # Создание класса
	wheels = 4 # Несколько переменных
	model = "Some"
	speed = 123.5

	def set(self, wheels, model, speed): # Создание методов
		self.wheels = wheels
		self.model = model
		self.speed = speed

	def getAll(self):
		print("Автомобиль ", self.model, " может ехать со скоростью ", self.speed, " на всех ", self.wheels, " колесах!")

shkoda = Car() # Первый объект
shkoda.set(4, "Shkoda", 125.45)
shkoda.getAll()

audi = Car() # Второй объект
audi.set(4, "Audi", 250.9)
audi.getAll()

class Car: # Создание класса
	wheels = 4 # Несколько переменных
	model = "Some"
	speed = 123.5

	def set(self, wheels, model, speed): # Создание методов
		self.wheels = wheels
		self.model = model
		self.speed = speed

	def getAll(self):
		print("Автомобиль ", self.model, " может ехать со скоростью ", self.speed, " на всех ", self.wheels, " колесах!")

class Motorcycle (Car):
	engine = "Default"

	def change (self, engine):
		self.engine = engine
		print ("Двигатель мотоцикла установлен как: " + engine)

shkoda = Car() # Первый объект
shkoda.set(4, "Shkoda", 125.45)
shkoda.getAll()

audi = Car() # Второй объект
audi.set(4, "Audi", 250.9)
audi.getAll()

print("") # Просто пропуск строки

harley = Motorcycle()
harley.change("Powerfull")
harley.set(2, "Harley Davidson", 200)
harley.getAll()





# написать декоратор:
def my_shiny_new_decorator(function_to_decorate):
    # Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой,
    # получая возможность исполнять произвольный код до и после неё.
    def the_wrapper_around_the_original_function():
        print("Я - код, который отработает до вызова функции")
        function_to_decorate() # Сама функция
        print("А я - код, срабатывающий после")
    # Вернём эту функцию
    return the_wrapper_around_the_original_function

# Представим теперь, что у нас есть функция, которую мы не планируем больше трогать.
def stand_alone_function():
    print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?")

# Однако, чтобы изменить её поведение, мы можем декорировать её, то есть просто передать декоратору,
# который обернет исходную функцию в любой код, который нам потребуется, и вернёт новую,
# готовую к использованию функцию:
stand_alone_function = my_shiny_new_decorator(stand_alone_function)
stand_alone_function()

list = ['Список']
tupl = ('кортеж')
ax = set('множество')
slovar = {'слов' : 'арь'}
