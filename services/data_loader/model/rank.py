from enum import Enum


class Rank(str, Enum):
    SOLDIER = 'soldier'
    COMMANDER = 'commander'
    OFFICER = 'officer'
