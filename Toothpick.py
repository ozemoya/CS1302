from graphics import Line, Point

class Toothpick:
    length = 63  # Defined length of each toothpick

    def __init__(self, x, y, direction):
        self.direction = direction
        if self.direction == "horizontal":
            self.ax = x - Toothpick.length // 2
            self.bx = x + Toothpick.length // 2
            self.ay = y
            self.by = y
        else:  # Vertical orientation
            self.ax = x
            self.bx = x
            self.ay = y - Toothpick.length // 2
            self.by = y + Toothpick.length // 2

    def display(self, window):
        # Draws the toothpick on the provided graphical window
        line = Line(Point(self.ax, self.ay), Point(self.bx, self.by))
        line.draw(window)

    def intersects_with(self, x, y):
        # Checks if the toothpick intersects with the given point (x, y)
        return self.ax == x and self.by == y or self.bx == x and self.ay == y

    def add_toothpick_end_a(self, existing_toothpicks):
        # Adds a new toothpick at end A if possible
        if self.is_end_available(self.ax, self.ay, existing_toothpicks):
            direction = "vertical" if self.direction == "horizontal" else "horizontal"
            return Toothpick(self.ax, self.ay, direction)
        return None

    def add_toothpick_end_b(self, existing_toothpicks):
        # Adds a new toothpick at end B if possible
        if self.is_end_available(self.bx, self.by, existing_toothpicks):
            direction = "vertical" if self.direction == "horizontal" else "horizontal"
            return Toothpick(self.bx, self.by, direction)
        return None

    def is_end_available(self, x, y, existing_toothpicks):
        # Checks if a new toothpick can be added at a given end without intersecting others
        for toothpick in existing_toothpicks:
            if toothpick != self and toothpick.intersects_with(x, y):
                return False
        return True
