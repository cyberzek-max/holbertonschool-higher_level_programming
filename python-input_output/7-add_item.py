#!/usr/bin/python3
"""
Adds all arguments to a Python list and saves them to a JSON file
"""

import sys
import importlib.util
from pathlib import Path

save_path = Path("add_item.json")

# Dynamically import save_to_json_file
spec = importlib.util.spec_from_file_location(
    "save_to_json_file", "./save_to_json_file.py"
)
save_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(save_mod)

# Dynamically import load_from_json_file
spec2 = importlib.util.spec_from_file_location(
    "load_from_json_file", "./load_from_json_file.py"
)
load_mod = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(load_mod)

save_to_json_file = save_mod.save_to_json_file
load_from_json_file = load_mod.load_from_json_file

# Load existing list if file exists, else start with empty list
if save_path.exists():
    items = load_from_json_file(str(save_path))
else:
    items = []

# Add all arguments passed to the script
items.extend(sys.argv[1:])

# Save updated list back to the file
save_to_json_file(items, str(save_path))
