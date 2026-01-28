# zimetrics-The-Sales-Data-Cleaner
A python ETL script that cleans messy sales CSV data, removes duplicates, converts USD to INR, and exports clean JSON reports. 

1. PROJECT TITLE: The Sales Data Cleaner
   PROJECT GOAL: To clean, transform, and convert raw sales CSV data into a structured JSON report using Python.

2. SETUP INSTRUCTIONS:
   Command to run the file is: python clean_sales.py in the terminal

3. THE LOGIC:
   First, from all the 10 tasks we have been given, I analyzed the second given problem and understood that sales data was in a messy CSV format with symbols, quotes     and duplicate entries. So I divided the problem into small steps like reading the file, cleaning data, converting values, removing duplicates and saving to JSON       format. Thus it became easier to implement.
   I chose this approach because Python's built in CSV and JSON modules make data processing simple and efficient. This method follows ETL i.e. Extract, Transform and    Load process, which is commonly used in real-world data projects.
   The hardest bug I faced was handling inconsistent data formats, especially removing dollar signs and quotes while converting prices to float.
   Initially, there were some errors. I fixed it by cleaning the data first by using replace() and strip() methods before converion processes.
   I also tested the script with multiple inputs to make sure it handled all cases correctly.

4. OUTPUT: For a output in terminal, I have added a simple print statement implying the successful completion of the script and creation of JSON file. I am hereby attaching the screenshot.
            <img width="1920" height="1080" alt="clean_sales" src="https://github.com/user-attachments/assets/c31c3957-bb77-49fa-9ca8-9670a587a9cd" />

5. FUTURE IMPROVEMENT: In few more days, this project can be enhanced by adding proper error handling for invalid input data, supporting more CSV files, and improving output formatting. Basic user input options can also be added to make our script more flexible and user-friendly.
