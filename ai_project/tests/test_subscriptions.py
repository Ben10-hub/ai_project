import unittest
from scripts.subscriptions import create_membership_database, add_membership, check_membership

class TestMembership(unittest.TestCase):
    def setUp(self):
        self.db_path = ':memory:'
        create_membership_database(self.db_path)

    def test_add_and_check_membership(self):
        license_plate = 'ABC123'
        add_membership(self.db_path, license_plate, 'Gold', 365)
        membership_type, expiry_date = check_membership(self.db_path, license_plate)
        self.assertIsNotNone(membership_type, "Membership not found.")
        self.assertEqual(membership_type, 'Gold', "Membership type mismatch.")

if __name__ == '__main__':
    unittest.main()
