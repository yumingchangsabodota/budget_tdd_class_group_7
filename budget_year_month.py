
from datetime import datetime

class BudgetYearMonth:
    def __init__(self, datetime_instance: datetime):
        self._datetime_instance = datetime_instance

    @property
    def year(self) -> int:
        return self._datetime_instance.year
    
    @property
    def month(self) -> int:
        return self._datetime_instance.month

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.year == other.year and self.month == other.month
        return False

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self.year != other.year or self.month != other.month
        return False

    def __le__(self, other):
        if isinstance(other, self.__class__):
            return (self.year == other.year and self.month <= other.month) or (self.year < other.year)
        return False
    
    def __ge__(self, other):
        if isinstance(other, self.__class__):
            return (self.year == other.year and self.month >= other.month) or (self.year < other.year)
        return False

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return (self.year == other.year and self.month < other.month) or (self.year < other.year)
        return False
    
    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return (self.year == other.year and self.month > other.month) or (self.year > other.year)
        return False