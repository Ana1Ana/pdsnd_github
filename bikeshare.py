import time
import pandas as pd
import numpy as np
import datetime as dt
import calendar

#create library with city data

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
    print('Hello!! Let\'s explore some US bikeshare data!!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input("Let's choose a city! Would you like to see data for Chicago, New York City or Washington?: ").lower()
        if city == "chicago" or city == "ch" or city == "chi" or city== "c":
            print ("You chose Chicago!\n")
            city = "chicago"
        if city == "new york city" or city == "new york" or city == "nyc" or city == "ny":
            print ("You chose New York!\n")
            city = "new york city"
        if city == "washington" or city == "wa" or city == "wash" or city=="w":
            city = "washington"
            print ("You chose Washington!\n")
        if city not in CITY_DATA:
            print("Please choose again!\n")
            continue
        city = CITY_DATA[city]
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    print("Let's filter the data!\n")

    while True:
          data_filter = input("Would you like to filter data by month or day of the week or both?(month, day or both) \n").lower()
          month = 'all'
          day = 'all'
          if data_filter == "month" or data_filter == "m" or data_filter == 'mon':
              print("We will filter by month!\n")
              month = input("Which month would you like to look at? (January to June or all): ").lower()
              print('We will filter by month and see data for {}.\n'.format(month))
              if month not in ['january', 'february', 'march', 'april', 'may', 'june','all']:
                  print("Please choose a month between January and June.\n")
                  continue
              month=month
          elif data_filter == "day" or data_filter == 'd':
              print("We will filter by day of the week!\n")
              day = input("Which day of the week would you like to see? (Monday to Sunday or all): ").lower()
              print('We will filter by day of the week and we will see data for {}.\n'.format(day))
              if day not in ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']:
                  print("Please choose again.\n")
                  continue
              day=day
          elif data_filter == "both" or data_filter == "b":
              print("We will filter by month and day of the week!\n")
              month = input("which month would you like to see? (January to June or all): ").lower()
              if month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
                  print("Please choose a month between January and June.\n")
                  continue
              month = month
              day = input("Which day of the week would you like to see?(Monday to Sunday or all): ").lower()
              if day not in ['sunday','monday','tuesday','wednesday','thursday','friday','saturday', 'all']:
                  print("Please choose again.\n")
                  continue
              day = day
          else:
              print("Please choose again!\n")
              continue
          break
    print("We will read data from {}, and filter by {}.\n".format(city, data_filter))
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
    print("Loading...\n")
    df = pd.read_csv(city)

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    #https://stackoverflow.com/questions/37625334/python-pandas-convert-month-int-to-month-name
    #https://docs.python.org/2/library/calendar.html
    print('\n****Calculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df["Start Time"])
    df['day_of_week'] = pd.to_datetime(df['Start Time'].dt.dayofweek)
    df['month'] = pd.to_datetime(df['Start Time'].dt.month, format='%m').dt.month_name()

    #display total amount of trips
    total_trips = df['Start Time'].count()
    print("On the chosen period there were {} trips.".format(total_trips))

    # TO DO: display the most common month
    most_comon_month = df['month'].mode()[0]
    print('The most popular month for travel is {}.'.format(most_comon_month))
    # TO DO: display the most common day of week

    most_comon_day = df['day_of_week'].mode()[0].day_name()
    print('The most popular day for travel is {}.'.format(most_comon_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_comon_hour = df['hour'].mode()[0]
    print('The most common Start time for trips is {} o\'clock.'.format(most_comon_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n****Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    comon_start_station = df['Start Station'].mode()[0]
    print('The most popular start station is {}.'.format(comon_start_station))

    # TO DO: display most commonly used end station
    comon_end_station = df['End Station'].mode()[0]
    print('The most popular end station is {}.'.format(comon_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    df['trip_combination'] = df['Start Station'] + " -> " + df['End Station']
    most_frq_trip = df['trip_combination'].mode()[0]
    print('The most popular trip combination is {}.'.format(most_frq_trip))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\n****Calculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    #https://www.w3schools.com/python/numpy_ufunc_rounding_decimals.asp

    travel_time = np.round(sum(df['Trip Duration'])/3600,2)
    print('The total travel time was {} hours.'.format(travel_time))
    # TO DO: display mean travel time

    mean_travel_time = np.around(np.mean(df['Trip Duration'])/60,2)
    print('The average travel time was {} minutes.'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\n****Calculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print('The user types are the following:\n',user_types)

    # TO DO: Display counts of gender
    #https://stackoverflow.com/questions/26266362/how-to-count-the-nan-values-in-a-column-in-pandas-dataframe
    print('\n****Calculating gender data...\n')
    if 'Gender' in df:
        genders = df['Gender'].value_counts()
        print("The user gender distribution is the following:\n",genders)
        count_nan = len(df['Gender']) - df['Gender'].count()
        print ('\n{} users haven\'t added their gender.'.format(count_nan))
    else:
        print('Sorry! There is no gender data available for Washington.')
    # TO DO: Display earliest, most recent, and most common year of birth
    print ('\n****Let\'s look at the user birthdays...\n')
    if 'Birth Year' in df:
        birth_year = df['Birth Year']
        print('The oldest user was born in {}.'.format(int(min(birth_year))))
        print('The youngest user was born in {}.'.format(int(max(birth_year))))
        print('The most common year of birth is {}.'.format(int(np.mean(birth_year))))
        count_nan_birth = len(df['Birth Year']) - df['Birth Year'].count()
        print ('{} users haven\'t added their birth year.'.format(count_nan_birth))
    else:
        print('Sorry! There is no birth year data available for Washington.')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    print('\nLet\'s see some raw data!')
    #https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html
    raw = input('Would you like to see 5 rows of raw data?\n').lower()
    if raw != 'no':
        rows = 0
        while True:
            print(df.iloc[rows:rows+5])
            rows += 5
            extra_data = input('Would you like to see 5 more rows? yes or no.\n').lower()
            if extra_data not in ('yes','y'):
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
