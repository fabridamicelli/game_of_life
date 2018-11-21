# Conway's Game of Life
In [Game of Life](<http://en.wikipedia.org/wiki/Conway%27s_Game_of_Life>) the next state of each cell depends on its current state and its number of live neighbors:
 - If a cell is alive: it stays alive if it has 2 or 3 neighbors alive, and dies otherwise. 
 - If a cell is dead: it stays dead unless it has exactly 3 neighbors alive. 
Check [this](http://www.conwaylife.com/wiki/Main_Page) for catalogues of patterns and more.

## Example: "Bouncer"
![Alt Text](https://github.com/fabridamicelli/game_of_life/blob/master/examples/bouncer.gif)

## Requirements
### Animation:
You might have to install ffmpeg. On Ubuntu and Linux Mint:
```
sudo add-apt-repository ppa:mc3man/trusty-media
sudo apt-get update
sudo apt-get install ffmpeg
```
### Python
- Python version >= 3.6
- `numpy` 
- `matplotlib`
- `pytest` (only if you run tests) 

## Testing
To run the tests you must have [py.test](http://pytest.org/latest/) installed. To run the tests, use:
```
make test
```


