# src/cli.py
import sys
import os

# --- CRITICAL PATH FIX ---
# This block forces the project root (../) onto the Python path
# to resolve the persistent "ModuleNotFoundError: No module named 'src'"
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
# -------------------------

import click
from .utils import greet

@click.command()
@click.option('--name', default='Contributor', help='The name of the user to greet.')
def niu_greet(name):
    """
    A simple command line interface for greeting users.
    """
    message = greet(name)
    print(message)

if __name__ == '__main__':
    niu_greet()