"""class MyException(Exception):  # Некоректное входное значение
    def __init__(self, text):
        super().__init__(text)


try:
    print("My")
except MyException as arr:
    print(err)"""

def my_iter(obj):
    for i in obj:
        yield i

l1 = [1,2,3,4,5,6,7,]

iterator_object = my_iter(l1)

print(next(iterator_object))
print(next(iterator_object))
print(next(iterator_object))
print(next(iterator_object))


