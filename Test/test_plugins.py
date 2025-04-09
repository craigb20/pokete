import importlib.metadata
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pokete_classes.mods import ModError
import variables as var

def try_plugin(dict):
    mod_obs = []
    for ep in dict["pokete_mods"]: # gets dictionary of mods
        try:
            module_name, mod_path = ep.split(" = ")
            mod = importlib.import_module(mod_path)
            print(f"Loaded mod: {mod.name}, Version: {mod.version}")
            mod_obs.append(mod)
        except AttributeError as err:
            raise ModError(module_name, err)
    return mod_obs
        
def test_known_plugins():
    my_mods = {
    "pokete_mods": [
        "example_mod = mods.example","other_example = mods.example1"]}
    mod_obs = try_plugin(my_mods)
    assert len(mod_obs) == 2
    assert mod_obs[0].name == 'Example'
    assert mod_obs[0].version == "0.1.0"
    assert mod_obs[1].version == "3.1.3"
    
def test_other_plugins():
    my_mods = {
    "pokete_mods": []}
    mod_obs = try_plugin(my_mods)
    assert mod_obs == []
    assert len(mod_obs) == 0
