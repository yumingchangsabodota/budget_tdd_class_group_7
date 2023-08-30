# year, month, amount, 
# search start (date), end (date) -> sum (budget per day) 
# budget/days_of_month = budget per day

# illegal search range return 0
#

from typing import List, Dict, Union

from budget import Budget
from budget_query import BudgetQuery

class BudgetRepo:
    def __init__(self, budget_list: List[Budget]):
        self._mock_data = budget_list

    def get_all(self, budget_query: Union[None, BudgetQuery]= None) -> BudgetQuery:
        if budget_query == None:
            return budget_query
        
        source_budget = self.__dict_budget_data()

        for year_month in budget_query.map.keys():
            if year_month in source_budget:
                budget_query.map[year_month]['budget'] = source_budget[year_month]
        return budget_query
    
    def __dict_budget_data(self) -> Dict[str,Budget]:
        parsed_data = {}
        for budget in self._mock_data:
            parsed_data[budget.year_month] = budget

        return parsed_data



