import gym
import time
from stable_baselines3 import PPO
from logging_module import setup_logger  # Assuming you have a logging setup

# Initialize logger
logger = setup_logger()
logger.info("Logger initialized successfully.")

# Initialize the environment in render mode
logger.info("Initializing CarRacing-v2 environment in render mode...")
env = gym.make('CarRacing-v2', render_mode='human')
logger.info("Environment initialized successfully.")

# Load the trained model
model_path = "trained agents/The_Chaotic_Teenager_2025-02-09_15-51-33_reward_793.29.zip"  # Replace with actual filename
logger.info(f"Loading trained model from {model_path}...")
try:
    model = PPO.load(model_path, env=env)
    logger.info("✅ Model loaded successfully.")
except Exception as e:
    logger.error(f"⚠️ Failed to load the model. Error: {e}")
    exit(1)

# Reset the environment
obs = env.reset()[0]
logger.info("Starting simulation...")

while True:
    action, _states = model.predict(obs)  # Get the action from the trained model
    obs, reward, done, truncated, info = env.step(action)  # Take a step in the environment
    env.render()  # Render the environment
    logger.info(f"Reward: {reward}")
    logger.debug(f"Action taken: {action}, Reward: {reward}, Done: {done}, Truncated: {truncated}")

    if done or truncated:
        logger.info("Episode ended. Resetting environment...")
        obs = env.reset()[0]
