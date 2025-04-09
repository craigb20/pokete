# test_plugin.py
import importlib.metadata
from pokete_classes.mods import ModError
import variables as var



def test_plugins():
    mod_obs = []
    for ep in var.available_mods["pokete_mods"]: # gets dictionary of mods
        try:
            module_name, mod_path = ep.split(" = ")
            mod = importlib.import_module(mod_path)
            print(f"Loaded mod: {mod.name}, Version: {mod.version}")
            mod_obs.append(mod)
        except AttributeError as err:
            raise ModError(module_name, err)
    return mod_obs

if __name__ == "__main__":
    mods = test_plugins()
    print(mods)  # List of loaded mods
