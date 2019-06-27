"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module3_day33_pdf.py
    Creation Date:  6/27/2019, 10:25 AM
    Description:    Python Automation Program 5: PDF Manipulations
"""

# The `tabula` package is used to read tables from a PDF and allows the program to interact with the data. The output is
# stored as a dataframe which allows the use of functions like `.to_csv`. The resulting csv is not a clean
# representation of the data. Therefore, the file can be read and transformed to eliminate null columns and multi-row
# headers. While the `tabula` package provides the opportunity to extract data from a PDF, the output needs to be
# investigated and cleaned before it can be turned into a usable data product.
from tabula import read_pdf
import csv
import os

# The `read_pdf()` function stores the contents of the file as a dataframe in a list object. There are methods of
# cleaning the data without needing to write the data in the current format to a csv, but it is the easiest method based
# on the functions already discussed to this point in the course. Therefore, a temporary csv is created to store the
# uncleaned data.
census = read_pdf("MontcoCensus.pdf")
census.to_csv("census_temp.csv", mode="w", sep="|", index=False)

csv.register_dialect("pipe-delim", delimiter="|", lineterminator="\n")

# Since only the age and census numbers are needed, the program writes the new header and then bypasses the old header
# through the use of an `if` statement. The required data from the four rows are then written to the file. The resulting
# csv is in the proper format and the data can then be used for future analyses.
with open("census_temp.csv", "rt") as census_in, open("census_20100401.csv", "wt") as census_out:
    writer = csv.writer(census_out, delimiter="|", lineterminator="\n")
    writer.writerow(("age", "both_sexes", "male", "female"))
    for row in csv.reader(census_in, dialect="pipe-delim"):
        if row[0] == "Unnamed: 0" or row[0] == "":
            continue
        else:
            writer.writerow([row[0], row[2], row[3], row[4]])

# Once the temporary file is no longer needed, it can be removed.
os.remove("census_temp.csv")
