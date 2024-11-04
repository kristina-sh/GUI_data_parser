import unittest
from controller.data_centre_controller import DataCentreController as Controller
from presentation.data_centre_view import DataCentreAvailabilityView as View

class TestDataCentreControllerFileMissing(unittest.TestCase):
    """
    Unit tests for handling file-related scenarios in the DataCentreController class.

    This test suite focuses on verifying the behavior of DataCentreController
    when dealing with the presence and absence of the specified data file.

    Test Methods:
    - test_data_file_exists_happy_path: Tests the successful reload of data when the file exists.
    - test_data_file_does_not_exist_rainy_day: Tests the handling of a FileNotFoundError
      when attempting to reload data with a non-existent file.

    Author: Kristina Shalaginova
    """

    def setUp(self):
        """
        Set up the test environment by initializing the DataCentreController and DataCentreAvailabilityView.
        """
        self.controller = Controller()
        self.view = View()

    def tearDown(self):
        """
        Clean up resources after each test case (not implemented for this test class).
        """
        pass

    def test_data_file_exists_happy_path(self):
        """
        Test the successful reload of data when the file exists.

        Verifies that the data file is reloaded without errors and the records are not empty.

        Raises:
            AssertionError: If the test conditions are not met.
        """
        self.view.display_header()
        self.controller.reload_data(self.controller.data_file_path)

        self.assertIsNotNone(self.controller.datastore.records)
        self.assertNotEqual(len(self.controller.datastore.records), 0)

    def test_data_file_does_not_exist_rainy_day(self):
        """
        Test the handling of a FileNotFoundError when attempting to reload data with a non-existent file.

        Verifies that the appropriate exception is raised when trying to reload data from a non-existent file.

        Raises:
            AssertionError: If the test conditions are not met.
        """
        self.view.display_header()
        try:
            self.controller.reload_data(self.controller.data_file_path + "wrong_filename")
        except FileNotFoundError as error:
            self.assertEqual(str(error), "File not found")

if __name__ == '__main__':
    unittest.main(verbosity=2)


