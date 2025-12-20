class EmailNotifier:
    def send(self, message: str):
        print(f"[EMAIL] {message}")


def get_notifier(enabled: bool):
    if enabled:
        return EmailNotifier()
    return None


if __name__ == "__main__":
    notifier = get_notifier(True)

    if notifier is not None:
        notifier.send("order placed successfully")

    print("application continues...")