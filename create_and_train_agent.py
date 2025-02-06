import gym
import time
import numpy as np
import sys
from utils import run_for_n_seconds_random
from logging_module import setup_logger
from stable_baselines3 import PPO

# Load the logger
logger = setup_logger()

# Initialize the CarRacing-v2 environment with render_mode specified
env = gym.make('CarRacing-v2', render_mode='human')

# Initialize PPO with CNN policy
model = PPO('CnnPolicy', env, verbose=2)

model.learn(total_timesteps=1000000)

for _ in range(1000):  # Run training in steps
    model.learn(total_timesteps=1000)

    # Render the environment during training (watching the agent)
    obs = env.reset()
    done = False
    while not done:
        action, _states = model.predict(obs)
        obs, reward, done, info = env.step(action)
        env.render()  # Render the environment to visualize the agent's actions

env.close()

model.save("ppo_CarRacing-v2_cnn")

