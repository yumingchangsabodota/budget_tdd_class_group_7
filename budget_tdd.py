
import calendar

from datetime import datetime

class BudgetService:
    def __init__(self, start:datetime, end:datetime):
        self.start = start
        self.end = end
        self.budgets = {}


    def __get_get_days_of_month(self):
        pass