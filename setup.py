from pathlib import Path
import re
from typing import List, Tuple

from setuptools import setup, find_packages


NAME = "ml-engineering-foundations"
DESCRIPTION = "One-stop resource for ML engineering"

URL = "https://github.com/akashsonowal/ml-engineering-foundations"
AUTHOR =  "Akash Sonowal"
REQUIRES_PYTHON = ">=3.9.0"
HERE = PATH(__file__).parent

try:
  with open(HERE / "readme.md", encoding="utf-8") as f:
    long_description = "\n" + f.read()
except FileNotFoundError:
  long_description = DESCRIPTION
