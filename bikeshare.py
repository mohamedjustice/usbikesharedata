import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!\n')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = str(input('Please Enter The City you would like to Analyze: ')).lower() 
        if city not in CITY_DATA.keys():
            print('Pleae Enter a Valid City')
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:    
        month = str(input('Please Enter a month to filter by or "all" for no filter: ')).lower() 
        if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print('Pleae Enter a Valid Month (from January to June) or "all"')
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:    
        day = str(input('Please Enter a day of the week to filter by or "all" for no filter: ')).lower() 
        if day not in ('all', 'saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday'):
            print('Pleae Enter a Valid day')
            continue
        else:
            break


    print('-'*40)
    return city, month, day


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['dow'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['dow'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].value_counts().idxmax()
    print('The most common month is: ', common_month)

    # TO DO: display the most common day of week
    common_day = df['dow'].value_counts().idxmax()
    print('The most common day of the week is: ', common_day)

    # TO DO: display the most common start hour
    common_hour = df['hour'].value_counts().idxmax()
    print('The most common start hour is: ', common_hour)
    
    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print('The Most Commonly used start station is:', start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('The Most Commonly used end station is:', end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combination =  pd.DataFrame(df.groupby(['Start Station', 'End Station']).size().nlargest(1))
    print('The Most Commonly used combination of start station and end station trip are:\n', combination, sep = '')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('The Total travel time is:', round(total_travel_time/86400, 2), " Days")


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The Average travel time is:', round(mean_travel_time/60, 2), " Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types, sep = '')

    # TO DO: Display counts of gender
    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types, sep = '')
    except KeyError:
      print("\nGender Types:\nData is unavailable for the selected month.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:', Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nData is unavailable for the selected month.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('Most Recent Year:', Most_Recent_Year)
    except KeyError:
      print("Most Recent Year:\nData is unavailable for the selected month.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('Most Common Year:', Most_Common_Year)
    except KeyError:
      print("Most Common Year:\nData is unavailable for the selected month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    lines = 0
    while True :
        if lines == 0:
            view_data = str(input('Would you like to view 5 rows of individual trip data? Enter yes or no? ')).lower()
        else:
            view_data = str(input('Would you like to view the next 5 rows of individual trip data? Enter yes or no? ')).lower()
            
        if view_data == 'yes':
            print(df.iloc[lines:lines+5])
            lines += 5
        elif view_data == 'no':
            break
        else:
            print('Please enter either "yes" to view the raw data or "no" to exit')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = str(input('\nWould you like to restart? Enter yes or no.\n')).lower()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()