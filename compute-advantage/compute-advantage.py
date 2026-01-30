import numpy as np

def compute_advantage(states, rewards, V, gamma):
    """
    Returns: A (NumPy array of advantages)
    """
    states = np.asarray(states, dtype=np.int64)
    rewards = np.asarray(rewards, dtype=np.float64)
    V = np.asarray(V, dtype=np.float64)

    T = len(rewards)
    G = np.zeros(T, dtype=np.float64)

    running = 0.0
    for timestep in range(T-1, -1, -1):
        running = rewards[timestep] + gamma * running
        G[timestep] = running
    
    return G - V[states]
