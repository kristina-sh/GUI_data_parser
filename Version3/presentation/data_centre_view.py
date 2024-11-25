import tkinter as tk

class DataCentreAvailabilityView:
    """
    Presentation Layer

    This class handles the display of messages, user input, and record details in the console.
    Author:
    - Kristina Shalaginova
    """

    def __init__(self, root) -> None:
        """
        Initializes a DataCentreAvailabilityView object with a tkinter.Tk() parameter.

        Args:
            root (tkinter.Tk()): instance of tkinter frame. It helps to display the root window and manages all it's components.
        """
        self.root = root
        self.root.title("Data Centre Availability by Kristina Shalaginova")
        self.root.geometry("800x600")
        self.root.minsize(width=800, height=800)

        # Display area for text data and records
        self.records_text = tk.Text(root, height=20, width=110)
        self.records_text.pack(pady=10)

        # Printing the initial statement in records_text area
        self.records_text.insert(tk.END, "Initializing GUI...\n")

    def display_text(self, text_to_display):
        """
        Displays text in the text area.
        """
        self.records_text.insert(tk.END, text_to_display + "\n")

    def display_header(self):
        """
        Displays a header with the name of the Program author.
        """
        header = "*" * 80 + "\n" + "*" * 28 + "  Kristina Shalaginova  " + "*" * 28 + "\n" + "*" * 80
        # self.records_text.insert(tk.END, header + "\n")
        self.display_text(header)
           
    def display_menu(self):
        """
        Display a text hint what to do next.
        """
        self.display_text("Click a menu button below")

    def display_records(self, records):
        """
        Displays details of multiple records.

        Args:
            records (list): List of records to be displayed.
        """
        for record in records:
            self.display_header()
            self.display_text(f"Record ID: {record.get_id()}")
            self.display_text(f"Fiscal Year: {record.get_fiscal_year()}")
            self.display_text(F"Fiscal Period: {record.get_fiscal_period()}")
            self.display_text(f"Month: {record.get_month()}")
            self.display_text(f"Information Date: {record.get_information_date()}")
            self.display_text(f"Branch: {record.get_branch()}")
            self.display_text(f"Service: {record.get_service()}")
            self.display_text(f"SSC Client: {record.get_ssc_client()}")
            self.display_text(f"Metric Name: {record.get_metric_name()}")
            self.display_text(f"Value: {record.get_value()}")
            self.display_text(f"Metric Type: {record.get_metric_type()}")

    def display_record(self, record):
        """
        Displays details of a specific record.

        Args:
            record: The record to be displayed.
        """
        if record:
            self.display_header()
            self.display_text(f"Record ID: {record.get_id()}")
            self.display_text(f"Fiscal Year: {record.get_fiscal_year()}")
            self.display_text(F"Fiscal Period: {record.get_fiscal_period()}")
            self.display_text(f"Month: {record.get_month()}")
            self.display_text(f"Information Date: {record.get_information_date()}")
            self.display_text(f"Branch: {record.get_branch()}")
            self.display_text(f"Service: {record.get_service()}")
            self.display_text(f"SSC Client: {record.get_ssc_client()}")
            self.display_text(f"Metric Name: {record.get_metric_name()}")
            self.display_text(f"Value: {record.get_value()}")
            self.display_text(f"Metric Type: {record.get_metric_type()}")
        else:
            self.display_text(f"Error: Record not found.")