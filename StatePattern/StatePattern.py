from abc import ABC, abstractmethod


# interface
class TrafficLightState(ABC):
    @abstractmethod
    def next(self, context):
        pass

    @abstractmethod
    def get_colour(self):
        pass


# concrete classes
class RedState(TrafficLightState):
    def next(self, context):
        context.set_state(YellowState())

    def get_colour(self):
        return "RED -> Stop"


class GreenState(TrafficLightState):
    def next(self, context):
        context.set_state(RedState())

    def get_colour(self):
        return "GREEN -> Go"


class YellowState(TrafficLightState):
    def next(self, context):
        context.set_state(GreenState())

    def get_colour(self):
        return "Yellow -> Ready"


# context
class TrafficLight:
    def __init__(self):
        self._state = RedState()  # initial state

    def set_state(self, state: TrafficLightState):
        self._state = state

    def change_state(self):
        print(self._state.get_colour())
        self._state.next(self)


# client code
if __name__ == "__main__":
    traffic_light = TrafficLight()
    for _ in range(6):
        traffic_light.change_state()
