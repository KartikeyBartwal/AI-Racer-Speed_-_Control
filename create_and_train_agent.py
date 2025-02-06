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
model = PPO('CnnPolicy', env, verbose=2)
logger.info("PPO model initialized.")

logger.info("Starting training loop...")
for episode in range(1000):  # Run training in steps
    logger.info(f"Starting episode {episode + 1}...")
    model.learn(total_timesteps=1000)  # Uncomment if training is needed
#
#     # Reset environment at the start of each episode
#     obs = env.reset()
#     done = False
#     step_count = 0
#     total_reward = 0
#
#     while not done:
#         step_count += 1
#         action, _states = model.predict(obs)
#         obs, reward, done, info = env.step(action)
#         total_reward += reward
#
#         logger.info(f"Step {step_count}: Action taken: {action}, Reward: {reward}, Done: {done}")
#         env.render()  # Render the environment to visualize the agent's actions
#
#     logger.info(f"Episode {episode + 1} finished. Total steps: {step_count}, Total reward: {total_reward}")
#
# env.close()
# logger.info("Environment closed. Saving the model...")
#
# model.save("ppo_CarRacing-v2_cnn")
# logger.info("Model saved as 'ppo_CarRacing-v2_cnn'. Training complete.")
