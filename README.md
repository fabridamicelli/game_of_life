# Conway's Game of Life
In Game of Life the next state of each cell depends on its current state and its number of live neighbors. If a cell is alive, it stays alive if it has 2 or 3 neighbors, and dies otherwise. If a cell is dead, it stays dead unless it has exactly 3 neighbors.
For more info and interesting examples: <http://en.wikipedia.org/wiki/Conway%27s_Game_of_Life>

## Requirements
For animation to work you might have to install ffmpeg. On Ubuntu and Linux Mint, the following should work.
  $ sudo add-apt-repository ppa:mc3man/trusty-media
  $ sudo apt-get update
  $ sudo apt-get install ffmpeg

## Example: "Bouncer"
![Alt Text](https://github.com/fabridamicelli/game_of_life/blob/master/examples/bouncer.gif)
