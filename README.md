### Date created
2020-05-10

### Project Title
U.S. Bikeshare Data

### Description
This program provides bike sharing data for several U.S. cities. The user inputs the city, month and day to be analyzed. 

The program will return:
Most popular starting hour
Most popular start and end station
Most popular trip (from one station to another)
Total travel time
Mean travel time
User type (customer or subscriber)
User gender
Earliest age

It is also possible to browse through the raw data which generated the statistics.

### Files used
chicago.csv
new_york_city.csv
washington.csv

### Credits
I used this to clean up the input while loops
https://stackoverflow.com/questions/32151479/efficient-approach-for-multiple-or-statements-in-an-conditional-statement

Used because weekday_name was not working
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.day_name.html

I used this to search for pairs of column values
https://stackoverflow.com/questions/50310226/number-of-occurrence-of-pair-of-value-in-dataframe

Reminder to use to_string
https://stackoverflow.com/questions/29645153/remove-name-dtype-from-pandas-output

Reminder to use iloc
https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/#iloc-selection
