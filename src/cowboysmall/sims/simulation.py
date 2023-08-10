

class Simulation:

    def __init__(self, data: dict):
        self.data = data

    def step(self, iteration: int, data: dict) -> None:
        pass

    def run(self, iterations: int):
        for iteration in range(iterations):
            self.step(iteration, self.data)

        return self.data
