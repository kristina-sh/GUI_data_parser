import tkinter as tk

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
        
        show_input_field_for_record_id(self, action="Submit"): 
            Shows an input field for entering a record ID.

        show_input_fields_for_record(self, action="Submit"): 
            Shows input fields for entering or editing a record's details.

        action_by_fields(self, record_id, action): 
            Executes an action (Create or Edit) based on the input fields' data.

        action_by_record_id(self, record_id, action): 
            Executes an action (Display or Delete) based on the provided record ID.

        Author:
        - Kristina Shalaginova

    """

    # String variable to store path to the data folder
    data_folder_path = "data_files/"

    # String variable to store the csv file name that should be opened
    data_file_path = data_folder_path + "DataCentreAvailability.csv"

    def __init__(self, root):
        self.root = root
        self.datastore = DataStore()
        self.view = View(root)
        #loading_result = self.datastore.load_data(self.data_file_path)
        #self.view.records_text.insert(tk.END, loading_result + "\n")
        self.view.display_header()
        self.reload_data(self.data_file_path)
        self.view.display_menu()

        # Display menu options
        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack(pady=10)
        # Using a simple way to bind arguments in command function without an explicit wrapper method or modifying the original function.
        tk.Button(self.menu_frame, text="Reload Data from Dataset", command=lambda: self.reload_data(self.data_file_path)).grid(row=0, column=0, pady=5)
        tk.Button(self.menu_frame, text="Persist Data to Disk", command=lambda: self.persist_data(self.data_file_path)).grid(row=0, column=1, pady=5)
        tk.Button(self.menu_frame, text="Display All Records", command=lambda: self.display_all_records()).grid(row=1, column=0, pady=5)
        tk.Button(self.menu_frame, text="Display Specific Record", command=lambda: self.show_input_field_for_record_id("Display")).grid(row=1, column=1, pady=5)
        tk.Button(self.menu_frame, text="Create New Record", command=lambda: self.show_input_fields_for_record("Create")).grid(row=2, column=0, pady=5)
        tk.Button(self.menu_frame, text="Edit Record", command=lambda: self.show_input_fields_for_record("Edit")).grid(row=2, column=1, pady=5)
        tk.Button(self.menu_frame, text="Delete Record", command=lambda: self.show_input_field_for_record_id("Delete")).grid(row=3, column=0, pady=5)
        tk.Button(self.menu_frame, text="Exit", command=self.root.quit).grid(row=3, column=1, pady=5)

    def show_input_field_for_record_id(self, action="Submit"):
        self.input_field_for_id = tk.Entry(self.menu_frame)
        self.input_field_for_id.grid(row=4, column=0, pady=5)
        self.input_field_for_id.insert(0, "Please enter Record ID")
        self.input_field_for_id.config(fg='grey') 
        self.submit_record_id_button = tk.Button(self.menu_frame, text=action, command=lambda: self.action_by_record_id(self.input_field_for_id.get(), action)).grid(row=4, column=1, pady=5)

    def show_input_fields_for_record(self, action="Submit"):
        
        self.submit_fields_button = tk.Button(self.menu_frame, text=action, command=lambda: self.action_by_fields(self.input_field_for_record_id.get(), action)).grid(row=0, column=4, pady=5)
        
        self.input_field_for_record_id = tk.Entry(self.menu_frame)
        self.input_field_for_record_id.grid(row=0, column=3, pady=5)
        self.input_field_for_record_id.insert(0, "Please enter Record ID")
        self.input_field_for_record_id.config(fg='grey')
        
        self.input_field_for_fiscal_year = tk.Entry(self.menu_frame)
        self.input_field_for_fiscal_year.grid(row=1, column=3, pady=5)
        self.input_field_for_fiscal_year.insert(0, "Please enter Fiscal Year")
        self.input_field_for_fiscal_year.config(fg='grey')

        self.input_field_for_fiscal_period = tk.Entry(self.menu_frame)
        self.input_field_for_fiscal_period.grid(row=2, column=3, pady=5)
        self.input_field_for_fiscal_period.insert(0, "Please enter Fiscal Period")
        self.input_field_for_fiscal_period.config(fg='grey')

        self.input_field_for_month = tk.Entry(self.menu_frame)
        self.input_field_for_month.grid(row=3, column=3, pady=5)
        self.input_field_for_month.insert(0, "Please enter Month")
        self.input_field_for_month.config(fg='grey')

        self.input_field_for_information_date = tk.Entry(self.menu_frame)
        self.input_field_for_information_date.grid(row=4, column=3, pady=5)
        self.input_field_for_information_date.insert(0, "Please enter Information Date")
        self.input_field_for_information_date.config(fg='grey')

        self.input_field_for_branch = tk.Entry(self.menu_frame)
        self.input_field_for_branch.grid(row=5, column=3, pady=5)
        self.input_field_for_branch.insert(0, "Please enter Branch")
        self.input_field_for_branch.config(fg='grey')

        self.input_field_for_service = tk.Entry(self.menu_frame)
        self.input_field_for_service.grid(row=6, column=3, pady=5)
        self.input_field_for_service.insert(0, "Please enter Service")
        self.input_field_for_service.config(fg='grey')

        self.input_field_for_ssc_client = tk.Entry(self.menu_frame)
        self.input_field_for_ssc_client.grid(row=7, column=3, pady=5)
        self.input_field_for_ssc_client.insert(0, "Please enter SSC Client")
        self.input_field_for_ssc_client.config(fg='grey')

        self.input_field_for_metric_name = tk.Entry(self.menu_frame)
        self.input_field_for_metric_name.grid(row=8, column=3, pady=5)
        self.input_field_for_metric_name.insert(0, "Please enter Metric Name")
        self.input_field_for_metric_name.config(fg='grey')

        self.input_field_for_value = tk.Entry(self.menu_frame)
        self.input_field_for_value.grid(row=9, column=3, pady=5)
        self.input_field_for_value.insert(0, "Please enter Value")
        self.input_field_for_value.config(fg='grey')

        self.input_field_for_metric_type = tk.Entry(self.menu_frame)
        self.input_field_for_metric_type.grid(row=10, column=3, pady=5)
        self.input_field_for_metric_type.insert(0, "Please enter Metric Type")
        self.input_field_for_metric_type.config(fg='grey')

    def action_by_fields(self, record_id, action):
        # catching errors when Record ID is not integer or doesn't exist
        try:
            record_id_int = int(record_id)
            if action == "Edit":
                self.edit_record(record_id_int)
            elif action == "Create":
                new_data = {}
                new_data['_id'] = int(self.input_field_for_record_id.get())
                new_data['fiscal_year'] = self.input_field_for_fiscal_year.get()
                new_data['fiscal_period'] = self.input_field_for_fiscal_period.get()
                new_data['month'] = self.input_field_for_month.get()
                new_data['information_date'] = self.input_field_for_information_date.get()
                new_data['branch'] = self.input_field_for_branch.get()
                new_data['service'] = self.input_field_for_service.get()
                new_data['ssc_client'] = self.input_field_for_ssc_client.get()
                new_data['metric_name'] = self.input_field_for_metric_name.get()
                new_data['value'] = self.input_field_for_value.get()
                new_data['metric_type'] = self.input_field_for_metric_type.get()
                new_record = Record(**new_data)
                self.datastore.add_record(new_record)
    
        except ValueError:
            self.view.display_header()
            self.view.records_text.insert(tk.END, "Value not an integer. Please enter an integer...\n")
        except Exception as e:
            self.view.display_header()
            self.view.records_text.insert(tk.END, f"Error: {e}\n")

    def action_by_record_id(self, record_id, action):
        # catching errors when Record ID is not integer or doesn't exist
        try:
            record_id_int = int(record_id)
            if action == "Display":
                self.display_record(record_id_int)
            elif action == "Delete":
                self.delete_record(record_id_int)
    
        except ValueError:
            self.view.display_header()
            self.view.records_text.insert(tk.END, "Value not an integer. Please enter an integer...\n")
        except Exception as e:
            self.view.display_header()
            self.view.records_text.insert(tk.END, f"Error: {e}\n")

    def reload_data(self, filename):
        self.view.records_text.insert(tk.END, "Reloading data...\n")
        loading_result = self.datastore.load_data(filename)
        self.view.records_text.insert(tk.END, loading_result + "\n")

    def persist_data(self, filename):
        self.view.records_text.insert(tk.END, "Saving data...\n")
        saving_result = self.datastore.save_data(filename+"_new")
        self.view.records_text.insert(tk.END, saving_result + "\n")
    
    def display_all_records(self):
       
        records = self.datastore.get_all_records()
        self.view.display_records(records)

    def display_record(self, record_id):

        record = self.datastore.get_record(int(record_id))
        self.view.display_record(record)

    def edit_record(self, record_id):
       
        new_data = {}
        new_data['_id'] = int(self.input_field_for_record_id.get())
        new_data['fiscal_year'] = self.input_field_for_fiscal_year.get()
        new_data['fiscal_period'] = self.input_field_for_fiscal_period.get()
        new_data['month'] = self.input_field_for_month.get()
        new_data['information_date'] = self.input_field_for_information_date.get()
        new_data['branch'] = self.input_field_for_branch.get()
        new_data['service'] = self.input_field_for_service.get()
        new_data['ssc_client'] = self.input_field_for_ssc_client.get()
        new_data['metric_name'] = self.input_field_for_metric_name.get()
        new_data['value'] = self.input_field_for_value.get()
        new_data['metric_type'] = self.input_field_for_metric_type.get()
        new_record = Record(**new_data)
        
        record = self.datastore.get_record(record_id)
        if record:
            self.datastore.delete_record(record)
        self.datastore.add_record(new_record)

        self.view.display_text("Data entered successfully!")

    def delete_record(self, record_id):
        
        record = self.datastore.get_record(record_id)
        if record:
            self.datastore.delete_record(record)
            self.view.display_header()
            self.view.display_text("Record deleted successfully.")
        else:
            self.view.display_header()
            self.view.display_text("Record not found.")
