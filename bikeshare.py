#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Available cities: Chicago, New York City or Washington\nPlease enter city to analyze: ').title()
    while city not in {'Chicago', 'New York City', 'Washington'}:
        city = input('Invalid entry, please try again.\nAvailable cities: Chicago, New York City or Washington\nPlease enter city to analyze: ').title()

    # Get user input for month (all, january, february, ... , june)
    month = input('Enter the name of a month (January-June) or all for every month. \nPlease enter month to analyze: ').title()
    while month not in {'January', 'February', 'March', 'April', 'May', 'June', 'All'}:
        month = input('Invalid entry, please try again.\nEnter the name of a month (January-June) or all for every month. \nPlease enter month to analyze: ').title()
        
    # Get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Enter a day of the week or all for every day. \nPlease enter day to analyze: ').title()
    while day not in {'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All'}:
        day = input('Invalid entry, please try again.\nEnter a day of the week or all for every day. \nPlease enter day to analyze: ').title()

    print('-'*40)
    return city, month, day


# In[2]:


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['month_name'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
   
    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


# In[3]:


def time_stats(df, city, month, day):
    """Displays statistics on the most frequent times of travel."""

    # customized the output to highlight the chosen analysis criteria
    if month != 'All' and day != 'All':
        print('\nCalculating The Most Frequent Times of Travel for {}s in {} in {}\n'.format(day, month, city))
    elif month != 'All':
        print('\nCalculating The Most Frequent Times of Travel for {} in {}\n'.format(month, city))
    elif day != 'All':
        print('\nCalculating The Most Frequent Times of Travel for {}s in {}\n'.format(day, city))
    else:
        print('\nCalculating The Most Frequent Times of Travel in {}\n'.format(city))
    
    start_time = time.time()

    # display the most common month when analysing all months
    if month == 'All':
        popular_month = df['month_name'].mode()[0]
        print('Most Popular Month: ', popular_month)

    # display the most common day of week when analysing all days
    if day == 'All':
        popular_day = df['day_of_week'].mode()[0]
        print('Most Popular Day of Week: ', popular_day)

    # display the most common start hour
    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[4]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most popular starting station: ', popular_start_station, '\n')

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most popular ending station: ', popular_end_station, '\n')

    # display most frequent combination of start station and end station trip
    popular_combination = pd.Series(list(zip(df['Start Station'], df['End Station']))).mode()[0]
    print('Most popular trip (from, to): ', popular_combination, '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[5]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: ', int(total_travel_time/3600), 'hours')

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time: ', int(mean_travel_time), 'seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[6]:


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    print('User type: ')
    # Display counts of user types
    # Print value counts for each user type
    user_types = df['User Type'].value_counts()
    print(user_types.to_string(), '\n')
    
    # Skip gender and birth year stats if Washington is selected
    if city != 'Washington':
    
        print('User gender: ')
        # Display counts of gender
        gender_count = df['Gender'].value_counts()
        print(gender_count.to_string(), '\n')

        print('User age: ')
        # Display earliest, most recent, and most common year of birth
        earliest_birthyear = int(df['Birth Year'].min())
        print('Earliest birth year: ', earliest_birthyear)

        latest_birthyear = int(df['Birth Year'].max())
        print('Most recent birth year: ', latest_birthyear)

        most_common_birthyear = int(df['Birth Year'].mode()[0])
        print('Most common birth year: ', most_common_birthyear)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[7]:


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, city, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        
        # Ask user if they want to see raw data, taking input errors into account, displaying 5 lines of raw data each time
        raw_data = input('\nWould you like to view the raw data? Enter yes or no.\n')
        start = 0
        stop = 5
        while raw_data.lower() != 'no' and raw_data.lower() != 'yes':
            raw_data = input('Invalid entry. Please enter yes or no.')
        while raw_data.lower() == 'yes':
            print(df.iloc[start:stop])
            start += 5
            stop += 5
            raw_data = input('\nWould you like to view more raw data? Enter yes or no.\n')
            while raw_data.lower() != 'no' and raw_data.lower() != 'yes':
                raw_data = input('Invalid entry. Please enter yes or no.')
        
        # Added input error logic to restart variable, now it matches the rest of the program
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        while restart.lower() != 'no' and restart.lower() != 'yes':
            restart = input('Invalid entry. Please enter yes or no.')
        if restart.lower() == 'no':
            break

if __name__ == "__main__":
	main()

