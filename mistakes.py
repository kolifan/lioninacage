# ======= 1 ======
# def greet(name):
#     return f"Hello, {name}"
#
# print(greet(name="Ann", lang="en"))
#
# Совершенно непонятный аргумент lang. Зачем он тут? Исправляем:

def greet(name):
    return f"Hello, {name}"

print(greet(name="Ann"))

# ======= 2 ======
# def total(*args):
#     return sum(args)
#
# def wrapper(values):
#     return total(values)
#
# print(wrapper([1, 2, 3]))
#
# Функция total ждёт отдельные аргументы, а не список, который ей пытаются передать. Значит, список сначала надо распаковать и получить из него отдельные значения.

def total(*args):
    return sum(args)

def wrapper(values):
    return total(*values)

print(wrapper([1, 2, 3]))

# ======= 3 ======
# def greet(name, punctuation="!"):
#     return "Hi, " + name + punctuation
#
# def greet_with_options(name, **kwargs):
#     return greet(name, kwargs)
#
# print(greet_with_options("Bob", punctuation="???"))
#
# Здесь в функцию greet в качестве второго аргумента передаётся не то, что нужно. Функция ждёт строку, а приходит словарь. Исправляем так:

def greet(name, punctuation="!"):
    return "Hi, " + name + punctuation

def greet_with_options(name, **kwargs):
    return greet(name, kwargs.get("punctuation"))

print(greet_with_options("Bob", punctuation="???"))

# ======= 4 ======
# def show(kwargs, **kwargs):
#     print(kwargs)
#
# Здесь ошибка видна сразу: duplicate parametr name. Исправляем, например, так:

def show(kwargs1, **kwargs):
    print(kwargs)

# ======= 5 ======
# def add_item(x, items=[]):
#     items.append(x)
#     return items
#
# print(add_item(1))
# print(add_item(2))
#
# Здесь ошибок нет, но функция ведёт себя не так, как ожидается на первый взгляд. Для ожидаемых результатов лучше сделать так:

def add_item(x, items=None):
    if items==None:
        items = []

    items.append(x)
    return items

print(add_item(1))
print(add_item(2))