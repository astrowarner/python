class Elevator:
    def __init__(self):
        self.current_floor = 1
        self.requests = []
        self.direction = "up"  # Can be "up" or "down"

    def add_request(self, floor):
        if floor not in self.requests:
            self.requests.append(floor)
            self.requests.sort(reverse=self.direction == "down")
            print(f"Floor {floor} called")

    def move(self):
        # Moving the elevator one floor at a time in the current direction
        if self.direction == "up":
            self.current_floor += 1
        elif self.direction == "down":
            self.current_floor -= 1

        print(f"Current floor: {self.current_floor}, Direction: {self.direction}")

        # Check if the elevator needs to stop at this floor
        if self.current_floor in self.requests:
            self.requests.remove(self.current_floor)
            print(f"Stopping at floor {self.current_floor}")

        # Check for direction change conditions
        if not self.requests:
            return "Idle"
        if (self.current_floor == 20 and self.direction == "up") or \
           (self.current_floor == 1 and self.direction == "down"):
            self.change_direction()

    def change_direction(self):
        # Changing the direction of the elevator
        if self.direction == "up":
            self.direction = "down"
        else:
            self.direction = "up"
        self.requests.sort(reverse=self.direction == "down")
        print(f"Changing direction to {self.direction}")

# Example usage
elevator = Elevator()
elevator.add_request(5)
elevator.add_request(3)
elevator.add_request(10)

while elevator.requests:
    elevator.move()
