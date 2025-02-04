import time

def has_15_seconds_passed(start_time=None):
    if time.time() - start_time >= 15:  # Check if 15 seconds have passed
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

    while time.time() - start_time < duration:
        # Generate an action if a callable function is provided
        if callable(action):
            current_action = action()
        else:
            current_action = action

        print("Action vector:", current_action)

        # Perform the action and get the new state and reward
        state, reward, done, truncated, info = env.step(current_action)

        # Render the environment
        env.render()

        # Sleep to slow down the simulation
        time.sleep(speed_of_simulation)

        if done or truncated:
            break

    env.close()