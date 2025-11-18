from abc import ABC, abstractmethod


# Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, product_name):
        pass


# Subject Interface
class Subject(ABC):
    @abstractmethod
    def register(self, observer: Observer):
        pass

    @abstractmethod
    def remove(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass


# Concrete Subject
class Product(Subject):
    def __int__(self, product_name):
        self.observers = []
        self.productName = product_name
        self.inStock = False

    def register(self, observer: Observer):
        self.observers.append(observer)

    def remove(self, observer: Observer):
        self.observers.remove(observer)

    def setAvailability(self):
        previously = self.inStock
        self.inStock = True

        if not previously and self.inStock:
            print(f"{self.productName} is available now")
            self.notify()

    def notify(self):
        for observer in self.observers:
            observer.update(self.productName)


# Concrete Observer
class User(Observer):
    def __init__(self, user):
        self.user = user

    def update(self, product_name):
        print(f"{product_name} is available now")


if __name__ == "__main__":
    pass


