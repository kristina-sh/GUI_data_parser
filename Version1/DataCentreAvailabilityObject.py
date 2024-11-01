import pandas 

class DataCentreAvailabilityObject:
    """
    Class representing a data record for DataCentreAvailability.

    Attributes:
    - _id (str): Unique id identifier which assosiated with the record.
    - fiscal_year (str): Fiscal year which associated with the record.
    - fiscal_period (str): Fiscal period which associated with the record.
    - month (str): Month which associated with the record.
    - information_date (str): Date which associated with the record.
    - branch (str): Branch which associated with the record.
    - service (str): Service which associated with the record.
    - ssc_client (str): SSC client which associated with the record.
    - metric_name (str): Name of the metric which associated with the record.
    - value (str): Value which associated with the record.
    - metric_type (str): Type of the metric which associated with the record.

    Methods:
    - get_id(): Returns the unique id identifier.
    - get_fiscal_year(): Returns the fiscal year.
    - get_fiscal_period(): Returns the fiscal period.
    - get_month(): Returns the month.
    - get_information_date(): Returns the information date.
    - get_branch(): Returns the branch.
    - get_service(): Returns the service.
    - get_ssc_client(): Returns the SSC client.
    - get_metric_name(): Returns the metric name.
    - get_value(): Returns the metric value.
    - get_metric_type(): Returns the metric type.
    - set_id(_id): Sets the unique id identifier.
    - set_fiscal_year(fiscal_year): Sets the fiscal year.
    - set_fiscal_period(fiscal_period): Sets the fiscal period.
    - set_month(month): Sets the month.
    - set_information_date(information_date): Sets the information date.
    - set_branch(branch): Sets the branch.
    - set_service(service): Sets the service.
    - set_ssc_client(ssc_client): Sets the SSC client.
    - set_metric_name(metric_name): Sets the metric name.
    - set_value(value): Sets the metric value.
    - set_metric_type(metric_type): Sets the metric type.
    Author:
    - Kristina Shalaginova 
    """
    
    def __init__(self, _id, fiscal_year, fiscal_period, month, information_date, branch, service, ssc_client, metric_name,
                  value, metric_type):
        self._id = _id
        self.fiscal_year = fiscal_year
        self.fiscal_period = fiscal_period
        self.month = month
        self.information_date = information_date
        self.branch = branch
        self.service = service
        self.ssc_client = ssc_client
        self.metric_name = metric_name
        self.value = value
        self.metric_type = metric_type

    # Accessor methods (getters)
    def get_id(self):
        return self._id

    def get_fiscal_year(self):
        return self.fiscal_year

    def get_fiscal_period(self):
        return self.fiscal_period

    def get_month(self):
        return self.month

    def get_information_date(self):
        return self.information_date

    def get_branch(self):
        return self.branch

    def get_service(self):
        return self.service

    def get_ssc_client(self):
        return self.ssc_client

    def get_metric_name(self):
        return self.metric_name

    def get_value(self):
        return self.value

    def get_metric_type(self):
        return self.metric_type

    # Mutator methods (setters)
    def set_id(self, _id):
        self._id = _id

    def set_fiscal_year(self, fiscal_year):
        self.fiscal_year = fiscal_year

    def set_fiscal_period(self, fiscal_period):
        self.fiscal_period = fiscal_period

    def set_month(self, month):
        self.month = month

    def set_information_date(self, information_date):
        self.information_date = information_date

    def set_branch(self, branch):
        self.branch = branch

    def set_service(self, service):
        self.service = service

    def set_ssc_client(self, ssc_client):
        self.ssc_client = ssc_client

    def set_metric_name(self, metric_name):
        self.metric_name = metric_name

    def set_value(self, value):
        self.value = value

    def set_metric_type(self, metric_type):
        self.metric_type = metric_type

def read_csv_file(file_path, num_records=5):
    """
    Reads data from a CSV file and creates DataCentreAvailabilityObject instances.

    Parameters:
    - file_path (str): Path to the CSV file.
    - num_records (int): Number of records that should be read from the CSV file.

    Returns:
    - List[DataCentreAvailabilityObject]: List of DataCentreAvailabilityObject instances.
    """

    # Initializing an empty list for the Data Centre Availability Objects
    record_objects = []
    
    # Try - except block for reading csv file and catching for 'File not found' and other errors
    try:
        # Using the read csv pandas API to read a file with comma-separated values into DataFrame
        data_frame = pandas.read_csv(file_path, nrows=num_records)

        # Convert to lowercase and replace spaces with underscores
        data_frame.columns = [col.lower().replace(' ', '_') for col in data_frame.columns]  

        # for loop to add record objects to the list
        for _, row in data_frame.iterrows():
            record = DataCentreAvailabilityObject(**row)
            record_objects.append(record)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

    return record_objects

    
def display_header():
    """
    Displays a header with the name of the Program author.
    """
    print("*"*54)
    print("*"*15 + "  Kristina Shalaginova  " + "*"*15)
    print("*"*54)


# String variable to store csv file name that should be opened
file_path = 'DataCentreAvailability.csv'

# Reading the csv file
records = read_csv_file(file_path)

# Output record data from the DataCentreAvailability.csv file on screen with name of the Program author after each record
for record in records:
    display_header()
    print(f"Record ID: {record.get_id()}")
    print(f"Fiscal Year: {record.get_fiscal_year()}")
    print(F"Fiscal Period: {record.get_fiscal_period()}")
    print(f"Month: {record.get_month()}")
    print(f"Information Date: {record.get_information_date()}")
    print(f"Branch: {record.get_branch()}")
    print(f"Service: {record.get_service()}")
    print(f"SSC Client: {record.get_ssc_client()}")
    print(f"Metric Name: {record.get_metric_name()}")
    print(f"Value: {record.get_value()}")
    print(f"Metric Type: {record.get_metric_type()}")
  
 