import subprocess
import sys

from setuptools import find_packages, setup

setup(
    name="fdm",
    version="0.2.0",
    author="Anonymous",
    packages=find_packages(),
    description="Fair distribution matching",
    python_requires=">=3.6",
    package_data={"clustering": ["py.typed"], "fdm": ["py.typed"], "shared": ["py.typed"]},
    install_requires=[
        'dataclasses;python_version<"3.7"',
        "GitPython >= 2.1.11",
        "gitpython",
        "hydra-core",
        "hydra-ray-launcher",
        "lapjv",
        "matplotlib >= 3.0.2, < 3.3.1",
        "numpy >= 1.15",
        "pandas >= 1.0",
        "pillow",
        "pipenv >= 2018.11.26",
        "scikit-image >= 0.14",
        "scikit_learn >= 0.20.1",
        "scipy >= 1.2.1",
        "seaborn >= 0.9.0",
        "teext",
        "torch >= 1.2",
        "torchvision >= 0.4.0",
        "tqdm >= 4.31.1",
        "typed-argument-parser == 1.4",
        "typer",
        "typing-extensions >= 3.7.2",
        "wandb >= 0.10.2",

    ],
)

try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "faiss-gpu"])
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "faiss-cpu"])
