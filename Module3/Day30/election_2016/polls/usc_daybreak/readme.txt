Summary results files for the USC Dornsife/Los Angeles Times Daybreak Poll

The files posted here contain the data that are plotted in the graphs,
plus some additional information. The files all have the same structure:
- They are tab delimited text files
- The first row contains the variable names
- The remaining rows have results for one date each. (A "date" is the last
  day of a 7-day rolling window, so e.g., "07/10/2016" uses observations
  from 07/04/2016-07/10/2016.)
- The columns are: date (MM/DD/2016), N (sample size), Trump (%), Clinton (%),
  sediff (standard error of the Trump-Clinton difference), Lo, Up.
  Lo and Up are the lower and upper boundaries of the gray area that
  indicates the area of uncertainty in the graphs.

The file names are combinations of
- Result type:
  * pop - popular vote; predicted fraction of the votes that each
    candidate will get
  * win - (average) percentage chance that each candidate will win the
    election according to the respondents
  * int - intention to vote, by candidate preference
- Breakdown variable:
  * sex - gender (0=female, 1=male)
  * rac - race/ethnicity (1=White, 2=African-American, 3=other, 4=Hispanic)
  * age - age category (1=18-34, 2=35-64, 3=65+)
  * edu - education (1=High school or less, 2=Some college or associate's
    degree, 3=Bachelor's degree or more)
  * inc - family income (1=$0-34,999/year, 2=$35,000-74,999/year,
    3=$75,000 and more)
- Category of the breakdown variable (e.g., 0 = female)

win.csv, pop.csv, and int.csv have no (further) breakdowns.
The other files are of the form type_variable_category.csv and are part of a
breakdown. int.csv is already a breakdown and there are no further breakdowns
of intention to vote.


