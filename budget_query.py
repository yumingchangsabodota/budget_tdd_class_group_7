import calendar

from typing import Dict
from datetime import datetime
from dateutil.relativedelta import relativedelta

from budget_year_month import BudgetYearMonth

class BudgetQuery:
    def __init__(self, start:datetime, end:datetime):
        self._start = start
        self._end = end

    @property
    def is_illegal(self) -> bool:
        if self._start > self._end: 
            return True
        return False 
    
    @property
    def query_to_yearmonth_days_dict(self) -> Dict[str, int]:
        if self.is_illegal:
            return {}
        
        year_month_days_dict = {}
        current = self._start
        start_year_month = f"{self._start.year}{self._start.month:0>2}"
        end_year_month = f"{self._end.year}{self._end.month:0>2}"

        while BudgetYearMonth(self._end) >= BudgetYearMonth(current):
            current_year_month = f"{current.year}{current.month:0>2}"
            if self.__is_within_one_month():
                days = self.__get_within_one_month_days()
                year_month_days_dict[current_year_month] = days
                break
            else:
                days = self.__get_days_of_month(current.year, current.month)
                if current_year_month == start_year_month:
                    days = days - self._start.day +1
                if current_year_month == end_year_month:
                    days = self._end.day
                year_month_days_dict[current_year_month] = days
            current += relativedelta(months=1)
        return year_month_days_dict
    
    def __get_within_one_month_days(self) -> int:
        return (self._end - self._start).days + 1

    def __is_within_one_month(self) -> bool:
        if f"{self._start.year}{self._start.month:0>2}" == f"{self._end.year}{self._end.month:0>2}":
            return True
        return False

    def __get_days_of_month(self, year:int , month: int) -> int:
        return calendar.monthrange(year, month)[1]
    