import app.app
import unittest

class flask_app_demo(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()                # creates a test client
        self.app.testing = True                     # propagate the exceptions to the test client

    def tearDown(self):
        pass

###############################################################################
### <Test>
###############################################################################
    def test_home_status_code(self):
        result = self.app.get('/')                  # sends HTTP GET to application
        self.assertEqual(result.status_code, 200)   # assert the status code of the response

    def test_home_data(self):
        result = self.app.get('/')                  # sends HTTP GET to application
        self.assertEqual(result.data, "Hello World!!!")          # assert the response data

###############################################################################
### </Test>
###############################################################################
if __name__ == '__main__':                                  # pragma: no cover
    suite = unittest.TestLoader().loadTestsFromTestCase(flask_app_demo)
    unittest.TextTestRunner(verbosity=2).run(suite)
