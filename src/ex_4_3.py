""" ex_4_3.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def time_between_shutdowns(logfile):
    """
    Calculate the time between the first and last shutdown events recorded in the log file.
    Parameters: The path to the log file. 
    Returns: The time difference between the first and last shutdown events.
    """
    entries = get_shutdown_events(logfile)
    new_entries = [entry.split()[1] for entry in entries]
    timeobj = [logstamp_to_datetime(entry) for entry in new_entries]
    time_diff = timeobj[-1] - timeobj[0]
    return time_diff


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
