from controller.data_centre_controller import DataCentreController as Controller

def main():
    """
    Main function to run the program.

    It initializes the controller and starts the program.

    Returns:
        None
    """
    print("Initializing controller and running program...")
    controller = Controller()
    controller.run()