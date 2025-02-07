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
env = gym.make('CarRacing-v2', render_mode='human')
logger.info("Environment initialized successfully.")

# Initialize PPO with CNN policy
logger.info("Initializing PPO model with CnnPolicy...")
model = PPO('CnnPolicy', env, verbose=2, tensorboard_log = "./ppo_logs", batch_size = 2, n_steps = 1000)

logger.info("Starting training loop...")
model.learn(total_timesteps=1000)  # Train PPO for 1000 steps

logger.info("✅ Training Complete. Saving model...")
model.save("ppo_CarRacing-v2_cnn")
logger.info("💾 Model saved as 'ppo_CarRacing-v2_cnn'.")
