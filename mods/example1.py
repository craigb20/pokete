# This is an example mod that renames steini to steino

# Those two variables that provide the version and the
# name of the mod are needed
version = "3.1.3"
name = "One example"


# This function that takes p_data as argument is also needed,
# and can be used to modify p_data to add/change/remove Poketes,
# Attacks, Maps, NPCs etc.
def mod_p_data(p_data):
    p_data.pokes["steini"]["name"] = "stan"
