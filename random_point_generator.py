# %%
import numpy as np
import matplotlib.pyplot as plt

# %% 
input_path = "path"
data_file_int = "interior.asc"
data_file_bc = "boundary.asc" 
point_cloud_int = np.loadtxt(input_path+data_file_int, skiprows=1)
point_cloud_bc = np.loadtxt(input_path+data_file_bc, skiprows=1)
N_int = 500
N_bc = 200
seed = 42

# %%
def random_point_cloud(pc_dom, seed, N):    
     
    size = N

    """using Generator.choice"""
    rng = np.random.default_rng(seed)
    pc_dom_rand = rng.choice(pc_dom, size=size, replace=False)

    """using random.choice"""
    #seed = np.random.seed(42)
    #random_indices = np.random.choice(pc_dom.shape[0], size=size, replace = False)
    #pc_dom_rand = pc_dom[random_indices, :]

    """using random.randint (**can cause replacement problems**)"""
    #seed = np.random.seed(42)
    #pc_dom_rand = pc_dom[np.random.randint(pc_dom.shape[0], size=size, :] 
    
    return pc_dom_rand

# %%
def random_boundary_point_generator(boundary_point_array: np.ndarray, seed: int, number_of_samples: int):
    return random_point_cloud(boundary_point_array, seed, number_of_samples)

# %%
def random_interior_point_generator(interior_point_array: np.ndarray, seed: int, number_of_samples: int):
    return random_point_cloud(interior_point_array, seed, number_of_samples)