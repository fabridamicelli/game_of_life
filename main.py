import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from patterns import bouncer, glider_gun

def run_and_animate(grid=None, n_steps=1000):
    '''
    Run game of life, create animation and save as mp4 file.
    Animation is save in the working directory.    

    Parameters
    ----------
    grid: 2-D ndarray
        Initial grid on which the game runs.
    n_steps: int
        Number of iterations of the game.
    '''
    # Initialize figure for animation
    fig = plt.figure()
    plt.axis('off')
    ims = [[plt.imshow(grid, cmap='binary', interpolation='none', 
                       animated=True)]]

    # Run game of life
    n_rows, n_cols = grid.shape
    for _ in range(n_steps): 
        new_grid = np.zeros_like(grid)
        # Update cells
        for i in range(1, n_rows - 1):
            for j in range(1, n_cols - 1):
                cell_state = grid[i, j]
                neighbors = grid[i - 1: i + 2, j - 1: j + 2]
                n_alive_neighbors = np.sum(neighbors) - cell_state
                # State transition
                if cell_state and n_alive_neighbors in (2, 3):
                    new_grid[i, j] = 1
                if not cell_state and n_alive_neighbors == 3:
                    new_grid[i, j] = 1
        
        grid = new_grid
        # Save current state for animation    
        ims.append([plt.imshow(grid, cmap='binary', interpolation='none',
                               animated=True)])
        
    ani = animation.ArtistAnimation(fig, ims, interval=100, 
                                    blit=True, repeat_delay=100)
    ani.save('gameoflife.mp4')

if __name__ == '__main__':
    # grid = np.random.randint(2, size=(50, 50))
    run_and_animate(grid=bouncer, n_steps=150)
