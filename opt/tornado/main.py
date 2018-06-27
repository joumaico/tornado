import os
import pathlib
import subprocess
import sys
import time

from utils import get_cpu_temperature
from utils import read_tuples_from_file

PATH = pathlib.Path(__file__).parent


def main(config: str):
    """
    Control the fan speed based on the CPU temperature.

    Parameters
    ----------
    config (str)
        Path to the configuration file.

    Raises
    ----------
    AssertionError
        If the configuration data is invalid.
    """
    if os.path.exists(config):
        data = read_tuples_from_file(config)

    if not data:
        raise ValueError("The configuration file must not be empty.")

    for inputs in data:
        level, low, high = inputs
        assert level in (0, 1, 2, 3, 4, 5, 6, 7, 127)
        assert isinstance(low, int)
        assert isinstance(high, int)

    while True:
        temperature = get_cpu_temperature()
        if temperature:
            for inputs in data:
                level, low, high = inputs
                if low <= temperature <= high:
                    subprocess.run(
                        f"echo 'level {level}' | sudo tee /proc/acpi/ibm/fan",
                        shell=True,
                        check=True,
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.STDOUT,
                    )
        time.sleep(5)


if __name__ == "__main__":
    try:
        config = sys.argv[1]
    except Exception:  # fallback
        config = PATH / "config.ini"
    finally:
        main(config)
