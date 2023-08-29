
import calendar

from datetime import datetime
from budget_repo import Budget, BudgetRepo



class BudgetService:
    def __init__(self, budget_repo: BudgetRepo) -> None:
        self._budget_repo = budget_repo
        self._all_budget = self._budget_repo.get_all()

    def query(self, start:datetime, end:datetime) -> float:
        start_year = start.year
        start_month = start.month
        days = (end - start).days + 1
        budget = self.__get_budget_amount(start_year, start_month)

        
        return days * budget.daily_budget
    
    # //
    # 1. get_all 
    # 2. only return start - end month
    # 3. calculate single day budget per month
    # 4. 

    def __calculate_total(self):
        pass


    def __get_budget_amount(self, year:int, month:int) -> Budget:
        year_month = f"{year}{month:0>2}" #pad month to have two character
        for budget in self._all_budget:
            if budget.year_month == year_month:
                return budget
        return 0
    

    def __get_partial_month(self):
        pass
    def __get_cross_month(self):
        pass

    

