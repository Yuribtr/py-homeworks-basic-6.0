from abc import abstractmethod


class Animal:
    def __init__(self, name='', weight=0):
        # Making all fields private to prevent access from outside of class
        self.__name = name
        self.__weight = weight

    def feed(self, food_qty):
        self.__weight += food_qty

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_weight(self):
        return self.__weight

    # making abstract method to prevent instantiate from this class
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def make_specific_class_actions(self):
        pass

    @abstractmethod
    def get_type(self):
        pass

class MilkingAnimal(Animal):
    def do_milk(self):
        return 'доится'

    def make_specific_class_actions(self):
        return self.do_milk() + ' и делает ' + self.make_sound()

    @abstractmethod
    def make_sound(self):
        pass


class WoolenAnimal(Animal):
    def do_shave(self):
        return 'стрижет шерсть'

    def make_specific_class_actions(self):
        return self.do_shave() + ' и делает ' + self.make_sound()

    @abstractmethod
    def make_sound(self):
        pass


class LayingAnimal(Animal):
    def do_lay(self):
        return 'несет яйца'

    def make_specific_class_actions(self):
        return self.do_lay() + ' и делает ' + self.make_sound()

    @abstractmethod
    def make_sound(self):
        pass


class Goose(LayingAnimal):
    __type = 'Гусь'

    def get_type(self):
        return self.__type

    def make_sound(self):
        return 'га-га'


class Cow(MilkingAnimal):
    __type = 'Корова'

    def get_type(self):
        return self.__type

    def make_sound(self):
        return 'му-му'


class Sheep(WoolenAnimal, MilkingAnimal):
    __type = 'Овца'

    def get_type(self):
        return self.__type

    def make_sound(self):
        return 'бе-бе'

    def make_specific_class_actions(self):
        return super().do_shave() + ', ' + super().do_milk() + ' и делает ' + self.make_sound()


class Hen(LayingAnimal):
    __type = 'Курица'

    def get_type(self):
        return self.__type

    def make_sound(self):
        return 'ко-ко'


class Goat(MilkingAnimal, WoolenAnimal):
    __type = 'Коза'

    def get_type(self):
        return self.__type

    def make_sound(self):
        return 'ме-ме'

    def make_specific_class_actions(self):
        return super().do_shave() + ', ' + super().do_milk() + ' и делает ' + self.make_sound()


class Duck(LayingAnimal):
    __type = 'Утка'

    def get_type(self):
        return self.__type

    def make_sound(self):
        return 'кря-кря'


farm = [Goose('Серый', 4),
        Goose('Белый', 5),
        Cow('Манька', 200),
        Sheep('Барашек', 10),
        Sheep('Кудрявый', 12),
        Hen('Ко-Ко', 2),
        Hen('Кукареку', 1),
        Goat('Рога', 30),
        Goat('Копыта', 25),
        Duck('Кряква', 3)]

for animal in farm:
    animal.feed(1)
    print(animal.get_type() + ' "' + animal.get_name() + '" ' + animal.make_specific_class_actions())

total_weight = 0

if len(farm) > 0:
    # setting first animal as heaviest by default
    heaviest_animal = farm[0] if len(farm) > 0 else None
    for animal in farm:
        total_weight += animal.get_weight()
        heaviest_animal = animal if heaviest_animal.get_weight() < animal.get_weight() else heaviest_animal

    print(f'\nОбщий вес животных на ферме: {total_weight}')
    print(f'Самое тяжелое животное: {heaviest_animal.get_name()}')
else:
    print(f'\nНа ферме никого нет!')
