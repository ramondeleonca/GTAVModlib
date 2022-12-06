import os
import pathlib

def readcl(file: os.PathLike):
    with open(file, "r") as f:
        return f.read()

def get_path(path: os.PathLike) -> os.PathLike:
    real_path = os.path.expandvars(path)
    if not pathlib.Path(real_path).is_absolute():
        real_path = pathlib.Path(__file__).parent.parent.joinpath(real_path)
    return real_path