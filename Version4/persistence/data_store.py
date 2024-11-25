import pandas

from model.data_centre_availability_object import DataCentreAvailabilityObject


class DataStore:
    """
    Controller class for managing data related to data centers.

    Attributes:
        data_folder_path (str): String variable storing the path to the data folder.
        data_file_path (str): String variable storing the path to the CSV file to be opened.

    Methods:
        __init__(): Initializes the DataCentreController instance, loading initial data from the CSV file.
        reload_data(filename: str): Reloads data from the specified file.
        persist_data(filename: str): Persists data to the specified file.
        display_all_records(): Displays all records.
        display_record(record_id: int): Displays the record with the given record_id.
        edit_record(record_id: int): Edits the record with the specified record_id.
        delete_record(record_id: int): Deletes the record with the specified record_id.
        show_input_field_for_record_id(self, action="Submit"): Shows an input field for entering a record ID.
        show_input_fields_for_record(self, action="Submit"): Shows input fields for entering or editing a record's details.
        action_by_fields(self, record_id, action): Executes an action (Create or Edit) based on the input fields' data.
        action_by_record_id(self, record_id, action): Executes an action (Display or Delete) based on the provided record ID.

    Author:
    - Kristina Shalaginova
"""


    def __init__(self):
        
        self.records = []

    def add_record(self, record):
        
        self.records.append(record)

    def load_data(self, file_path, num_records=100):
       
        # Exception handling for csv file reading
        try:
            # Read CSV file into a pandas DataFrame
            data_frame = pandas.read_csv(file_path, nrows=num_records)
            # Standardize column names by converting to lowercase and replacing spaces with underscores
            data_frame.columns = [col.lower().replace(' ', '_') for col in data_frame.columns]
            # Iterate over data_frame rows and create DataCentreAvailabilityObject instances
            for _, row in data_frame.iterrows():
                record = DataCentreAvailabilityObject(**row)
                self.records.append(record)
            return "Data loaded successfully!"

        except FileNotFoundError:
            return f"Error: File '{file_path}' not found."
        except Exception as e:
            return f"Error: {e}"

    def save_data(self, file_path):
        
        # Exception handling for file writing
        try:
            data = [vars(record) for record in self.records]
            pandas.DataFrame(data).to_csv(file_path, index=False)
            return "Data saved successfully!"

        except Exception as e:
            return f"Error: {e}"
    
    def get_all_records(self):
       
        return self.records

    def get_record(self, record_id):
        
        # moving record_id index to the left
        # record_ids in the list are have indexes from 0 to 99, 
        # indexes in the csv file are from 1 to 100.

        record = next((record for record in self.records if record.get_id() == record_id), None)
        return record

    def delete_record(self, record):
        
        self.records.remove(record)
    
    def create_data_for_chart(self, column_name):
        chart_data = []
        power_cons_list = []
        months_set = set()
        records = self.get_all_records()
        for record in records:
            if record.get_metric_name() == column_name:
                power_cons_list.append(record)
        for power_cons in power_cons_list:
            months_set.add(power_cons.get_month())
        for month in months_set:
            value_bar_label_list = []
            for power_cons in power_cons_list:
                if month == power_cons.get_month():
                    value_bar_label_tuple = (power_cons.get_value(), power_cons.get_ssc_client())
                    value_bar_label_list.append(value_bar_label_tuple)
            # print(value_bar_label_list)
            group_value_bar_label_pair_tuple = (month, value_bar_label_list)
            chart_data.append(group_value_bar_label_pair_tuple)
        # print(chart_data)        
        return chart_data
