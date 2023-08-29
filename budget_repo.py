# year, month, amount, 
# search start (date), end (date) -> sum (budget per day) 
# budget/days_of_month = budget per day

# illegal search range return 0

from typing import List

class Budget:
    def __init__(self, year_month:str, amount: int):
        self.year_month = year_month
        self.amount = amount

class BudgetRepo:
    mock_data = [

    ]
    def get_all(self) -> List[Budget]:
        return self.mock_data

