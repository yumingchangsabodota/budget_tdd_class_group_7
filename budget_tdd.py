
import calendar

from typing import Dict, Union
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from budget_repo import Budget, BudgetRepo



class BudgetService:
    def __init__(self, budget_repo: BudgetRepo) -> None:
        self._budget_repo = budget_repo
        self._all_budget: List[Budget] = self._budget_repo.get_all()

    def query(self, start:datetime, end:datetime) -> float:
        # health check with illegal name and no data
        if not self.__is_illegal(start, end):
            return 0
        # if not self.__is_nodata(start, end):
        #     return 0
        start_year = start.year
        start_month = start.month
        year_month_days = self.__get_days_in_month(start, end)
        print(year_month_days)
        total_budget = 0
        if self.__is_partial_month(start,end):
            total_budget = self.__get_partial_month_amount(start,end)
        else:
            for year_month, days in year_month_days.items():
                total_budget += self.__get_budget_amount(year_month).daily_budget * days

        return total_budget
    
    # //
    # 1. get_all 
    # 2. only return start - end month
    # 3. calculate single day budget per month
    # 4. 
    def __is_illegal(self, start:datetime, end:datetime) -> bool:
        return False if start > end else True
    
    """
    def __is_nodata(self, start:datetime, end:datetime) -> bool:
        if start not in self._all_budget
            return False
        elif end not in self._all_budget:
            return False
        return True
    """

        
    def __calculate_total(self, cross_month_days:dict) -> float:
        pass

    def __get_days_in_month(self, start:datetime, end:datetime) -> Dict[str,int]:
        days_in_month_dict = {}
        
        current = start
        while end >= current:
            days_specific_month = self.__get_days_of_month(current.year, current.month)
            current_year_month = f"{current.year}{current.month:0>2}"

            if current_year_month == f"{start.year}{start.month:0>2}":
                days = days_specific_month - start.day + 1
            if current_year_month == f"{end.year}{end.month:0>2}":
                days = end.day

            days_in_month_dict[f"{current.year}{current.month:0>2}"] = days
            #year_month = f"{year}{month:0>2}"
            current += relativedelta(months=1)
        return days_in_month_dict

    def __get_days_of_month(self, year:int , month: int) -> int:
        return calendar.monthrange(year, month)[1]

    def __get_budget_amount(self, year_month:str) -> Budget:
        for budget in self._all_budget:
            if budget.year_month == year_month:
                return budget
        return Budget('N/A',0)

    def __is_partial_month(self, start:datetime, end:datetime) -> bool:
        if f"{start.year}{start.month:0>2}" == f"{end.year}{end.month:0>2}":
            return True
        return False

    def __get_partial_month_amount(self, start:datetime, end:datetime) -> float:
        
        days = (end - start).days + 1
        budget_amount = self.__get_budget_amount(f"{start.year}{start.month:0>2}").daily_budget * days
        return budget_amount
        
    def __get_cross_month(self):
        pass

    

