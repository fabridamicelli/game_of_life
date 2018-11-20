import sys; sys.path.append('/home/icns-fd/Dropbox/code/game_of_life')
import random
import numpy as np

from main import run_game_np, run_game_py, array_to_dict, dict_to_array, animate
from patterns import bouncer, glider_gun

def make_rand_grid_dict():
    grid = {(i, j): 0
        for i in range(50) 
        for j in range(50)}
    for (i, j), _ in grid.items():
        if random.random() > 0.5: 
            grid[(i, j)] = 1
    return grid

def make_rand_grid_np():
    return np.random.randint(2, size=(50, 50))

def test_dict_to_array():
    grid = make_rand_grid_dict()
    assert array_to_dict(dict_to_array(grid)) == grid

def test_array_to_dict():
    grid = make_rand_grid_np()
    assert (dict_to_array(array_to_dict(grid)) == grid).all()

def test_np_vs_py():
    grid = make_rand_grid_np()
    steps = 1
    run_np = run_game_np(grid.copy(), n_steps=steps)
    run_py = run_game_py(grid.copy(), n_steps=steps)    
    assert len(run_np) == len(run_py)
    assert sum([(a == b).all()
               for a, b in zip(run_np, run_py)]) == len(run_np)

    