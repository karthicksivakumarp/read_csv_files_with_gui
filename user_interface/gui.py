import os
from tkinter import Frame, Label, Listbox, Scrollbar, VERTICAL, HORIZONTAL, BOTH, END, ttk, TOP
from tkinter import Menu, BOTTOM, Entry, X


class UI(Frame):
    def __init__(self, root, ui_read_csv, ui_data_analysis, ui_report_gen):
        # Initialize the UI frame and its components
        super().__init__(root)
        # Various UI elements
        self.notebook = None
        self.selected_index = None
        self.selected_item = None
        self.tab_grapher = None
        self.tab_statistics = None
        self.tab_dataframe = None
        self.data_list_tree_view = None
        self.header_listbox = None
        self.columns = None
        self.csv_paths = None
        self.df_list = None
        self.filename_listbox = None
        self.left_frame_bottom = None
        self.left_frame_top = None
        self.right_frame_root = None
        self.master = root
        self.menu = None

        # Instances of other UI components
        self.read_mult_csv = ui_read_csv

        self.pass_data_for_analysis = ui_data_analysis.pass_data_frame
        self.analyze_single_csv = ui_data_analysis.analyze_data_single_csv
        self.analyze_data_all = ui_data_analysis.analyze_data_all
        self.generate_report = ui_report_gen.generate_report

        # Initialize UI elements
        self.init_menu_bar()
        self.config_frame()
        self.top_left_frame()
        self.bottom_left_frame()
        self.right_frame()

    def set_status_message(self, message):
        # Set the status message in the Entry widget
        self.status_text.config(state="normal")
        self.status_text.delete(0, END)  # Clear the existing message
        self.status_text.insert(0, message)
        self.status_text.config(state="disabled", bg="white")

    def init_menu_bar(self):
        # Initialize the menu bar with commands
        self.menu = Menu(self.master)

        file_menu = Menu(self.menu, tearoff=0)
        file_menu.add_command(label='Import csv file', command=self.read_csv_files)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.master.quit)

        self.menu.add_cascade(label='Files', menu=file_menu)

        analyze_menu = Menu(self.menu, tearoff=0)
        analyze_menu.add_command(label='Analyze Selected File', command=self.analyze_csv_files)
        analyze_menu.add_command(label='Analyze All', command=self.analyze_all_csv_files)

        self.menu.add_cascade(label='Analyze', menu=analyze_menu)

        report_menu = Menu(self.menu, tearoff=0)
        report_menu.add_command(label='Generate Report', command=self.generate_report_single)
        report_menu.add_command(label='Generate Report All', command=self.generate_report_all)

        self.menu.add_cascade(label='Report', menu=report_menu)

        self.master.config(menu=self.menu)

    def config_frame(self):
        # Configure the main frame layout
        self.left_frame_top = Frame(self.master, highlightbackground="grey", highlightthickness=1, bg='whitesmoke',
                                    width=400, height=400,
                                    relief='raised')
        self.left_frame_bottom = Frame(self.master, highlightbackground="grey", highlightthickness=1, bg='whitesmoke',
                                       width=400, height=400,
                                       relief='groove')
        self.right_frame_root = Frame(self.master, highlightbackground="grey", highlightthickness=1, bg='white',
                                      width=880, height=800)

        self.left_frame_top.grid(row=0, column=0, sticky='nsew')
        self.left_frame_bottom.grid(row=1, column=0, sticky='nsew')
        self.right_frame_root.grid(row=0, column=1, rowspan=2, sticky='nsew')

        self.master.grid_rowconfigure(0, weight=1)  # Make the first row expandable
        self.master.grid_rowconfigure(1, weight=1)  # Make the second row expandable
        self.master.grid_columnconfigure(1, weight=1)  # Make the second column expandable

    def top_left_frame(self):
        # Create UI components for displaying file names
        label = Label(self.left_frame_top, text="File Names")
        label.grid(row=0, column=0, sticky='w')

        # Create a custom style for the listbox
        style = ttk.Style()
        style.configure("CustomListbox.TListbox", background="white", foreground="black", font=('Arial', 8))

        self.filename_listbox = Listbox(self.left_frame_top, width=30, height=30)
        self.filename_listbox.grid(row=1, column=0, sticky='nsew')

        self.filename_listbox.configure(bg=style.lookup("CustomListbox.TLabel", "background"),
                                        fg=style.lookup("CustomListbox.TLabel", "foreground"),
                                        font=style.lookup("CustomListbox.TLabel", "font"))

        # Add vertical scrollbar to the self.listbox
        scrollbar_y = Scrollbar(self.left_frame_top, orient=VERTICAL)
        scrollbar_y.grid(row=1, column=1, sticky='ns')
        self.filename_listbox.config(yscrollcommand=scrollbar_y.set)
        scrollbar_y.config(command=self.filename_listbox.yview)

        self.filename_listbox.bind("<<ListboxSelect>>", self.on_listbox_select)

        # Add horizontal scrollbar to the self.listbox
        scrollbar_x = Scrollbar(self.left_frame_top, orient=HORIZONTAL)
        scrollbar_x.grid(row=2, column=0, sticky='ew')
        self.filename_listbox.config(xscrollcommand=scrollbar_x.set)
        scrollbar_x.config(command=self.filename_listbox.xview)
        self.left_frame_top.grid_rowconfigure(1, weight=1)  # Make the second row expandable
        self.left_frame_top.grid_columnconfigure(0, weight=1)  # Make the first column expandable

    def bottom_left_frame(self):
        # Create UI components for displaying column names
        label = Label(self.left_frame_bottom, text="Columns")
        label.grid(row=0, column=0, sticky='w')

        # Create a custom style for the listbox
        style = ttk.Style()
        style.configure("CustomListbox.TListbox", background="white", foreground="black", font=('Arial', 8))

        self.header_listbox = Listbox(self.left_frame_bottom, width=30, height=20)
        self.header_listbox.grid(row=1, column=0, sticky='nsew')

        self.header_listbox.configure(bg=style.lookup("CustomListbox.TLabel", "background"),
                                      fg=style.lookup("CustomListbox.TLabel", "foreground"),
                                      font=style.lookup("CustomListbox.TLabel", "font"))

        # Add vertical scrollbar to the self.listbox
        scrollbar_y = Scrollbar(self.left_frame_bottom, orient=VERTICAL)
        scrollbar_y.grid(row=1, column=1, sticky='ns')
        self.header_listbox.config(yscrollcommand=scrollbar_y.set)
        scrollbar_y.config(command=self.header_listbox.yview)

        # Add horizontal scrollbar to the self.listbox
        scrollbar_x = Scrollbar(self.left_frame_bottom, orient=HORIZONTAL)
        scrollbar_x.grid(row=2, column=0, sticky='ew')
        self.header_listbox.config(xscrollcommand=scrollbar_x.set)
        scrollbar_x.config(command=self.header_listbox.xview)

        self.left_frame_bottom.grid_rowconfigure(1, weight=1)  # Make the second row expandable
        self.left_frame_bottom.grid_columnconfigure(0, weight=1)  # Make the first column expandable

    def right_frame(self):
        # Create the right frame with tabs and various components
        self.notebook = ttk.Notebook(self.right_frame_root)
        self.notebook.pack(fill=BOTH, expand=True)

        # Create tabs
        self.tab_dataframe = Frame(self.notebook)
        self.tab_statistics = Frame(self.notebook)
        self.tab_grapher = Frame(self.notebook)

        # Add tabs to the self.notebook
        self.notebook.add(self.tab_dataframe, text="DataFrame")
        self.notebook.add(self.tab_statistics, text="Statistics")
        self.notebook.add(self.tab_grapher, text="Grapher")

        style = ttk.Style()
        style.configure("TNotebook.Tab", padding=(10, 5), font=('Arial', 8))
        style.map("TNotebook.Tab", background=[("selected", "lightblue")])

        # Data Frame Tab
        self.data_list_tree_view = ttk.Treeview(self.tab_dataframe)

        style = ttk.Style()
        style.configure("Custom.Treeview", background="white", foreground="black", fieldbackground="white")

        self.data_list_tree_view.configure(style="Custom.Treeview")

        v_scrollbar = ttk.Scrollbar(self.tab_dataframe, orient='vertical', command=self.data_list_tree_view.yview)
        self.data_list_tree_view.configure(yscrollcommand=v_scrollbar.set)
        v_scrollbar.pack(side="right", fill="y")

        h_scrollbar = ttk.Scrollbar(self.tab_dataframe, orient='horizontal', command=self.data_list_tree_view.xview)
        self.data_list_tree_view.configure(xscrollcommand=h_scrollbar.set)
        h_scrollbar.pack(side="bottom", fill="x")

        self.data_list_tree_view.pack(side=TOP, fill=BOTH, expand=True)

        # Status Message Text
        self.status_text = Entry(self.right_frame_root, state="disabled", bg="white")
        self.status_text.pack(side=BOTTOM, fill=X)

        self.set_status_message("Files->Import csv file - To import csv files")

    def read_csv_files(self):
        # Read CSV files and update UI elements accordingly
        self.set_status_message("Reading csv files.....")
        self.filename_listbox.delete(0, END)
        self.header_listbox.delete(0, END)
        self.df_list, self.csv_paths, self.columns = self.read_mult_csv()

        for file_name in self.csv_paths:
            self.filename_listbox.insert(END, (os.path.basename(file_name)))

        for n in range(len(self.columns)):
            self.header_listbox.insert(END, self.columns[n])

        self.set_status_message("Completed")

    def on_listbox_select(self, event):
        # Handle selection in the file listbox
        if self.filename_listbox.curselection():
            self.selected_item = self.filename_listbox.get(self.filename_listbox.curselection())
            self.selected_index = self.filename_listbox.curselection()[0]

            self.data_list_tree_view['show'] = 'headings'
            self.data_list_tree_view["columns"] = list(range(len(self.columns)))
            self.data_list_tree_view.delete(*self.data_list_tree_view.get_children())

            for n in range(len(self.columns)):
                self.data_list_tree_view.heading(n, text=self.columns[n])
                self.data_list_tree_view.column(n, stretch=True)

            for index, row in self.df_list[self.selected_index].iterrows():
                self.data_list_tree_view.insert("", END, values=list(row))

            self.set_status_message(f"Data Frame of {self.selected_item} selected")

    def analyze_csv_files(self):
        # Analyze the selected CSV file
        if self.filename_listbox.curselection():
            self.pass_data_for_analysis(self.df_list, self.csv_paths, self.columns)
            self.analyze_single_csv(self.selected_index)
            self.set_status_message(f"Data Analysis of {self.selected_item} done")
        else:
            self.set_status_message(f"Please select a csv file from the list")

    def analyze_all_csv_files(self):
        # Analyze all CSV files
        self.pass_data_for_analysis(self.df_list, self.csv_paths, self.columns)
        self.analyze_data_all()
        self.set_status_message(f"Data Analysis done")

    def generate_report_single(self):
        # Generate a report for the selected CSV file
        if self.filename_listbox.curselection():
            self.generate_report(self.df_list[self.selected_index], self.csv_paths[self.selected_index], self.columns)
        else:
            self.set_status_message(f"Please select a csv file from the list")

    def generate_report_all(self):
        # Generate reports for all CSV files
        for n in range(len(self.df_list)):
            self.generate_report(self.df_list[n], self.csv_paths[n], self.columns)
