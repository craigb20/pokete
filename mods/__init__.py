"""This imports all mods and validates them."""

import os
import importlib
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pokete_classes.mods import ModError
import variables as var


from importlib.metadata import entry_points

# if using poetry and a .toml file to set it up:
# [tool.poetry.plugins."pokete_mods"]
# example_mod = "mods.example_mod"
entry_points_dict = var.available_mods

def load_mod(ep):
    module_name, mod_path = ep.split(" = ")
    mod = importlib.import_module(mod_path)
    return mod,module_name

mod_obs = []
for ep in entry_points_dict["pokete_mods"]:
    try:
        # mod = ep.load() # loading data as metadata file
        mod,modu_name = load_mod(ep)
        [mod.version, mod.name, mod.mod_p_data]
        mod_obs.append(mod)
    except AttributeError as err:
        # When mod is not correctly stored
        raise ModError(modu_name, err)

mod_info = {i.name : i.version for i in mod_obs}
# print(mod_info)
