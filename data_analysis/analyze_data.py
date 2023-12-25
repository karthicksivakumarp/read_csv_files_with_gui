class analyze_csv_data:
    # Customize this file for your needs to analyze data
    def __init__(self):
        # Initialize variables to store data frames, file paths, and columns
        self.df_list = None
        self.csv_filepaths = None
        self.columns = None

    def pass_data_frame(self, df_list, csv_filepaths, columns):
        # Method to pass data frames, file paths, and columns to the analyzer
        self.df_list = df_list
        self.csv_filepaths = csv_filepaths
        self.columns = columns

    def analyze_data_all(self):
        # Method to analyze data for all CSV files
        for n in range(len(self.df_list)):
            print(n)
            print(self.df_list[n])
            print(self.csv_filepaths[n])
            print(self.columns)

    def analyze_data_single_csv(self, index):
        # Method to analyze data for a single CSV file specified by index
        print(self.df_list[index])
        print(self.csv_filepaths[index])
        print(self.columns)
