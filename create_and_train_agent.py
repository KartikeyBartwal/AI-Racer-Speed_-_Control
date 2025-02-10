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
    model = PPO.load("trained agents/ppo_CarRacing-v2_2025-02-09_15-04-02_reward_-50.90", env = env, verbose=2, tensorboard_log="./ppo_logs", batch_size=128, n_steps=2048)
    print("✅ Loaded existing model successfully.")
except Exception as e:
    print(f"⚠️ Failed to load saved model. Initializing new model. Error: {e}")
    model = PPO('CnnPolicy', env, verbose=2, tensorboard_log="./ppo_logs", batch_size=128, n_steps=2048)


# Number of iterations
num_iterations = 1000
timesteps_per_iteration = 2048

logger.info(f"Starting {num_iterations} training iterations...")

for i in range(1, num_iterations + 1):
    # Train the model and store the result
    training_results = model.learn(total_timesteps=timesteps_per_iteration)

    logger.debug("Training results: \n")
    logger.debug(training_results)

    # Extract mean episode reward from logs
    ep_rewards = [ep_info["r"] for ep_info in training_results.ep_info_buffer]  # Extract rewards
    ep_reward_mean = np.mean(ep_rewards) if ep_rewards else "unknown"  # Compute mean if available

    logger.debug(f"ep_reward_mean: {ep_reward_mean}")

    # Save the model only if ep_reward_mean exceeds 800
    if isinstance(ep_reward_mean, (int, float)) and ep_reward_mean > 800:
        # Generate a unique filename using timestamp and reward
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        model_filename = f"ppo_CarRacing-v2_{timestamp}_reward_{ep_reward_mean:.2f}.zip"

        # Save the model
        model.save("trained agents/" + model_filename)
        print(f"💾 Model saved as '{model_filename}'.")

logger.info("🏁 Training Complete. All iterations finished.")

