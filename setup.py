# To build an executable on windows, run "python setup.py build" 
import sys 
import os
from cx_Freeze import setup, Executable

# Add files
files = ["icon.ico"]

# Target
target = Executable(
    script = "main.py",
    base = "Win32GUI",
    icon = "icon.ico",
)

# Setup
setup(
    name = "AppAI",
    version = "1.0",
    description = "lorem ipsum",
    author = "Tahar Chettaoui",
    options = {"build_exe": {"include_files":files}},
    executables = [target],
)