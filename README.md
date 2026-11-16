# Snake_Game
Classic Snake game in Python using the turtle module, with score, high score, game over, pause and quit controls.
This is a classic Snake game made with Python’s turtle module. You move the snake around the screen, eat the red food to grow longer, and try to get the highest score without hitting a wall or your own body.

What the game has

The snake moves in steps on a grid, and the food always appears on that same grid. Each time you eat, a new piece is added to the tail and your score goes up by 10. The score and the high score are shown at the top, and the game gets a little faster with each food. If you hit a wall or yourself, “Game Over” appears, the game resets, and your high score stays. You can also pause and resume the game, and quit it with one key.

Controls

Use the arrow keys or W, A, S, D to move. Press the space bar to pause and resume. Press Esc to quit. The snake cannot turn straight back into itself.

How to run it

Install Python 3. The turtle, time and random modules come with Python, so you don’t need to install anything else. Download the file snake.py, open a terminal in the same folder, and type: python snake.py

How it works

A loop runs about ten times every second. In each round, it updates the screen, checks whether the snake ate the food, moves the tail, moves the head, and checks for crashes. The tail pieces are kept in a list. Each piece jumps to the spot of the piece in front of it, and the first piece jumps to where the head was. Crashes are found by measuring the distance between the head and the other objects, and by checking the head’s position against the edges of the window.

What I learned

I practiced using variables, lists, loops and functions together in one program. I also learned how to handle keyboard presses, detect collisions, and fix bugs, especially indentation mistakes.

Ideas for later

Save the high score in a file, rewrite the game using classes, and add levels or obstacles.

About me

I built this in my first semester of Computer Science and Engineering.
