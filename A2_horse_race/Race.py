import Dice
import graphics
import time

class Horse:
    def __init__(self, speed, y, image, window):
        self.x_pos = 50
        self.y_pos = y
        self.image = graphics.Image(graphics.Point(self.x_pos,self.y_pos),image)
        self.window = window
        self.dice = Dice.Dice(speed)

    def move(self):
        step = self.dice.roll()
        self.x_pos += step
        self.image.move(step, 0 )


    def draw(self):
        self.image.draw(self.window)

    def crossed_finish_line(self, x =650):
        if self.x_pos >= x:
            return True
        return False


def main():
    window = graphics.GraphWin("background", 700, 350)
    finish_x = 650
    finish_line = graphics.Line(graphics.Point(650,0),graphics.Point(650,350))
    horse_1 = Horse(9,100,"Knight.gif", window)
    horse_2 = Horse(10,200,"Wizard.gif", window)

    finish_line.draw(window)
    horse_1.draw()
    horse_2.draw()
    window.getMouse()
    winner = None
    while winner == None:
        horse_1.move()
        horse_2.move()

        if horse_1.crossed_finish_line(finish_x) and horse_2.crossed_finish_line(finish_x):
            print("tie")
            window = "Tie"
        elif horse_1.crossed_finish_line(finish_x):
            winner = "Horse 1"
        elif horse_2.crossed_finish_line(finish_x):
            winner = "Horse 2"
        time.sleep(0.002)

    print(f"Winner  = {winner}")
    window.getMouse()
    window.close()


if __name__ == "__main__":
    main()



