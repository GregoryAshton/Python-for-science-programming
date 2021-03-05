import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches


class Square(object):
    def __init__(self):
        self.width = 1
        self.height = 1
        self.left = 0
        self.bottom = 0
        self.color = "C0"
        self.transparency = 0.3

    def contains(self, x, y):
        left = self.left
        right = left + self.width
        bottom = self.bottom
        top = bottom + self.height
        if left < x < right and bottom < y < top:
            return True
        else:
            return False

    def draw(self, ax):
        patch = matplotlib.patches.Rectangle(
            (self.left, self.bottom),
            self.width,
            self.height,
            alpha=self.transparency,
            color=self.color,
            zorder=-1000
        )
        ax.add_patch(patch)
        return ax


class Circle(object):
    def __init__(self):
        self.centrex = 0.5
        self.centrey = 0.5
        self.diameter = 1
        self.radius = self.diameter / 2
        self.color = "C1"
        self.transparency = 0.3

    def contains(self, x, y):
        xp = x - self.centrex
        yp = y - self.centrey
        if xp ** 2 + yp ** 2 < self.radius ** 2:
            return True
        else:
            return False

    def draw(self, ax):
        patch = matplotlib.patches.Circle(
            (self.centrex, self.centrey),
            self.radius,
            alpha=self.transparency,
            color=self.color,
            zorder=-100
        )
        ax.add_patch(patch)
        return ax


def draw_square_and_circle(square, circle):
    fig, ax = plt.subplots()
    square.draw(ax)
    circle.draw(ax)
    ax.set_xlim(-0.2, 1.2)
    ax.set_ylim(-0.2, 1.2)
    ax.set_aspect("equal")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    return fig, ax


square = Square()
circle = Circle()
