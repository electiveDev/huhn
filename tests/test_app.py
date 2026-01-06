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
        df = pd.DataFrame(columns=['id', 'date', 'type', 'amount', 'cost', 'note'])
        df.to_csv(DATA_FILE, index=False)

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_egg(self):
        response = self.client.post('/add', data={
            'type': 'egg',
            'date': '2023-12-01',
            'amount': '10'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        df = pd.read_csv(DATA_FILE)
        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]['type'], 'egg')
        self.assertEqual(df.iloc[0]['amount'], 10)

    def test_add_food(self):
        response = self.client.post('/add', data={
            'type': 'food',
            'date': '2023-12-01',
            'cost': '25.50',
            'note': '25kg sack'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        df = pd.read_csv(DATA_FILE)
        self.assertEqual(df.iloc[0]['type'], 'food')
        self.assertEqual(df.iloc[0]['cost'], 25.50)
        self.assertEqual(df.iloc[0]['note'], '25kg sack')

if __name__ == '__main__':
    unittest.main()
