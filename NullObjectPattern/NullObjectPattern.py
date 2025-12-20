from abc import ABC, abstractmethod


# common interface
class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


# real object
class EmailNotifier(Notifier):
    def send(self, message: str):
        print(f"[EMAIL] {message}")


# null object
class NullNotifier(Notifier):
    def send(self, message: str):
        pass  # do nothing


def get_notifier(enabled: bool) -> Notifier:
    if enabled:
        return EmailNotifier()
    return NullNotifier()  # never returns None


if __name__ == "__main__":
    notifier = get_notifier(False)

    notifier.send("order placed successfully")

    print("application continues safely...")
