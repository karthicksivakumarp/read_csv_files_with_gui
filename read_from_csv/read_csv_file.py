import pandas as pd
import tkinter.filedialog as tkfd


class read_csv_data:
    def __init__(self):
        # Initialize variables to store CSV file paths and data frames
        self.csv_file_paths = None
        self.df = None
        self.df_reversed = None

    def read_mult_csv_file(self):
        # Method to read multiple CSV files and return a list of reversed data frames
        df_list = []  # List to store data frames
        fType = [('CSV', '*.csv')]  # File type for file dialog
        self.csv_file_paths = tkfd.askopenfilenames(title='Select csv files', filetypes=fType)  # Open file dialog
        print(f"Total {len(self.csv_file_paths)} csv files selected")

        # Read the first 2 lines of the first CSV file to identify the delimiter and decimal separator
        with open(self.csv_file_paths[0], 'r') as file:
            lines = [next(file) for _ in range(2)]

        delimiter = ','  # Default delimiter
        decimal_separator = '.'  # Default decimal separator

        # Check for common delimiters and decimal separators in the first 2 lines
        for line in lines:
            if ',' in line:
                delimiter = ','
                break
            elif ';' in line:
                delimiter = ';'
                break
            elif '\t' in line:
                delimiter = '\t'
                break
            elif '|' in line:
                delimiter = '|'
                break
            if ',' in line:
                decimal_separator = ','
                break
            elif '.' in line:
                decimal_separator = '.'
                break

        # Read each CSV file, set delimiter and decimal separator, reverse the data frame, and add it to the list
        for path in self.csv_file_paths:
            df = pd.read_csv(filepath_or_buffer=path, delimiter=delimiter, decimal=decimal_separator)
            df_reversed = df[::-1].reset_index(drop=True)  # Reverse the data frame and reset the index
            df_list.append(df_reversed)

        columns = df_list[0].columns  # Extract column names from the first data frame
        return df_list, self.csv_file_paths, columns  # Return the list of data frames, file paths, and columns
