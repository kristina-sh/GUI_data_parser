import tkinter as tk

class DataCentreAvailabilityView:
   

    """
    Presentation Layer

    This class handles the display of messages, user input, and record details using tkinter.

    Author:
    - Kristina Shalaginova

    Methods:
        __init__(root): Initializes a DataCentreAvailabilityView object with a tkinter.Tk() parameter.
        display_text(text_to_display): Displays text in the text area.
        display_header(): Displays a header with the name of the Program author.
        display_menu(): Display a text hint what to do next.
        display_records(records): Displays details of multiple records.
        display_record(record): Displays details of a specific record.
        draw_horizontal_chart(chart_title, horizontal_chart_data): Draws a horizontal bar chart.
        draw_vertical_chart(chart_title, vertical_chart_data): Draws a vertical bar chart.
    """

    def __init__(self, root) -> None:
        
        self.root = root
        self.root.title("Data Centre Availability by Kristina Shalaginova")
        self.root.geometry("800x800")
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
        
        self.display_text("Click a menu button below")

    def display_records(self, records):
        
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
    
    def draw_horizontal_chart(self, chart_title, horizontal_chart_data):
        
        # Initialize the horizontal chart window
        root_horizontal_chart = tk.Tk()
        root_horizontal_chart.title(chart_title + " Horizontal Bar Chart with Labels")
        # Create a canvas for drawing
        canvas_width = 570  # Adjusted to provide more space for bar labels
        canvas_height = 870  # Adjusted for potentially more bars
        canvas = tk.Canvas(root_horizontal_chart, width=canvas_width, height=canvas_height)
        canvas.pack()

        # Settings for the bar chart
        single_bar_height = 17
        group_gap = 15  # Gap between groups of bars
        bar_gap = 4  # Gap between bars within a group
        offset_left = 100
        max_value = max([max(values, key=lambda item: item[0])[0] for label, values in horizontal_chart_data])
        scale = (canvas_width - offset_left - 80) / max_value  # Adjusted for text space

        # Draw the bars and their labels
        current_y = group_gap
        for label, values in horizontal_chart_data:
            num_bars = len(values)
            group_height = num_bars * single_bar_height + (num_bars - 1) * bar_gap
            for i, (value, bar_label) in enumerate(values):
                # Calculate bar coordinates
                x0 = offset_left
                y0 = current_y + i * (single_bar_height + bar_gap)
                x1 = x0 + value * scale
                y1 = y0 + single_bar_height
                # Draw the bar
                canvas.create_rectangle(x0, y0, x1, y1, fill="blue")
                # Draw the bar label
                canvas.create_text(x1 + 5, (y0 + y1) / 2, anchor="w", text=bar_label)
            # Draw the group label
            middle_bar_y0 = current_y + (num_bars // 2) * (single_bar_height + bar_gap)
            middle_bar_y1 = middle_bar_y0 + single_bar_height
            canvas.create_text(x0 - 10, (middle_bar_y0 + middle_bar_y1) / 2, anchor="e", text=label)
            current_y += group_height + group_gap

    def draw_vertical_chart(self, chart_title, vertical_chart_data):
        # Data for the bar chart
        data = vertical_chart_data

        # Initialize the main window
        root = tk.Tk()
        root.title(chart_title + " Vertical Bar Chart")

        # Calculate canvas width dynamically based on the data
        canvas_width = max(len(month_data) for _, month_data in data) * (len(data) * 35) + 270
        canvas_height = 570

        # Create a canvas on which to draw the bars
        canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
        canvas.pack()

        # Parameters for the bar chart layout
        max_height = 400  # Maximum height of a bar
        bar_width = 30  # The width of each bar
        group_spacing = 50  # Space between groups of bars
        bar_spacing = 10  # Space between bars within a group
        y_offset = canvas_height - 50  # Distance from the bottom (to draw the chart from bottom-up)

        # Calculate the maximum value to scale bars accordingly
        max_value = max([max([value for value, _ in month_data]) for _, month_data in data])

        # Initial x_offset
        x_offset = 50

        # Process each month
        for month, values in data:
            # Draw each bar in the month
            for i, (value, label) in enumerate(values):
                # Scale the bar height according to the value it represents
                bar_height = (value / max_value) * max_height
                # Calculate the bottom left and top right coordinates of the bar
                x1 = x_offset + i * (bar_width + bar_spacing)
                y1 = y_offset - bar_height
                x2 = x1 + bar_width
                y2 = y_offset
                # Draw the bar
                canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
                # Label the bar with its label ABOVE the bar
                canvas.create_text(x1 - 15 + bar_width / 2, y1 - 10, text=label)

            # Label the month below the group
            canvas.create_text(x1 - (bar_width + bar_spacing) * (len(values) / 2), y2 + 40, text=month)

            # Update the x_offset for the next group
            x_offset += len(values) * (bar_width + bar_spacing) + group_spacing
