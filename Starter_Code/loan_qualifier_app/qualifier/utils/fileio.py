# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(csvpath, qualifying_loans):
    """Writes the CSV file to the path provided.

    Args:
        csvpath (Path): The csv file path.
        qualifying_loans: the list of loans for which user qualified.
        
    """     
    with open(csvpath, 'w', newline='') as saved_loans_file:
        csvwriter = csv.writer(saved_loans_file)

        # Add a header to the new CSV file
        header = ['Lender','Max Loan Amount','Max LTV','Max DTI','Min Credit Score','Interest Rate']
        csvwriter.writerow(header)
        # Write the CSV data
        for row in qualifying_loans:
            csvwriter.writerow(row)
    return saved_loans_file