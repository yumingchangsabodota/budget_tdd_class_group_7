# year, month, amount, 
# search start (date), end (date) -> sum (budget per day) 
# budget/days_of_month = budget per day

# illegal search range return 0
#

from typing import List
from typing import Dict

from budget import Budget


class BudgetRepo:
    def __init__(self, budget_list: List[Budget]):
        self._mock_data = budget_list

    def get_all(self) -> List[Budget]:
        return self.__dict_budget_data()
    
    def __dict_budget_data(self) -> Dict[str,Budget]:
        parsed_data = {}
        for budget in self._mock_data:
            parsed_data[budget.year_month] = budget

        return parsed_data



