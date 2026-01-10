import unittest
import os
import pandas as pd
from data_handler import add_record, get_all_records, get_record, update_record, delete_record, get_statistics, DATA_FILE

class TestDataHandler(unittest.TestCase):

    def setUp(self):
        # Reset data file before each test
        df = pd.DataFrame(columns=['id', 'date', 'type', 'amount', 'cost', 'note'])
        df.to_csv(DATA_FILE, index=False)

    def test_add_and_get_records(self):
        # Add Egg
        add_record('2023-10-01', 'egg', amount=5)
        # Add Food
        add_record('2023-10-02', 'food', cost=25.0, note="25kg")

        records = get_all_records()
        self.assertEqual(len(records), 2)

        egg_record = next(r for r in records if r['type'] == 'egg')
        self.assertEqual(egg_record['amount'], 5)
        self.assertEqual(egg_record['cost'], 0)
        self.assertEqual(egg_record['date'], '01/10/2023')

        food_record = next(r for r in records if r['type'] == 'food')
        self.assertEqual(food_record['cost'], 25.0)
        self.assertEqual(food_record['note'], "25kg")

    def test_statistics_logic(self):
        # 1. Buy 10 chickens for 100€
        add_record('2023-01-01', 'chicken', amount=10, cost=100.0)
        stats = get_statistics()
        self.assertEqual(stats['current_chickens'], 10)

        # 2. Buy Food 50€
        add_record('2023-01-02', 'food', cost=50.0)

        # 3. Lay 50 eggs
        add_record('2023-01-03', 'egg', amount=50)

        stats = get_statistics()
        # Cost per egg = (100 + 50) / 50 = 3.0€
        self.assertEqual(stats['cost_per_egg'], 3.0)
        self.assertEqual(stats['total_food_cost'], 50.0)
        self.assertEqual(stats['total_chicken_cost'], 100.0)

        # 4. Lose 1 chicken (no cost)
        add_record('2023-02-01', 'chicken', amount=-1, cost=0)
        stats = get_statistics()
        self.assertEqual(stats['current_chickens'], 9)

    def test_statistics_time_range_logic(self):
        from unittest.mock import patch

        # Scenario: Food bought in Nov 2023. Current date Jan 2024.
        add_record('2023-11-15', 'food', amount=10, cost=90.00)

        with patch('pandas.Period.now') as mock_now:
            def side_effect(freq):
                if freq == 'M':
                    return pd.Period('2024-01', freq='M')
                if freq == 'Y':
                    return pd.Period('2024', freq='Y')
                return pd.Period.now(freq)

            mock_now.side_effect = side_effect

            stats = get_statistics()
            # Nov 2023, Dec 2023, Jan 2024 = 3 months. 90/3 = 30.
            self.assertEqual(stats['avg_food_cost_month'], 30.0)

            # Years: 2023, 2024 = 2 years. 90/2 = 45.
            self.assertEqual(stats['avg_food_cost_year'], 45.0)

if __name__ == '__main__':
    unittest.main()
