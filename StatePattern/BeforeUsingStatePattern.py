class TrafficLight:
    def __init__(self):
        self.state = "RED"

    def change(self):
        if self.state == "RED":
            print("RED - Stop")
            self.state = "YELLOW"

        elif self.state == "GREEN":
            print("GREEN - Go")
            self.state = "RED"

        elif self.state == "YELLOW":
            print("YELLOW - Ready")
            self.state = "GREEN"

        else:
            raise ValueError("Invalid traffic light state")


if __name__ == "__main__":
    traffic_light = TrafficLight()

    for _ in range(6):
        traffic_light.change()
