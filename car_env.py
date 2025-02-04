import gym
import time
import numpy as np
from utils import has_15_seconds_passed
import sys

# List all available environments
envs = gym.envs.registry.values()
env_names = [env.id for env in envs]
print(env_names)

# Initialize the CarRacing-v2 environment with render_mode specified
env = gym.make('CarRacing-v2', render_mode='human')

# Reset the environment to start
state, info = env.reset()
start_time = time.time()

env.render()

time.sleep(800)

env.close()