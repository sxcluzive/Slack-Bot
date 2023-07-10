import unittest
from test.app import convert_to_sql, format_raw_sql

class AppTest(unittest.TestCase):

    def test_convert_to_sql(self):
        # Test a valid query
        query = "What is the SQL query to get the list of names of all users?"
        expected_sql = "SELECT Name FROM USERS;"
        self.assertEqual(convert_to_sql(query), expected_sql)

        # Test an invalid query
        query = "What is the SQL query to get the names of all students who are not enrolled in any classes?"
        expected_sql = "Either we don't have any matching result of your query of something went wrong from our end, please try again with new prompt"
        self.assertEqual(convert_to_sql(query), expected_sql)

        #Test a valid query
        query ="the name of all users"
        expected_sql = "SELECT name FROM users WHERE name IS NOT NULL;"
        self.assertEqual(convert_to_sql(query), expected_sql)

        #Test a indirect query
        query = "which are users who used phone in winter"
        expected_sql = "SELECT * FROM users WHERE onboarding_time BETWEEN '2022-12-21' AND '2023-03-20';"
        self.assertEqual(convert_to_sql(query), expected_sql)
if __name__ == "__main__":
    unittest.main()
