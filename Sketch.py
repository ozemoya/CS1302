from Toothpick import Toothpick
from graphics import GraphWin
import sys

def run_simulation():
    iterations = int(sys.argv[1])
    window_size = 1000
    window_title = "Toothpick Simulation"
    window = GraphWin(window_title, window_size, window_size)
    window.setBackground("white")

    midpoint_x = window.width / 2
    midpoint_y = window.height / 2

    initial_toothpick = Toothpick(midpoint_x, midpoint_y, "horizontal")
    toothpicks = [initial_toothpick]
    new_toothpicks = []
    total_toothpicks = 1

    for iteration in range(iterations):
        if iteration == 0:
            print(f"Iteration #0: New toothpicks: 1, Total: 1")
        else:
            print(f"Iteration #{iteration}: New toothpicks: {len(new_toothpicks)}, Total: {total_toothpicks}")

        new_toothpicks = []
        index = 0

        while index < len(toothpicks):
            toothpicks[index].display(window)
            toothpick_end_a = toothpicks[index].add_toothpick_end_a(toothpicks)
            toothpick_end_b = toothpicks[index].add_toothpick_end_b(toothpicks)

            if toothpick_end_a is not None:
                new_toothpicks.append(toothpick_end_a)
            if toothpick_end_b is not None:
                new_toothpicks.append(toothpick_end_b)

            index += 1

        toothpicks.extend(new_toothpicks)
        total_toothpicks += len(new_toothpicks)

    window.getMouse()  # Wait for mouse click before closing
    window.close()

if __name__ == "__main__":
    run_simulation()
