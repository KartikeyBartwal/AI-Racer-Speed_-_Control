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

# Try to load the saved model
try:
    model = PPO.load("trained agents/ppo_CarRacing-v2_cnn_new", env=env)
    print("✅ Loaded existing model successfully.")
except Exception as e:
    print(f"⚠️ Failed to load saved model. Initializing new model. Error: {e}")
    model = PPO('CnnPolicy', env, verbose=2, tensorboard_log="./ppo_logs", batch_size=128, n_steps=2048)


# Number of iterations
num_iterations = 1
timesteps_per_iteration = 2048

logger.info(f"Starting {num_iterations} training iterations...")

for i in range(1, num_iterations + 1):
    logger.info(f"🚀 Starting Iteration {i}/{num_iterations}...")

    model.learn(total_timesteps=timesteps_per_iteration)

logger.info("🏁 Training Complete. All iterations finished.")

# Extract latest episode reward mean
ep_reward_mean = env.get_episode_rewards()[-1] if env.get_episode_rewards() else "unknown"

# Generate a unique filename using timestamp and reward
timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
model_filename = f"ppo_CarRacing-v2_{timestamp}_reward_{ep_reward_mean:.2f}.zip"

# Save the model uniquely
model.save("trained agents/" + model_filename)
print(f"💾 Model saved as '{model_filename}'.")
