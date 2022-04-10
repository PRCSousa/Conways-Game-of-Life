# Conway's Game of Life

This is a basic implementation of Conway's Game of Life ruleset, visualized with the pygame library of a grid:

- Each square represents a cell, and, just like life, they can birth, reproduce, and die.
    - Any live cell with 1 or less live neighbours dies.
    - Any live cell with more than three live neighbours dies.
    - Any dead cell with exactly three live neighbours becomes a live cell.
    - Any cell with two or three neighbours live on to the next generation.

## How to play: ##

   Run the program, in the console you're gonna be asked for the grid size. Click the grid to set the cells you desire and press SPACE to move to the next generation, or ENTER pass generations automatically.
