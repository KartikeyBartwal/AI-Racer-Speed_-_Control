import time
import numpy as np
from logging_module import setup_logger

# Load the logger
logger = setup_logger()

def has_15_seconds_passed(start_time=None):
    """
    Checks if 15 seconds have passed since the given start time.

    Parameters:
    start_time (float): The start time in seconds.

    Returns:
    bool: True if 15 seconds have passed, False otherwise.
    """
    if time.time() - start_time >= 15:
        logger.info("15 seconds have passed since the function started.")
        return True
    else:
        return False

def run_for_n_seconds(env, action, duration=15, speed_of_simulation=0.05):
    """
    Runs the CarRacing-v2 environment for a specified duration with the given action.

    Parameters:
    env (gym.Env): The CarRacing-v2 environment.
    action (np.ndarray or callable): Action vector (fixed or function that generates actions).
    duration (int): Number of seconds to run the simulation.
    speed_of_simulation (float): Time delay between frames to control simulation speed.
    """
    start_time = time.time()
    logger.info(f"Starting controlled simulation for {duration} seconds.")

    while time.time() - start_time < duration:
        # Generate an action if a callable function is provided
        if callable(action):
            current_action = action()
        else:
            current_action = action

        logger.debug(f"Executing action: {current_action}")

        # Perform the action and get the new state and reward
        state, reward, done, truncated, info = env.step(current_action)

        logger.debug(f"State updated: Reward: {reward}, Done: {done}, Truncated: {truncated}, Info: {info}")

        # Render the environment
        env.render()

        # Sleep to slow down the simulation
        time.sleep(speed_of_simulation)

        if done or truncated:
            logger.warning("Simulation ended early due to environment termination (done/truncated).")
            break

    env.close()
    logger.info("Simulation run completed and environment closed.")

def run_for_n_seconds_random(env, duration=15, speed_of_simulation=0.05):
    """
    Runs the CarRacing-v2 environment for a specified duration with randomly generated actions.

    Parameters:
    env (gym.Env): The CarRacing-v2 environment.
    duration (int): Number of seconds to run the simulation.
    speed_of_simulation (float): Time delay between frames to control simulation speed.
    """
    start_time = time.time()
    logger.info(f"Starting random action simulation for {duration} seconds.")

    while time.time() - start_time < duration:
        # Generate a random action vector
        action = np.random.uniform(low=-1, high=1, size=(3,))
        action[2] = 0  # Ensuring no acceleration

        logger.debug(f"Random action generated: {action}")

        # Perform the action and get the new state and reward
        state, reward, done, truncated, info = env.step(action)

        logger.debug(f"Environment response: Reward: {reward}, Done: {done}, Truncated: {truncated}, Info: {info}")

        # Render the environment
        env.render()

        # Sleep to slow down the simulation
        time.sleep(speed_of_simulation)

        if done or truncated:
            logger.warning("Random action simulation terminated early due to environment termination.")
            break

    env.close()
    logger.info("Random action simulation completed and environment closed.")
