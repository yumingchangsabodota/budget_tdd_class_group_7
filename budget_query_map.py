
from typing import Dict, Any

from budget_year_month import BudgetYearMonth
from budget import Budget

class BudgetQueryYearMonthDaysMap:
    def __init__(self):
        self.map = {}
    
    def get_total_budget(self):
        total_budget = 0
        for year_month in self.map.keys():
            budget = self.map[year_month]['budget']
            daily = budget.daily_budget
            days = self.map[year_month]['days']
            total_budget += days * daily
        return total_budget
            
    def add_days(self, year_month: BudgetYearMonth, days: int):
        self.__init_dict_item(year_month)
        self.map[year_month.year_month]['days'] = days

    def add_budget(self, year_month: BudgetYearMonth, budget: Budget):
        self.__init_dict_item(year_month)
        self.map[year_month.year_month]['budget'] = budget

    def get_days(self, year_month: BudgetYearMonth) -> int:
        if year_month.year_month not in self.map:
            return 0
        return self.map[year_month.year_month]
    
    def __init_dict_item(self, year_month: BudgetYearMonth):
        if year_month.year_month not in self.map:
            self.map[year_month.year_month] = {}
            if 'days' not in self.map[year_month.year_month]:
                self.map[year_month.year_month]['days'] = 0
            if 'budget' not in self.map[year_month.year_month]:
                self.map[year_month.year_month]['budget'] = Budget()