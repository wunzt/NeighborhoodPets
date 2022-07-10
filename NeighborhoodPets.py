# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 7/10/2022
# Description:

import json


class DuplicateNameError(Exception):
    """Creates an exception to be raised later."""
    pass


class NeighborhoodPets:
    """Creates a dictionary of neighborhood pets, allowing pets to be added with a pet_name as the key, and its
    species and owner as values."""

    def __init__(self):
        """Initializes the dictionary of neighborhood pets."""
        self._pet_dict = {}

    def add_pet(self, pet_name, species, owner):
        """Allows pets to be added with a pet_name as the key, and its species and owner as values."""

        if pet_name in self._pet_dict:
            raise DuplicateNameError
        else:
            self._pet_dict[pet_name] = [species, owner]

    def delete_pet(self, pet_name):
        """Deletes a pet from the dictionary by taking its name."""
        self._pet_dict.pop(pet_name)

    def get_owner(self, pet_name):
        """Returns the name of the pet's owner."""
        if pet_name in self._pet_dict:
            return self._pet_dict[pet_name][1]

    def save_as_json(self, file_name):
        """Saves the pet dictionary to a .json file of the name passed."""
        with open(file_name, "w") as outfile:
            json.dump(self._pet_dict, outfile)

    def read_json(self, file_name):
        """Reads a .json file with the passed name, replacing the current pet dictionary with the .json file's own."""
        with open(file_name, "r") as infile:
            self._pet_dict = json.load(infile)

    def get_all_species(self):
        """Returns a list of the species of all pets in the dictionary."""
        species_list = []

        for key in self._pet_dict:
            species_list.append(self._pet_dict[key])

        return species_list