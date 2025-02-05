import gym
import time
import numpy as np
import sys
from utils import run_for_n_seconds_random
from logging_module import setup_logger

# Load the logger
logger = setup_logger()

# Initialize the CarRacing-v2 environment with render_mode specified
env = gym.make('CarRacing-v2', render_mode='human')
logger.info("Running the 'CarRacing-v2' environment")

# Reset the environment to start
state, info = env.reset()
start_time = time.time()

# Test run the simulation
run_for_n_seconds_random(env, 100)

env.close()
