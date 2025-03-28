"""Madlibs Stories."""

class Story:
    """Madlibs story."""

    def __init__(self, words, text):
        """Create story with words and template text."""
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""
        text = self.template
        for key, val in answers.items():
            text = text.replace("{" + key + "}", val)
        return text

# Define multiple stories
stories = {
    "adventure": Story(
        ["place", "noun", "verb", "adjective", "plural_noun"],
        "Once upon a time in {place}, a {adjective} {noun} loved to {verb} {plural_noun}."
    ),
    "fantasy": Story(
        ["creature", "weapon", "magic", "adjective"],
        "The {adjective} {creature} wielded a {weapon} and cast {magic} spells."
    ),
    "sci-fi": Story(
        ["planet", "alien_species", "verb", "gadget"],
        "On {planet}, the {alien_species} learned to {verb} using a {gadget}."
    ),
    "murder mystery": Story(
        ["murderer", "victim", "room", "weapon", "suspect"],
        "{murderer} killed the {victim} in the {location} with a {weapon}."
    ),
    "horror": Story(
        ["creature", "location", "adjective", "verb", "noun"],
        "Late at night, the {creature} lurked in the {location}, its {adjective} eyes glowing as it {verb} a {noun}."
    ),
    "romance": Story(
        ["person", "place", "emotion", "verb", "adjective"],
        "In {place}, {person} met someone who made them feel {emotion}, and they {verb} together under the {adjective} moon."
    ),
    "western": Story(
        ["cowboy", "horse", "place", "weapon", "adjective"],
        "The {adjective} {cowboy} rode their {horse} into {place}, ready for a showdown with their trusty {weapon}."
    ),
    "fairy tale": Story(
        ["princess", "place", "evil_creature", "action", "magical_item"],
        "The {princess} escaped from the {place}, chased by an {evil_creature}, but she used her {magical_item} to {action}."
    ),
    "sports": Story(
        ["team", "sport", "adjective", "action", "opponent"],
        "{team} played a {adjective} game of {sport}, {action} against their toughest opponent yet."
    ),
    "superhero": Story(
        ["superhero", "power", "villain", "city", "action"],
        "In the heart of {city}, {superhero} used their {power} to stop the {villain} from {action}."
    ),
}



