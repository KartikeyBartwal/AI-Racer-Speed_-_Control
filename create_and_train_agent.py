import gym
import time
import numpy as np
import sys
from utils import run_for_n_seconds_random
from logging_module import setup_logger
from stable_baselines3 import PPO

# Load the logger
logger = setup_logger()
logger.info("Logger initialized successfully.")

# Initialize the CarRacing-v2 environment with render_mode specified
logger.info("Initializing CarRacing-v2 environment...")
env = gym.make('CarRacing-v2')
logger.info("Environment initialized successfully.")

# Initialize PPO with CNN policy
logger.info("Initializing PPO model with CnnPolicy...")
model = PPO('CnnPolicy', env, verbose=2, tensorboard_log="./ppo_logs", batch_size=64, n_steps=1000)

# Number of iterations
num_iterations = 100
timesteps_per_iteration = 10000

logger.info(f"Starting {num_iterations} training iterations...")

for i in range(1, num_iterations + 1):
    logger.info(f"🚀 Starting Iteration {i}/{num_iterations}...")

    model.learn(total_timesteps=timesteps_per_iteration)

logger.info("🏁 Training Complete. All iterations finished.")
model.save("ppo_CarRacing-v2_cnn_final")  # Save final trained model
