import unittest
import os
import pandas as pd
from data_handler import add_record, get_all_records, get_record, update_record, delete_record, get_statistics, DATA_FILE

class TestDataHandler(unittest.TestCase):

    def setUp(self):
        # Reset data file before each test
        df = pd.DataFrame(columns=['id', 'date', 'eggs', 'food_cost'])
        df.to_csv(DATA_FILE, index=False)

    def test_add_and_get_records(self):
        add_record('2023-10-01', 5, 2.5)
        records = get_all_records()
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]['eggs'], 5)
        self.assertEqual(records[0]['food_cost'], 2.5)

    def test_get_record(self):
        rec_id = add_record('2023-10-01', 5, 2.5)
        record = get_record(rec_id)
        self.assertIsNotNone(record)
        self.assertEqual(record['id'], rec_id)

    def test_update_record(self):
        rec_id = add_record('2023-10-01', 5, 2.5)
        update_record(rec_id, '2023-10-01', 10, 5.0)
        record = get_record(rec_id)
        self.assertEqual(record['eggs'], 10)
        self.assertEqual(record['food_cost'], 5.0)

    def test_delete_record(self):
        rec_id = add_record('2023-10-01', 5, 2.5)
        delete_record(rec_id)
        record = get_record(rec_id)
        self.assertIsNone(record)

    def test_statistics(self):
        # Day 1: 2 eggs, cost 1.0
        # Day 2: 4 eggs, cost 1.0
        # Same month
        add_record('2023-10-01', 2, 1.0)
        add_record('2023-10-02', 4, 1.0)

        stats = get_statistics()
        self.assertEqual(stats['total_eggs'], 6)
        self.assertEqual(stats['total_cost'], 2.0)
        self.assertEqual(stats['avg_eggs_day'], 3.0) # (2+4)/2
        self.assertEqual(stats['avg_eggs_month'], 6.0) # 6 eggs in 1 month
        self.assertEqual(stats['avg_cost_month'], 2.0) # 2.0 cost in 1 month

        # Add another month
        add_record('2023-11-01', 4, 2.0)
        stats = get_statistics()
        self.assertEqual(stats['total_eggs'], 10)
        self.assertEqual(stats['avg_eggs_month'], 5.0) # (6 + 4) / 2 months = 5.0

if __name__ == '__main__':
    unittest.main()
