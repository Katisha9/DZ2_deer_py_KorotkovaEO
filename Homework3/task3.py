# 4. Создайте словарь со списком вещей для похода в качестве ключа и их массой в
# качестве значения. Определите какие вещи влезут в рюкзак, передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

max_weight = int(input('Введите максимальную грузоподъемность рюкзака в кг: '))
def fill_backpack(items, max_weight):
    sorted_items = sorted(items.items(),
                          key=lambda x: -x[1],
                          reverse=True)
    backpack = {}

    for k, v in sorted_items:
        if v <= max_weight:
            backpack.update({k: v})
            max_weight -= v
    return backpack


items = {'палатка': 4, 'спальник': 2, 'еда': 3, 'вода': 1}

print(*fill_backpack(items, max_weight))