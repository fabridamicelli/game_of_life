import random
from typing import List, Tuple, Dict
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from patterns import bouncer, glider_gun

def run_game_np(grid: np.ndarray, n_steps: int=100) -> List:            
    '''
    Run game of life.
    Implementation using numpy.

    Parameters
    ----------
    grid: 2-D ndarray
        Initial grid on which the game runs.
    n_steps: int
        Number of iterations of the game.
    
    Returns
    -------
    time_series: list of 2-D ndarrays
       Time series of grids.        
    '''    
    n_rows, n_cols = grid.shape
    time_series = []    
    for _ in range(n_steps): 
        new_grid = np.zeros_like(grid)
        # Loop over all cells
        for i in range(1, n_rows - 1):
            for j in range(1, n_cols - 1):
                cell_state = grid[i, j]
                neighbors = grid[i - 1: i + 2, j - 1: j + 2]
                n_neighbors_alive = np.sum(neighbors) - cell_state
                # Update cell state
                if cell_state and n_neighbors_alive in (2, 3):
                    new_grid[i, j] = 1
                if not cell_state and n_neighbors_alive == 3:
                    new_grid[i, j] = 1
        
        grid = new_grid        
        time_series.append(grid)

    return time_series    
        
# Pure python implementation
def neighbors(cell: Tuple) -> List:
    i, j = cell
    neighs = [        
        (i - 1, j - 1),
        (i - 1, j),
        (i - 1, j + 1),
        (i, j - 1),        
        (i, j + 1),
        (i + 1, j - 1),
        (i + 1, j),
        (i + 1, j + 1)
    ]
    return neighs

def dict_to_array(grid_dict: Dict) -> np.ndarray:
    ''' map grid from dict representation to ndarray'''
    rows, cols = zip(*grid_dict.keys())        
    n_rows, n_cols = len(set(rows)), len(set(cols))
    grid_array = np.zeros((n_rows, n_cols))
    for (i, j), state in grid_dict.items():
        if state:
            grid_array[i, j] = 1
    return grid_array        

def array_to_dict(grid_array: np.ndarray) -> Dict:
    ''' map grid from ndarray representation to dict'''    
    n_rows, n_cols = grid_array.shape    
    grid_dict = {(i, j): grid_array[i, j]
                for i in range(n_rows)                 
                for j in range(n_cols)}
    return grid_dict            

def run_game_py(grid: Dict, n_steps: int=150) -> List:
    '''
    Run game of life.
    Pure python implementation (no numpy).

    Parameters
    ----------
    grid: dict
        Initial grid on which the game runs. 
        Dict keys -> id of the cell (coordinates).
        Dict values -> state (0/dead, 1/alive)    
    n_steps: int
        Number of iterations of the game.

    Returns
    -------
    time_series: list of dicts
       Time series of grids.    
    '''    
    rows, cols = zip(*grid.keys())        
    n_rows, n_cols = len(set(rows)), len(set(cols))
    time_series = [] 
    for _ in range(n_steps):                 
        new_grid = {(i, j): 0 for i in range(n_rows) for j in range(n_cols)}                                    
                            
        for cell in zip(range(1, n_rows - 1), range(1, n_cols - 1)):                
            n_neighbors_alive = sum([grid[neigh] 
                                    for neigh in neighbors(cell)])                               
            if grid[cell] and n_neighbors_alive in (2, 3):
                new_grid[cell] = 1
            if not grid[cell] and n_neighbors_alive == 3:
                new_grid[cell] = 1    
    
        grid = new_grid
        time_series.append(grid)
        
    return time_series

def animate(time_series: List, filename: str=None) -> None:
    '''
    Create animation and save as mp4 file.
    Animation is save in the working directory unless a filename is specified.    

    Parameters
    ----------
    time_series: list of 2-D ndarrays
        Time series of grids.
    filename: str (optional)
        Complete name of file to save to disk.
    '''
    fig = plt.figure()
    plt.axis('off')
    ims = [[plt.imshow(grid, cmap='binary', interpolation='none', animated=True)]                       
            for grid in time_series]

    ani = animation.ArtistAnimation(fig, ims, interval=100, blit=True, 
                                    repeat_delay=100)
                                    
    if filename:
        ani.save(f'{filename}.mp4')
    else:
        ani.save('gameoflife.mp4')


