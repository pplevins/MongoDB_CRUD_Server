from rank import Rank


class Soldier:
    def __init__(self, soldier_id, first_name, last_name, phone_number, rank:Rank):
        """
        :param soldier_id:
        :param first_name:
        :param last_name:
        :param phone_number:
        :param rank:
        """
        self._soldier_id = soldier_id
        self._first_name = first_name
        self._last_name = last_name
        self._phone_number = phone_number
        self._rank = rank

    def __str__(self):
        """String representation"""
        return (f"Soldier No. {self._soldier_id}\n"
                f"First Name: {self._first_name}\n"
                f"Last Name: {self._last_name}\n"
                f'Phone number: {self._phone_number}\n'
                f'Rank: {self._rank}')
