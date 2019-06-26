"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module3_day31_csv.py
    Creation Date:  6/26/2019, 8:15 AM
    Description:    Python Automation Program 3: CSV Manipulations
"""

import csv

actor = ["Alan Alda", "Loretta Swit", "Jaime Farr", "William Christopher", "Larry Linville", "Mike Farrell",
         "Gary Burghoff"]
character = ["Captain Benjamin Franklin 'Hawkeye' Pierce", "Major Margaret 'Hot Lips' Houlihan",
             "Corporal Maxwell Q Klinger", "Father Francis Mulcahy", "Major Frank Burns", "Captain B.J. Hunnicutt",
             "Corporal Walter 'Radar' O'Reilly"]
episodes = [251, 251, 216, 213, 121, 179, 177]

# The file needs to first be opened. The `wt` option will create or overwrite the file in the current working directory.
mash = open("mash.csv", "wt")

# Since this is the first time writing data, the `.writerow()` function is used to first add the header. Then, a loop
# is implemented to add the contents of the three lists into the proper place. Finally, the file is closed.
try:
    writer = csv.writer(mash)
    writer.writerow(("actor", "character", "episodes"))
    for i in range(len(actor)):
        writer.writerow((actor[i], character[i], episodes[i]))
finally:
    mash.close()

# When `mash.csv` is opened, there are extra newline characters included which turns the file double spaced. The
# function can be modified by changing the `lineterminator` option.
mash = open("mash.csv", "wt")
try:
    writer = csv.writer(mash, lineterminator="\n")
    writer.writerow(("actor", "character", "episodes"))
    for i in range(len(actor)):
        writer.writerow((actor[i], character[i], episodes[i]))
finally:
    mash.close()

# By using the append (`a`) option when opening the file, new entries can be added to an existing file. With the rest of
# the data, there were no instances of a comma used in the text strings. Therefore, these entries do not need to be
# encapsulated by quotation marks. However, if a string contains commas, python will automatically add the string in
# quotes when writing to a csv. Additionally, a csv is type agnostic; python will not prohibit a string from being added
# to a column containing integers.
mash = open("mash.csv", "at")
try:
    writer = csv.writer(mash, lineterminator="\n")
    writer.writerow(("This includes a, comma", "How will that affect, it?", "This normally contains integers"))
finally:
    mash.close()

# Like modifying the line terminator, the separator can also be modified based on needs. It is common to change the
# separator to a tab or a symbol that is not often used in text to avoid the automatic addition of quotes. A tab
# separated file is called a `.tsv` and can be created by simply changing the extension and the delimiter. In both the
# pipe delimited and tab delimited examples, all of the entries are written without the need of additional quotes.
mash = open("mash_pipe.csv", "wt")
try:
    writer = csv.writer(mash, delimiter="|", lineterminator="\n")
    writer.writerow(("actor", "character", "episodes"))
    for i in range(len(actor)):
        writer.writerow((actor[i], character[i], episodes[i]))
    writer.writerow(("This includes a, comma", "How will that affect, it?", "This normally contains integers"))
finally:
    mash.close()

mash = open("mash.tsv", "wt")
try:
    writer = csv.writer(mash, delimiter="\t", lineterminator="\n")
    writer.writerow(("actor", "character", "episodes"))
    for i in range(len(actor)):
        writer.writerow((actor[i], character[i], episodes[i]))
    writer.writerow(("This includes a, comma", "How will that affect, it?", "This normally contains integers"))
finally:
    mash.close()

# In order to read csv files with different delimiters, the `dialect` option must be implemented. If custom options were
# used to create the file, then the custom dialect must first be registered.
csv.register_dialect("pipe-delim", delimiter="|", lineterminator="\n")

# Data cannot be removed from the same file because the `wt` option truncates the file before it writes data.
# Additionally, the `at` option does not remove existing records and would only append additional items. Therefore, a
# secondary file is required to write the cleaned output. However, the `at` option could be leveraged along with the
# `rt` option on the same file to analyze if a record exists before adding it.
with open("mash_pipe.csv", "rt") as mash_in, open("mash.csv", "wt") as mash_out:
    writer = csv.writer(mash_out, lineterminator="\n")
    for row in csv.reader(mash_in, dialect="pipe-delim"):
        if row[0] == "This includes a, comma":
            continue
        else:
            writer.writerow(row)
