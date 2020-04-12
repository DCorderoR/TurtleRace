import turtle
import random


class Circuit():
    runners = []
    __posStartY = (-30, -10, 10, 30)
    __colorTurtle = ("Red", "Blue", "Green", "Orange")

    def __init__(self, width, height):
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor("lightgray")
        self.__startLine = - width / 2 + 20
        self.__finishLine = width / 2 - 20

        self.__createRunners()

    def __createRunners(self):
        for i in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.color(self.__colorTurtle[i])
            new_turtle.shape("turtle")
            new_turtle.penup()
            new_turtle.setpos(self.__startLine, self.__posStartY[i])

            self.runners.append(new_turtle)

    def compete(self):
        winner = False

        while not winner:
            for Turtle in self.runners:
                advance = random.randint(1, 6)
                Turtle.forward(advance)

                if Turtle.position()[0] >= self.__finishLine:
                    winner = True
                    print("{} turtle win".format(Turtle.color()[0]))
                    break


if __name__ == "__main__":
    circuit = Circuit(640, 480)
    circuit.compete()