class Ingredient:
    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __setattr__(self, name, value):
        if name in ('name', 'measure'):
            if not isinstance(value, str):
                raise TypeError()
        if name == 'volume':
            if not isinstance(value, int):
                raise TypeError()
        return super().__setattr__(name, value)

    def __str__(self):
        return f"{self.name}: {self.volume}, {self.measure}"

class Recipe:
    def __init__(self, *args):
        self.ing_list = []
        for x in args:
            if isinstance(x, Ingredient):
                 self.ing_list.append(x)

    def __len__(self):
        return len(self.ing_list)

    def add_ingredient(self, ing):
        # - добавление нового ингредиента ing (объект класса Ingredient) в рецепт (в конец);
        if isinstance(ing, Ingredient):
            self.ing_list.append(ing)

    def remove_ingredient(self, ing):
        # - удаление ингредиента по объекту ing (объект класса Ingredient) из рецепта;
        if isinstance(ing, Ingredient) and ing in self.lst:
            self.lst.remove(ing)

    def get_ingredients(self):
        # - получение кортежа из объектов класса Ingredient текущего рецепта.
        return tuple(self.ing_list)

recipe = Recipe()
recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
ings = recipe.get_ingredients()
[print(x) for x in ings]
n = len(recipe) # n = 3
print(n)


#tests

i1 = Ingredient("Соль", 1, "столовая ложка")
i2 = Ingredient("Мука", 1, "кг")
i3 = Ingredient("Мясо баранины", 10, "кг")
i4 = Ingredient("Масло", 100, "гр")
recipe = Recipe()
recipe = Recipe(i1, i2, i3)
recipe.add_ingredient(i4)
recipe.remove_ingredient(i3)

assert len(recipe) == 3, "функция len вернула неверное значение"
lst = recipe.get_ingredients()
for x in lst:
    assert isinstance(x, Ingredient), "в списке рецептов должны быть только объекты класса Ingredient"
    assert hasattr(x, 'name') and hasattr(x, 'volume') and hasattr(x, 'measure'), "объект класса Ingredient должен иметь атрибуты: name, volume, measure"

assert str(i4) == "Масло: 100, гр", "метод __str__ вернул неверное значение"

i4 = Ingredient("Масло", 120, "гр")
recipe.add_ingredient(i4)
assert len(recipe) == 4, "функция len вернула неверное значение"