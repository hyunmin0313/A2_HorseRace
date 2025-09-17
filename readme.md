# COMP1020_A2
## Horse Race Simulation

### 1. Project Description

This project implements a **Horse Race Simulator** in Python.
It demonstrates **Object-Oriented Programming (OOP)** concepts, uses **random number generation** with a dice, and visualizes the race using the `graphics.py` library.



### 2. Horse Class (Horse.py)

* **Attributes**
  * `x, y` : Horse position (horizontal = movement, vertical = lane)
  * `image` : Image object for the horse
  * `dice` : Dice object to determine step size
  * `window` : Graphics window object
    
* **Methods**
  * `__init__(self, speed, y, image_file, window)` : Initialize attributes
  * `move(self)` : Roll the dice and update position
  * `draw(self)` : Draw the horse on the graphics window
  * `crossed_finish_line(self, x)` : Check if the horse has crossed the finish line
    
### 3. Simulation Flow

1. A `700x350` graphics window is created.
2. Two horses are displayed at the starting line.
3. The race starts when the user clicks the mouse.
4. Horses move forward by rolling the dice (random step size).
5. The race ends when one or both horses cross the finish line.
6. Winner (or tie) is displayed.
7. Final mouse click closes the window.



Would you like me to also add a **sample screenshot section** (with placeholders, e.g. `![Race Screenshot](screenshot.png)`) so your README looks even more polished on GitHub?
