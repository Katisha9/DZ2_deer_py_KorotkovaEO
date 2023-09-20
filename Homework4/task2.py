# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление

def create_dict_kwargs(**kwargs):
    return_dict = {}
    for key, value in kwargs.items():
        if value.__hash__ is None:
            return_dict[str(value)] = key
        else:
            return_dict[value] = key
    return return_dict


arg1 = dict(one=1, two=2)
arg2 = 22
arg3 = "bipbip"

print(create_dict_kwargs(arg1=arg1, arg2=arg2, arg3=arg3))