import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

months = ['january', 'february', 'march', 'april', 'may', 'june']

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

name = input("Hey there! What is your name?\n")
print("\nHi", name, "... are you ready to explore some data?\n")
sure_question = input("Yes/no: ").lower()
if sure_question != "yes":
    print("No worries", name, "...see you next time!")
    exit()
else:
    print("\nGreat! Let's get started!\n")


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    city_name = ''
    while city_name.lower() not in CITY_DATA:
        print("Ok,", name, "which city would you like to explore?")
        city_name = input("Chicago, New York City, or Washington:  ")
        if city_name.lower() in CITY_DATA:
            # We were able to get the name of the city to analyze data.
            city = CITY_DATA[city_name.lower()]
        else:
            # We were not able to get the name of the city to analyze data so we continue the loop.
            print("Sorry we didn't quite catch that! Please enter chicago, new york city or washington.\n")

    # get user input for month (all, january, february, ... , june)
    while True:
        print("\nPerfect!\n")
        month = input(
            "\nNow which month would you like to display?\n\nJanuary February, March,\nApril, May, June, or type 'all' to display them all:  ").lower()
        if month != "all" and month not in months:
            print("Sorry! Please try and enter one of the months listed previously!")
        else:
            break
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        print("\nGreat! " + name + ", which day  would you like to see?\n\nMonday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday\n- or type 'all' to display every day):  ")

        day = input().lower()
        print("\nDid you want to see", day.title(), "?")
        confirming = input("Yes/no? ").lower()
        if confirming == "yes":
            print("\nGreat!")
            break
        else:
            print("No worries!")

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
# loading data for cities
    df = pd.read_csv(city)

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name

    df['hour'] = df['Start Time'].dt.hour

# filtering by month
    if month != 'all':
        month = months.index(month)+1
        df = df[df['month'] == month]

# filtering by day
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    mo_com_month = df['month'].mode()[0]
    print('The most common month is: {}'.format(mo_com_month))

    # TO DO: display the most common day of week
    mo_com_day = df['day_of_week'].mode()[0]
    print('The most common day of the week is: {}'.format(mo_com_day))

    # TO DO: display the most common start hour
    mo_com_hour = df['hour'].mode()[0]
    print('The most common start hour is: {}'.format(mo_com_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('The most common start station is: ' + common_start)

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('The most common end station is: ' + common_end)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combo_stations = (df['Start Station'] + '-' + df['End Station']).mode()[0]
    print('The most frequent combination of start and end station are: ' + str(frequent_combo_stations))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_tt = df['Trip Duration'].sum()
    minute, second = divmod(total_tt, 60)
    hour, minute = divmod(minute, 60)
    print("The total travel time is: {} hours, {} minutes and {} seconds.".format(hour, minute, second))

    # TO DO: display mean travel time
    mean_tt = df['Trip Duration'].mean()
    print("The average travel time is: " + str(mean_tt))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User Type in this Data is: {}".format(user_types))

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print("Counts of Gender for this is: {}".fortmat(gender))
    except:
        print("\nGender not found in this column.")

   # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year_birth = int(df['Birth Year'].min())
        print("The person with the earliest birth year: {}".format(earliest_year_birth))
        recent_year_birth = int(df['Birth Year'].max())
        print("The person who is the youngest is: {}".format(recent_year_birth))
        common_year_birth = int(df['Birth Year'].mode()[0])
        print("The most common year people were born in is: {}".format(common_year_birth))
    except:
        print("Birth year unavailable.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # The total users are counted using value_counts method
    # They are then displayed by their types (e.g. Subscriber or Customer)
    user_type = df['User Type'].value_counts()

    print(f"The types of users by number are given below:\n\n{user_type}")

    # This try clause is implemented to display the numebr of users by Gender
    # However, not every df may have the Gender column, hence this...
    try:
        gender = df['Gender'].value_counts()
        print(f"\nThe types of users by gender are given below:\n\n{gender}")
    except:
        print("\nThere is no 'Gender' column in this file.")

    # Similarly, this try clause is there to ensure only df containing
    # 'Birth Year' column are displayed
    # The earliest birth year, most recent birth year and the most common
    # birth years are displayed
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print(
            f"\nThe earliest year of birth: {earliest}\n\nThe most recent year of birth: {recent}\n\nThe most common year of birth: {common_year}")
    except:
        print("There are no birth year details in this file.")


def display_data(df):
    count = 0
    response_field = ['yes', 'no']
    input_response = ''

    while input_response not in response_field:
        print("Would you like to see the first five rows?")
        input_response = input().lower()
        if input_response == 'yes':
            print(df.head())
        elif input_response not in response_field:
            print("It looks like that response isn't in our database. Plese try again.")

    while input_response == 'yes':
        print(name, "Would you like to see the next five rows of data?")
        count += 5
        input_response = input().lower()
        # If user opts for it, this displays next 5 rows of data
        if input_response == "yes":
            print(df[count:count+5])
        else:
            print('-'*40)
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
