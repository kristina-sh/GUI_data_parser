from presentation.data_centre_view import DataCentreAvailabilityView as View
from persistence.data_store import DataStore as DataStore
from model.data_centre_availability_object import DataCentreAvailabilityObject as Record


class DataCentreController():
    """
    Controller class for managing data related to data centers.

    Attributes:
        data_folder_path (str): String variable storing the path to the data folder.
        data_file_path (str): String variable storing the path to the CSV file to be opened.

    Methods:
        __init__():
            Initializes the DataCentreController instance, loading initial data from the CSV file.

        reload_data(filename: str):
            Reloads data from the specified file.

        persist_data(filename: str):
            Persists data to the specified file.

        display_all_records():
            Displays all records.

        display_record(record_id: int):
            Displays the record with the given record_id.

        edit_record(record_id: int):
            Edits the record with the specified record_id.

        delete_record(record_id: int):
            Deletes the record with the specified record_id.

        run():
            Starts the program, displaying a menu and handling user choices.
        Author:
        - Kristina Shalaginova

    """

    # String variable to store path to the data folder
    data_folder_path = "data_files/"

    # String variable to store the csv file name that should be opened
    data_file_path = data_folder_path + "DataCentreAvailability.csv"

    def __init__(self):
      
        self.datastore = DataStore()
        self.view = View()
        print("Loading initial data...")
        self.datastore.load_data(self.data_file_path)

    def reload_data(self, filename):
        
        self.datastore.load_data(filename)

    def persist_data(self, filename):
       
        self.datastore.save_data(filename)
    
    def display_all_records(self):
       
        records = self.datastore.get_all_records()
        self.view.display_records(records)

    def display_record(self, record_id):
       
        record = self.datastore.get_record(record_id)
        self.view.display_record(record)

    def edit_record(self, record_id):
       
        new_data = {}
        new_data['_id'] = int(input("Enter new Record ID: "))
        new_data['fiscal_year'] = input("Enter Fiscal Year: ")
        new_data['fiscal_period'] = input("Enter Fiscal Period: ")
        new_data['month'] = input("Enter Month: ")
        new_data['information_date'] = input("Enter Information Date: ")
        new_data['branch'] = input("Enter Branch: ")
        new_data['service'] = input("Enter Service: ")
        new_data['ssc_client'] = input("Enter SSC Client: ")
        new_data['metric_name'] = input("Enter Metric Name: ")
        new_data['value'] = input("Enter Value: ")
        new_data['metric_type'] = input("Enter Metric Type: ")
        new_record = Record(**new_data)
        
        record = self.datastore.get_record(record_id)
        if record:
            self.datastore.delete_record(record)
        self.datastore.add_record(new_record)

        print("Data entered successfully!")

    def delete_record(self, record_id):
        
        record = self.datastore.get_record(record_id)
        if record:
            self.datastore.delete_record(record)
            print("Record deleted successfully.")
        else:
            print("Record not found.")


    def run(self):
       
        while True:
            self.view.display_header()
            self.view.display_menu()

            choice = input("Enter your choice (1-8): ")

            if choice == '1':
                print("Reloading data from the Dataset...")
                self.reload_data(self.data_file_path)
                
            elif choice == '2':
                new_file_path = input("Enter the new file name to write data: ")
                print("Saving data to the disk...")
                self.persist_data(self.data_folder_path + new_file_path)

            elif choice == '3':
                self.view.display_records(self.datastore.records)

            elif choice == '4':
                record_id = input("Enter the Record ID: ")
                record_id_int = int(record_id)
                self.display_record(record_id_int)

            elif choice == '5':

                # Creating Input data object for a new record
                new_data = {}

                # Get user input for each attribute
                new_data['_id'] = int(input("Enter Record ID: "))

                if self.datastore.get_record(new_data['_id']):
                    print("Record with Record Id " + str(new_data['_id']) + " already exist")
                else:
                    new_data['fiscal_year'] = input("Enter Fiscal Year: ")
                    new_data['fiscal_period'] = input("Enter Fiscal Period: ")
                    new_data['month'] = input("Enter Month: ")
                    new_data['information_date'] = input("Enter Information Date: ")
                    new_data['branch'] = input("Enter Branch: ")
                    new_data['service'] = input("Enter Service: ")
                    new_data['ssc_client'] = input("Enter SSC Client: ")
                    new_data['metric_name'] = input("Enter Metric Name: ")
                    new_data['value'] = input("Enter Value: ")
                    new_data['metric_type'] = input("Enter Metric Type: ")
                    new_record = Record(**new_data)
                    self.datastore.add_record(new_record)
                    print("New record created successfully.")

            elif choice == '6':
                
                # Get user input for each attribute
                record_id = int(input("Enter Record ID: "))
                self.edit_record(record_id)

            elif choice == '7':
                record_id = int(input("Enter the Record ID to delete: "))
                self.delete_record(record_id)

            elif choice == '8':
                print("Exiting program...")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 8.")
