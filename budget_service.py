
import calendar

from typing import Dict
from datetime import datetime
from dateutil.relativedelta import relativedelta
from budget_repo import Budget, BudgetRepo
from budget_query import BudgetQuery



class BudgetService:
    def __init__(self, budget_repo: BudgetRepo) -> None:
        self._budget_repo = budget_repo
        self._all_budget: Dict[str,Budget] = self._budget_repo.get_all()

    def query(self, start:datetime, end:datetime) -> float:
        budget_query = BudgetQuery(start, end)
        if budget_query.is_illegal:
            return 0

        total_budget = 0
        for year_month, days in budget_query.query_to_yearmonth_days_dict.items():
            if year_month in self._all_budget:
                total_budget += self._all_budget[year_month].daily_budget * days
        return total_budget


        
    

