import gym
import time
import numpy as np
import sys
from utils import run_for_n_seconds_random

np.bool = np.bool_

# List all available environments
envs = gym.envs.registry.values()
env_names = [env.id for env in envs]

# Initialize the CarRacing-v2 environment with render_mode specified
env = gym.make('CarRacing-v2', render_mode='human')

# Reset the environment to start
state, info = env.reset()
start_time = time.time()


run_for_n_seconds_random(env, 100)

env.close()
