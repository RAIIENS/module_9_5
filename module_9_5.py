# Создаём пользовательский класс исключения StepValueError
class StepValueError(ValueError):
    pass
# Создаём класс итератора
class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start

    def __iter__(self):
        self.pointer = self.start  # Сброс указателя на start
        return self

    def __next__(self):
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration  # Завершение итерации
        current_value = self.pointer
        self.pointer += self.step  # Увеличиваем указатель на step
        return current_value

# Пример использования
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

# Создаём другие итераторы
iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

# Итерация по каждому из итераторов
for i in iter2:
    print(i, end=' ')
print()

for i in iter3:
    print(i, end=' ')
print()

for i in iter4:
    print(i, end=' ')
print()

for i in iter5:
    print(i, end=' ')
print()

# Пояснение:
# Имеем класс исключения StepValueError.
# Создаём пустой класс, наследуемый от ValueError, который будет использоваться для обработки
# ошибок, связанных с шагом.
# Далее смотрим класс итератора Iterator:
# Конструктор __init__ принимает параметры start, stop и step. Если step равен 0, выбрасывается
# исключение StepValueError.
# Метод __iter__ сбрасывает указатель pointer на значение start и возвращает сам объект
# итератора.
# Метод __next__ проверяет, достиг ли указатель pointer предела (stop). Если достиг,
# выбрасывается исключение StopIteration, чтобы завершить итерацию. В противном случае
# возвращается текущее значение pointer, и он увеличивается на значение step.
#
# Пример использования:
#
# Создаются итераторы с различными параметрами, и по каждому из них выполняется
# итерация с выводом значений.
#
# Пример вывода:
#
# Шаг указан неверно
# -5 -4 -3 -2 -1 0 1
# 6 8 10 12 14
# 5 4 3 2 1

# В случае iter5 = Iterator(10, 1) любой следующий элемент после 10
# должен быть >9. Иначе этот итератор выбрасывается. Поэтому мы его и не видим в выводе значений.