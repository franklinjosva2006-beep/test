import subprocess
import sys
import os

# Set working directory to zeravaneai for proper imports
os.chdir(os.path.join(os.path.dirname(__file__), "zeravaneai"))
sys.path.insert(0, os.getcwd())

# Run the actual app
exec(open("frontend/app.py").read())
