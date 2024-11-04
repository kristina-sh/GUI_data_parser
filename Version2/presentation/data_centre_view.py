class DataCentreAvailabilityView:
    """
    Presentation Layer

    This class handles the display of messages, user input, and record details in the console.
    Author:
    - Kristina Shalaginova
    """

    def __init__(self) -> None:
        """
        Initializes a DataCentreAvailabilityView object.
        """
        pass

    def display_header(self):
        """
        Displays a header with the name of the Program author.
        """
        print("*"*54)
        print("*"*15 + "  Kristina Shalaginova  " + "*"*15)
        print("*"*54)
                        
    def display_menu(self):
        """
        Displays a menu with options for the user.
        """
        print("1. Reload Data from Dataset")
        print("2. Persist Data to Disk")
        print("3. Display All Records")
        print("4. Display Specific Record")
        print("5. Create New Record")
        print("6. Edit Record")
        print("7. Delete Record")
        print("8. Exit")
        
    def display_records(self, records):
        """
        Displays details of multiple records.

        Args:
            records (list): List of records to be displayed.
        """
        for record in records:
            self.display_header()
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

    def display_record(self, record):
        """
        Displays details of a specific record.

        Args:
            record: The record to be displayed.
        """
        if record:
            self.display_header()
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
        else:
            print(f"Error: Record not found.")