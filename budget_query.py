import calendar

from typing import Dict, Union
from datetime import datetime

from budget_year_month import BudgetYearMonth
from budget_query_map import BudgetQueryYearMonthDaysMap


class BudgetQuery:
    def __init__(self, start:datetime, end:datetime):
        self._start = start
        self._end = end
        self._query_map = self.__create_query_map()

    @property
    def is_illegal(self) -> bool:
        if self._start > self._end: 
            return True
        return False 
    
    @property
    def map(self):
        return self._query_map.map
    
    @property
    def total_budget(self):
        return self._query_map.get_total_budget()
    
    def __create_query_map(self) -> BudgetQueryYearMonthDaysMap:
        if self.is_illegal:
            return BudgetQueryYearMonthDaysMap
        
        map = BudgetQueryYearMonthDaysMap()
        current = BudgetYearMonth(self._start)
        start = BudgetYearMonth(self._start)
        end = BudgetYearMonth(self._end)

        while end >= current:
            if self.__is_within_one_month():
                days = self.__get_within_one_month_days()
                map.add_days(current ,days)
                break
            else:
                days = self.__get_days_of_month(current.year, current.month)
                if current == start:
                    days = days - start.day +1
                if current == end:
                    days = end.day
                map.add_days(current, days)
            current.increase_one_month()
        return map
    
    def __get_within_one_month_days(self) -> int:
        return (self._end - self._start).days + 1

    def __is_within_one_month(self) -> bool:
        if f"{self._start.year}{self._start.month:0>2}" == f"{self._end.year}{self._end.month:0>2}":
            return True
        return False

    def __get_days_of_month(self, year:int , month: int) -> int:
        return calendar.monthrange(year, month)[1]
    