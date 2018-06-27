import pathlib
import re
import subprocess
import typing as t


def get_cpu_temperature() -> float:
    """
    Retrieves the CPU temperature by parsing the output of the `sensors` command.

    Returns
    -------
    float
        The temperature of the CPU in degrees Celsius.
    """
    feedback = subprocess.check_output(["sensors"]).decode().split("\n")
    for i in feedback:
        if "cpu" in i.lower():
            match = re.search(r"\+(\d+\.\d+)°C", i)
            if match:
                return float(match.group(1))
    return 0.0


def read_tuples_from_file(fp: t.Union[str, pathlib.PosixPath]) -> t.List[t.Tuple[int, int, int]]:
    """
    Reads a file containing tuples of integers and returns them as a list of tuples.

    Parameters
    ----------
    fp (str)
        The file path to read from.

    Returns
    ----------
    List[Tuple[int, int, int]]
        A list of tuples, each containing three integers.

    Example
    ----------
    >>> read_tuples_from_file("path/to/config")
    [(5, 0, 40), (7, 39, 60), (127, 59, 512)]
    """
    with open(fp, "r") as f:
        s = f.read()

    pattern = r"\((\d+),\s*(\d+),\s*(\d+)\)"
    matches = re.findall(pattern, s)
    tuples = [(int(x), int(y), int(z)) for x, y, z in matches]

    return tuples
