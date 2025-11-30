#!/usr/bin/python3
"""
Adds all arguments to a Python list and saves them to a JSON file.
"""

import sys
import json
from pathlib import Path

save_path = Path("add_item.json")

# Try to import helper functions, else define fallback
try:
    from save_to_json_file import save_to_json_file
except ImportError:
    def save_to_json_file(my_obj, filename):
        with open(filename, "w") as f:
            json.dump(my_obj, f)

try:
    from load_from_json_file import load_from_json_file
except ImportError:
    def load_from_json_file(filename):
        with open(filename, "r") as f:
            return json.load(f)

# Load existing list if file exists, else start with empty list
if save_path.exists():
    items = load_from_json_file(str(save_path))
else:
    items = []

# Add all arguments passed to the script
items.extend(sys.argv[1:])

# Save updated list back to the file
save_to_json_file(items, str(save_path))
