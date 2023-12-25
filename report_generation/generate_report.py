class generate_report:
    def __init__(self):
        """
        Constructor for the generate_report class.
        Initializes instance variables to store analysis data.
        Customize this file for your needs to generate report
        """
        # Initialize instance variables to store analysis data
        self.analysis_data_1 = None
        self.analysis_data_2 = None
        self.analysis_data_3 = None

    def generate_report(self, data1, data2, data3):
        """
        Method to generate a report by assigning analysis data to instance variables.

        Parameters:
        - data1: The first set of analysis data.
        - data2: The second set of analysis data.
        - data3: The third set of analysis data.
        """
        # Assign data1 to analysis_data_1
        self.analysis_data_1 = data1
        # Assign data2 to analysis_data_2
        self.analysis_data_2 = data2
        # Assign data3 to analysis_data_3
        self.analysis_data_3 = data3

        # Print analysis_data_1
        print("Analysis Data 1:")
        print(self.analysis_data_1)

        # Print analysis_data_2
        print("Analysis Data 2:")
        print(self.analysis_data_2)

        # Print analysis_data_3
        print("Analysis Data 3:")
        print(self.analysis_data_3)

