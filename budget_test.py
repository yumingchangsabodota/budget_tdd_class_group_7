import unittest

from datetime import datetime
from budget_tdd import BudgetService
from budget_repo import Budget, BudgetRepo

class BudgetTestCase(unittest.TestCase):
    
    def setUp(self):
        budgets = [
            Budget('202307', 310),
            Budget('202308', 3100)
        ]
        self.mock_budget = BudgetRepo(budgets)
        self.budget_svc = BudgetService(self.mock_budget)

    def test_get_partial_days_of_month(self):
        budget = self.budget_svc.query(start = datetime(2023,7,1), end = datetime(2023,7,2))
        self.assertEqual(budget, 20.0)
    
    def test_get_all_days_of_month(self):
        budget = self.budget_svc.query(start = datetime(2023,7,1), end = datetime(2023,7,31))
        self.assertEqual(budget, 310.0)

    def test_get_cross_month(self):
        budget = self.budget_svc.query(start = datetime(2023,7,1), end = datetime(2023,8,7))
        self.assertEqual(budget, 380.0)

    def test_get_illegal_date(self):
        budget = self.budget_svc.query(start = datetime(2023,8,7), end = datetime(2023,7,8))
        self.assertEqual(budget, 0)

    def test_get_no_data(self):
        budget = self.budget_svc.query(start = datetime(2099,3,1), end = datetime(2099,3,2))
        self.assertEqual(budget, 0)

if __name__ == '__main__':
    unittest.main()





