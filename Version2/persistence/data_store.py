import pandas

from model.data_centre_availability_object import DataCentreAvailabilityObject


class DataStore:
    """
    Model Layer: Persistence Layer

    It provides functionality for storing and manipulating records in the data store.

    Attributes:
        records (list): A list of  objects representing the records in the data store.
    Author:
    - Kristina Shalaginova
    """

    def __init__(self):
        """
        Initializes an empty DataStore object.
        """
        self.records = []

    def add_record(self, record):
        """
        Adds a new record to the data store.

        Args:
            record (DataCentreAvailabilityObject): represents the record to be added.
        """
        self.records.append(record)

    def load_data(self, file_path, num_records=100):
        """
        Loads data from a CSV file into the data store.

        Args:
            file_path (str): The path to the CSV file.
            num_records (int): The number of records to load (default is 100).
        """
        # Exception handling for file reading
        try:
            data_frame = pandas.read_csv(file_path, nrows=num_records)
            data_frame.columns = [col.lower().replace(' ', '_') for col in data_frame.columns]

            for _, row in data_frame.iterrows():
                record = DataCentreAvailabilityObject(**row)
                self.records.append(record)
            print("Data loaded successfully!")

        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except Exception as e:
            print(f"Error: {e}")

    def save_data(self, file_path):
        """
        Saves data from the data store to a CSV file.

        Args:
            file_path (str): The path to the CSV file.
        """
        # Exception handling for file writing
        try:
            data = [vars(record) for record in self.records]
            pandas.DataFrame(data).to_csv(file_path, index=False)
            print("Data saved successfully!")

        except Exception as e:
            print(f"Error: {e}")
    
    def get_all_records(self):
        """
        Retrieves all records from the data store.

        Returns:
            list: A list of all Record objects in the data store.
        """
        return self.records

    def get_record(self, record_id):
        """
        Retrieves a record from the data store based on the index.

        Args:
            record_id (int): The index of the record to retrieve.

        Returns:
            RecordObject or None: The record object if found, None if index is out of range.
        """
        # moving record_id index to the left
        # record_ids in the list are have indexes from 0 to 99, 
        # indexes in the csv file are from 1 to 100.

        record = next((record for record in self.records if record.get_id() == record_id), None)
        return record

    def delete_record(self, record):
        """
        Deletes a record from the data store.

        Args:
            record (Record): represents the record to be deleted.
        """
        self.records.remove(record)

