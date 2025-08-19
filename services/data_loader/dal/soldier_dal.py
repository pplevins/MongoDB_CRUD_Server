class SoldierDAL:
    """Class to represent person's Data Layer, and implementing CRUD operations for people."""

    def __init__(self, conn_str=None):
        """Constructor"""
        pass

    def _connect(self):
        """Connect to database."""
        pass

    def get_all_soldiers(self):
        """Get all soldiers from the database."""
        pass

    def insert_soldier(self, soldier):
        """Insert soldier into database."""
        pass

    def remove_soldier(self, soldier_id):
        """Remove soldier from database."""
        pass

    def update_soldier(self, soldier_id, soldier):
        """Update existed soldier in the database."""
        pass