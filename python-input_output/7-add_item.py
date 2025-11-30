#!/usr/bin/python3
"""
Adds all arguments to a Python list and saves them to a JSON file
"""

import sys
from pathlib import Path
save_path = Path("add_item.json")

# Relative imports for local modules
from .save_to_json_file import save_to_json_file
from .load_from_json_file import load_from_json_file

# Load existing list if file exists, else start with empty list
if save_path.exists():
    items = load_from_json_file(str(save_path))
else:
    items = []

# Add all arguments passed to the script
items.extend(sys.argv[1:])

# Save updated list back to the file
save_to_json_file(items, str(save_path))
