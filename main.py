# Import necessary modules
from read_from_csv import read_csv_file
from data_analysis import analyze_data
from report_generation import generate_report
from tkinter import Tk
from user_interface import gui

# Initialize CSV reader instance
read_csv = read_csv_file.read_csv_data()

# Obtain the function/method for reading multiple CSV files
# Note: "read_mult_csv_file" is a function or method defined in the "read_csv_file" module
main_read_csv = read_csv.read_mult_csv_file

# Initialize data analyzer instance
analyze_data = analyze_data.analyze_csv_data()

# Initialize report generator instance
report_gen = generate_report.generate_report()

# Create the main Tkinter window
root = Tk()
root.title('Csv DataAnalyzer')  # Set the title of the Tkinter window
root.geometry("800x600")  # Set the initial dimensions of the Tkinter window

# Create the user interface (GUI) using the UI class from the "user_interface" module
# Pass the necessary components (main_read_csv, analyze_data, report_gen) to the GUI
gui.UI(root, main_read_csv, analyze_data, report_gen)

# Start the Tkinter event loop to run the GUI
root.mainloop()
