
import calendar

from typing import Dict
from datetime import datetime
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
        query_result = self._budget_repo.get_all(budget_query)
        return query_result.total_budget



        
    

