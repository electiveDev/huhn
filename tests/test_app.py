import unittest
from app import app
from data_handler import DATA_FILE
import pandas as pd
import os

class TestApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        # Reset data file before each test
        df = pd.DataFrame(columns=['id', 'date', 'eggs', 'food_cost'])
        df.to_csv(DATA_FILE, index=False)

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_record(self):
        response = self.client.post('/add', data={
            'date': '2023-12-01',
            'eggs': '10',
            'food_cost': '5.5'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        # Verify it was added
        df = pd.read_csv(DATA_FILE)
        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]['eggs'], 10)

    def test_records_page(self):
        response = self.client.get('/records')
        self.assertEqual(response.status_code, 200)

    def test_edit_and_update(self):
        # Add a record first
        self.client.post('/add', data={
            'date': '2023-12-01',
            'eggs': '10',
            'food_cost': '5.5'
        })
        df = pd.read_csv(DATA_FILE)
        rec_id = df.iloc[0]['id']

        # Test Edit Page
        response = self.client.get(f'/edit/{rec_id}')
        self.assertEqual(response.status_code, 200)

        # Test Update
        response = self.client.post(f'/update/{rec_id}', data={
            'date': '2023-12-01',
            'eggs': '12',
            'food_cost': '6.0'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        df = pd.read_csv(DATA_FILE)
        self.assertEqual(df.iloc[0]['eggs'], 12)

    def test_delete(self):
        # Add a record first
        self.client.post('/add', data={
            'date': '2023-12-01',
            'eggs': '10',
            'food_cost': '5.5'
        })
        df = pd.read_csv(DATA_FILE)
        rec_id = df.iloc[0]['id']

        response = self.client.post(f'/delete/{rec_id}', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        df = pd.read_csv(DATA_FILE)
        self.assertEqual(len(df), 0)

if __name__ == '__main__':
    unittest.main()
