from abc import abstractmethod, ABC


# Component Interface
class Coffee(ABC):

    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass


# Concrete Component
class SimpleCoffee(Coffee):
    def cost(self):
        return 50

    def description(self):
        return "Simple Coffee"


# Decorator Base Class
class CoffeeDecorator(Coffee):
    def __init__(self, my_coffee: Coffee):
        self._coffee = my_coffee

    def cost(self):
        return self._coffee.cost()

    def description(self):
        return self._coffee.description()


# Concrete Decorators
class MilkDecorator(CoffeeDecorator):

    def cost(self):
        return self._coffee.cost() + 20

    def description(self):
        return self._coffee.description() + "+ Milk"


class WhippedCreamDecorator(CoffeeDecorator):

    def cost(self):
        return self._coffee.cost() + 50

    def description(self):
        return self._coffee.description() + "+ Whipped Cream"


class SugarDecorator(CoffeeDecorator):

    def cost(self):
        return self._coffee.cost() + 10

    def description(self):
        return self._coffee.description() + "+ Sugar"


if __name__ == "__main__":
    coffee = SimpleCoffee()
    print(coffee.cost(), coffee.description())
    coffee = MilkDecorator(coffee)
    print(coffee.cost(), coffee.description())
    coffee = WhippedCreamDecorator(coffee)
    print(coffee.cost(), coffee.description())
    coffee = SugarDecorator(coffee)
    print(coffee.cost(), coffee.description())
