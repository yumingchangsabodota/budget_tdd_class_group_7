import calendar

class Budget:
    def __init__(self, year_month:str, amount: int):
        self.year_month = year_month
        self.amount = amount
    
    def __get_days_of_month(self) -> int:
        if self.year_month == 'N/A':
            return 0
        year = int(self.year_month[:4])
        month = int(self.year_month[4:])
        return calendar.monthrange(year, month)[1]

    @property
    def daily_budget(self) -> float:
        if self.amount == 0:
            return 0
        days = self.__get_days_of_month()
        return self.amount/days