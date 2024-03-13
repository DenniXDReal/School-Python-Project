import unittest
import pandas as pd
from unittest.mock import patch
from main_data import VisitorsAnalyticsUtils

class TestVisitorsAnalyticsUtils(unittest.TestCase):
    def setUp(self):
        self.utils = VisitorsAnalyticsUtils
        self.file_path = "data/Int_Monthly_Visitor.csv"

    def test_load_data_file(self):
        df = self.utils.loadDataFile()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 479)
        self.assertEqual(len(df.columns), 35)
        print("Number of Columns:", len(df.columns))
        print("Number of Rows:", len(df))

if __name__ == "__main__":
    unittest.main()