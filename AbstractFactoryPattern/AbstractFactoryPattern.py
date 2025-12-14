from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self):
        pass


class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass


class WindowsButton(Button):
    def render(self):
        print("rendering windows button")


class MacButton(Button):
    def render(self):
        print("rendering mac button")


class WindowsCheckbox(Checkbox):
    def render(self):
        print("rendering windows checkbox")


class MacCheckbox(Checkbox):
    def render(self):
        print("rendering mac checkbox")


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()


def build_ui(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    button.render()
    checkbox.render()


if __name__ == "__main__":
    os_type = input("enter os type").lower()
    if os_type == "windows":
        factory = WindowsFactory()

    elif os_type == "mac":
        factory = MacFactory()

    else:
        raise ValueError("unsupported os")

    build_ui(factory)

