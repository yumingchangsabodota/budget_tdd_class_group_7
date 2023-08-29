import unittest

from datetime import datetime
from budget_service import BudgetService
from budget_repo import Budget, BudgetRepo

class BudgetTestCase(unittest.TestCase):
    
    def setUp(self):
        budgets = [
            Budget('202307', 310),
            Budget('202308', 3100),
            Budget('202309', 30),
        ]
        self.mock_budget = BudgetRepo(budgets)
        self.budget_svc = BudgetService(self.mock_budget)

    def test_get_one_day_of_budget(self):
        budget = self.budget_svc.query(start = datetime(2023,8,1), end = datetime(2023,8,1))
        self.assertEqual(budget, 100.0)

    def test_get_days_of_budget_within_one_month(self):
        budget = self.budget_svc.query(start = datetime(2023,7,1), end = datetime(2023,7,3))
        self.assertEqual(budget, 30.0)
    
    def test_get_budget_of_entire_month(self):
        budget = self.budget_svc.query(start = datetime(2023,7,1), end = datetime(2023,7,31))
        self.assertEqual(budget, 310.0)
        budget = self.budget_svc.query(start = datetime(2023,8,1), end = datetime(2023,8,31))
        self.assertEqual(budget, 3100.0)
        budget = self.budget_svc.query(start = datetime(2023,9,1), end = datetime(2023,9,30))
        self.assertEqual(budget, 30.0)

    def test_get_budget_across_month(self):
        budget = self.budget_svc.query(start = datetime(2023,7,1), end = datetime(2023,8,7))
        self.assertEqual(budget, 1010.0)
        budget = self.budget_svc.query(start = datetime(2023,7,30), end = datetime(2023,9,2))
        self.assertEqual(budget, 3122.0)

    def test_get_illegal_date(self):
        budget = self.budget_svc.query(start = datetime(2023,8,7), end = datetime(2023,7,8))
        self.assertEqual(budget, 0)

    def test_get_no_data(self):
        budget = self.budget_svc.query(start = datetime(2099,3,1), end = datetime(2099,3,2))
        self.assertEqual(budget, 0)

if __name__ == '__main__':
    unittest.main()





