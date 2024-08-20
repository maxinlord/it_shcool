from typing import Any


class MeansOfTransport:
    def __init__(self, color, brand) -> None:
        self.__color = color
        self.__brand = brand
    
    def show_color(self):
        print(self.color)
    
    def show_brand(self):
        print(self.brand)
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color = color
    
    @property
    def brand(self):
        return self.__brand
    
    @brand.setter
    def brand(self, brand):
        self.__brand = brand


class Car(MeansOfTransport):
    car_drive = 4

    def __init__(self, color, brand, wheels) -> None:
        super().__init__(color, brand)
        self.__wheels = wheels
    
    @classmethod
    def show_car_drive(cls):
        print(cls.car_drive)

class Moped(MeansOfTransport):
    def __init__(self, color, brand, wheels) -> None:
        super().__init__(color, brand)
        self.__wheels = wheels

    @staticmethod
    def time_spent_on_road(distance, speed):
        return distance / speed



class Calculator:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    
class Concatenate(Calculator):
    def add(self):
        return str(self.a) + str(self.b)




class Animals:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def voice(self):
        raise NotImplementedError("Subclasses must implement this method")
    

class Cat(Animals):
    def voice(self):
        return "Meow"
    

class Dog:
    __isinstance = None

    def __new__(cls, *args, **kwargs):
        if cls.__isinstance is None:
            cls.__isinstance = super().__new__(cls)
        return cls.__isinstance

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    

class Humans:
    def __init__(self, list_human: list) -> None:
        self.humans = list_human
    
    def add_human(self, human):
        self.humans.append(human)
    
    def __str__(self) -> str:
        return str(self.humans)
    
    def __iter__(self):
        return iter(self.humans)




class Point:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
    
    def __setattr__(self, key: str, value) -> Any:
        old_value = self.__dict__.get(key)
        print(f'{old_value}->{value}')
        object.__setattr__(self, key, value)

