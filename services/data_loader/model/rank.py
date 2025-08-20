from enum import Enum


class Rank(str, Enum):
    """Class to represent the rank of the soldier (Enum)"""
    SOLDIER = 'soldier'
    COMMANDER = 'commander'
    OFFICER = 'officer'
