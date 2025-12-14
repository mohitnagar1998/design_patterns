class Handler:
    def __init__(self, next_handler=None):
        self.next = next_handler

    def handle(self, request):
        if self.next:
            return self.next.handle(request)

class LowLevelHandler(Handler):
    def handle(self, request):
        if request < 10:
            return f"LowLevelHandler processec {request}"
        return super().handle(request)

class MidLevelHandler(Handler):
    def handle(self, request):
        if 10 <= request < 20:
            return f"MidLevelHandler processed {request}"
        return super().handle(request)

class HighLevelHandler(Handler):
    def handle(self, request):
        if request >= 20:
            return f"HighLevelHandler processed {request}"
        return super().handle(request)


if __name__ == "__main__":
    # Build Chain
    chain = LowLevelHandler(MidLevelHandler(HighLevelHandler()))

    print(chain.handle(5))
    print(chain.handle(15))
    print(chain.handle(25))

