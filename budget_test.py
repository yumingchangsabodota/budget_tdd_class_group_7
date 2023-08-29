import unittest

from datetime import datetime
from budget_tdd import BudgetService
from budget_repo import Budget, BudgetRepo

class BudgetTestCase(unittest.TestCase):
    

    def test_get_partial_days_of_month(self):
        mock_budget = BudgetRepo([Budget('202307',310)])
        budget_svc = BudgetService(mock_budget)
        budget = budget_svc.query(start = datetime(2023,7,1), end = datetime(2023,7,2))
        self.assertEqual(budget,20)
    
    def test_get_all_days_of_month(self):
        mock_budget = BudgetRepo([Budget('202307',310),Budget('202308',3100)])
        budget_svc = BudgetService(mock_budget)
        budget = budget_svc.query(start = datetime(2023,7,1), end = datetime(2023,7,31))
        self.assertEqual(budget,310)

    def test_get_cross_month(self):
        pass

    def test_get_illegal_date(self):
        pass

    def test_get_no_data(self):
        pass

if __name__ == '__main__':
    unittest.main()



