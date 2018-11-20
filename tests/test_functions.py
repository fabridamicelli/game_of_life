import random
import numpy as np

from main import run_game_np, run_game_py, array_to_dict, dict_to_array
from patterns import bouncer, glider_gun

def test_dict_to_array():
    # Make random grid
    grid = {(i, j): 0
        for i in range(40) 
        for j in range(40)}
    for (i, j), _ in grid.items():
        if random.random() > 0.5: 
            grid[(i, j)] = 1
    assert array_to_dict(dict_to_array(grid)) == grid

def test_array_to_dict():
    # Make random grid
    grid = np.random.randint(2, size=(50, 50))
    assert (dict_to_array(array_to_dict(grid)) == grid).all()