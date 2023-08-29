# year, month, amount, 
# search start (date), end (date) -> sum (budget per day) 
# budget/days_of_month = budget per day

# illegal search range return 0
#
import calendar
from typing import List

class Budget:
    def __init__(self, year_month:str, amount: int):
        self.year_month = year_month
        self.amount = amount
    
    def __get_days_of_month(self) -> int:
        year = int(self.year_month[:4])
        print(year)
        month = int(self.year_month[4:])
        print(month)
        return calendar.monthrange(year, month)[1]

    @property
    def daily_budget(self):
        days = self.__get_days_of_month()
        return self.amount/days

class BudgetRepo:
    def __init__(self, budget_list: List[Budget]):
        self._mock_data = budget_list

    def get_all(self) -> List[Budget]:
        return self._mock_data



