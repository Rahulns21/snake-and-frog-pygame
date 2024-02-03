# Snake and Frog Game with Pygame

Welcome to the Snake and Frog Game built using the Pygame module in Python! This classic arcade-style game allows you to control a snake that grows longer as it consumes frogs while avoiding collisions with the walls and itself.

## Prerequisites

Before running the game, make sure you have the following installed:

- Python (>=3.6)
- Pygame module (`pip install pygame`)

## How to Play

1. Clone this repository:

    ```bash
    git clone https://github.com/Rahulns21/snake-and-frog-pygame.git
    ```

2. Navigate to the project directory:

    ```bash
    cd snake-and-frog-pygame
    ```

3. Run the game:

    ```bash
    python main.py
    ```

4. Use the arrow keys to control the snake:
   - UP arrow: Move the snake upward
   - DOWN arrow: Move the snake downward
   - LEFT arrow: Move the snake left
   - RIGHT arrow: Move the snake right

5. Eat the frogs (blue in color) to grow longer and earn points.

6. Avoid collisions with the walls and the snake's own body.

7. The game ends when the snake collides with the walls or itself.

## Features

- **Score:** The score increases every time the snake eats a frog.
- **Speed:** The snake's speed gradually increases as it eats more frogs.
- **Game Over:** Displays a Game Over message when the snake collides with the walls or itself.
- **Restart:** Press the "R" key to restart the game after it's over.

## Customization

Feel free to customize the game by modifying the following parameters in the `main.py` file:

- Set the initial size of the snake.
- Control the frames per second (FPS) to adjust the game speed.
- Customize the colors of the snake, frogs, and background.

## Acknowledgments

This Snake and Frog Game is built using the Pygame module, a set of Python modules designed for writing video games. Thanks to the Pygame community for providing a versatile framework for creating interactive games.

Enjoy the game and happy coding!
