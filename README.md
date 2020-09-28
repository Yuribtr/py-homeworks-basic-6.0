# Задание 6.1 + продолжение

## Домашнее задание к лекции «Объекты и классы. Взаимодействие между ними»

Задача №1 "Ферма Дядюшки Джо"

Вы приехали помогать на ферму Дядюшки Джо и видите вокруг себя множество разных животных:

    гусей "Серый" и "Белый"
    корову "Маньку"
    овец "Барашек" и "Кудрявый"
    кур "Ко-Ко" и "Кукареку"
    коз "Рога" и "Копыта"
    и утку "Кряква" ​ Со всеми животными вам необходимо как-то взаимодействовать:
    кормить
    корову и коз доить
    овец стричь
    собирать яйца у кур, утки и гусей
    различать по голосам(коровы мычат, утки крякают и т.д.) ​

Задание 1:

Нужно реализовать классы животных и определить методы взаимодействия с животными ​Для каждого животного из списка должен существовать экземпляр класса. Каждое животное требуется накормить и подоить/постричь/собрать яйца, если надо. ​
Задание 2:

У каждого животного должно быть определено имя(self.name) и вес(self.weight).

    Необходимо посчитать общий вес всех животных(экземпляров класса);
    Вывести название самого тяжелого животного.

## Задача №1 "Ферма Дядюшки Джо". Продолжение.
У всех животных есть общее поведение. Каждое животное можно накормить. Каждое животное может подать голос.
Но есть поведение, принадлежащее только определенным животным. Например, собирать яйца можно только с кур, утки и гусей.  

## Задание 1:
Реализовать родительский класс для всех животных и вынести общее поведение в него.  
От родительского класса должны будут отнаследоваться все остальные животные.  
В родительском классе должно быть 2-3 общих класса и общие поля.

## Задание 2:
Используя методы из родительского класса, вызывать их в цикле у списка всех животных.