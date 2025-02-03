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

# Run a loop to control the car's movement
while not has_15_seconds_passed():
    # Take random actions to move the car (you can fine-tune this later)
    action = np.random.uniform(low=-1, high=1, size=(4,))  # Random action vector in the action space

    print("action vector:", action)


    # Perform the action and get the new state and reward
    state, reward, done, truncated, info = env.step(action)

    # Render the environment to display it
    env.render()

    # Sleep for a bit to slow down the rendering process
    time.sleep(0.05)  # Adjust this value to control the speed of the simulation

# Close the environment once done
env.close()