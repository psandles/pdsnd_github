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
    print('-'*80)
    print("\nHello! \n\nLet's explore some US bikeshare data!\n")
    print('-'*80)
    print('\nUSER INPUT\n')   
    # Gets user input for city (chicago, new york city, washington).
    while True:
        city = str(input("Please enter a city from Chicago, New York City and Washington: ")).lower()
        if city == "chicago" or city == "new york city" or city == "washington":
            break
        else:
            print("  I'm sorry. You didn't enter one of the cities we have data for.\n")
    print("  Great. We'll use data for {} to calcuate various statistics.\n\n".format(city.title()))

    
    # Gets user input for month (january, ... , june or all)
    while True:
        month = str(input("Please enter a month or, alternatively, enter all to view statistics for all months: ")).lower()
        if month == "january" or "february" or "march" or "april" or "may" or "june" or "all":
            break
        else:
            print("  I'm sorry. You didn't give a valid input.\n")
    if month == "january" or "february" or "march" or "april" or "may" or "june":
        print("  Thanks. We'll just focus on statistics for {}.\n\n".format(month.title()))
    else:
        print("  Thanks. We'll look at statistics for all months.\n\n")
        
         
    # Gets user input for day of week (monday, ... sunday or all)
    while True:
        day = str(input("Please enter a day or, alternatively, enter all to view statistics for all days: ")).lower()
        if day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday" or day == "saturday" or day == "sunday" or day == "all":
            break
        else:
            print("  I'm sorry. You didn't give a valid input.\n")
    if day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday" or day == "saturday" or day == "sunday":
        print("  You've chosen to view statistics just for a {}.\n\n".format(day.title()))
    else:
        print("  You've chosen to view statistics for every day of the week.\n\n")            
            
    print('-'*80)
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
    # Creates Pandas DataFrame for selected city
    city_file = city.replace(" ", "_") + ".csv"
    df = pd.read_csv(city_file)

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.weekday
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']

    
    # Converts month to month_filter, a number between 1 and 6 (if applicable)
    if month != "all":
        if month == "january":
            month = 1
            df = df[df['month'] == month]
        elif month == "february":
            month = 2
            df = df[df['month'] == month]
        elif month == "march":
            month = 3
            df = df[df['month'] == month]
        elif month == "april":
            month = 4
            df = df[df['month'] == month]
        elif month == "may":
            month = 5
            df = df[df['month'] == month]
        else:
            month = 6
            df = df[df['month'] == month]
         
    # Converts day to a number between 0 (Monday) and 6 (Sunday) (if applicable)
    if day != "all":
        if day == "monday":
            day = 0
            df = df[df['weekday'] == day]
        elif day == "tuesday":
            day = 1
            df = df[df['weekday'] == day]
        elif day == "wednesday":
            day = 2
            df = df[df['weekday'] == day]
        elif day == "thursday":
            day = 3
            df = df[df['weekday'] == day]
        elif day == "friday":
            day = 4
            df = df[df['weekday'] == day]
        elif day == "saturday":
            day = 5
            df = df[df['weekday'] == day]
        else:
            day = 6 
            df = df[df['weekday'] == day]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nOVERVIEW STATISTICS\n')
    start_time = time.time()

    # Displays the most common month
    most_popular_month = df['month'].mode()[0]
    if most_popular_month == 1:
        most_popular_month_name = "January"
    elif most_popular_month == 2:
        most_popular_month_name = "February"
    elif most_popular_month == 3:
        most_popular_month_name = "March"
    elif most_popular_month == 4:
        most_popular_month_name = "April"
    elif most_popular_month == 5:
        most_popular_month_name = "May"
    else:
        most_popular_month_name = "June"
    
    mpm_df = df[df['month'] == most_popular_month]
    most_popular_month_count = mpm_df['month'].count()
    
    print("  {} was the most popular month for travelling during which {} journeys were made.".format(most_popular_month_name, most_popular_month_count))
      
    # Display the most common day of week
    most_popular_weekday = df['weekday'].mode()[0]
    if most_popular_weekday == 0:
        most_popular_weekday_name = "Monday"
    elif most_popular_weekday == 1:
        most_popular_weekday_name = "Tuesday"
    elif most_popular_weekday == 2:
        most_popular_weekday_name = "Wednesday"
    elif most_popular_weekday == 3:
        most_popular_weekday_name = "Thursday"
    elif most_popular_weekday == 4:
        most_popular_weekday_name = "Friday"
    elif most_popular_weekday == 5:
        most_popular_weekday_name = "Saturday"
    else:
        most_popular_weekday_name = "Sunday"

    mpw_df = df[df['weekday'] == most_popular_weekday]
    most_popular_weekday_count = mpw_df['weekday'].count()
        
    print("  {} was the most popular weekday for travelling and a total of {} journeys were made on this day.".format(most_popular_weekday_name, most_popular_weekday_count))

    # Display the most common start hour
    start_popular_hour = df['hour'].mode()[0]
    end_popular_hour = start_popular_hour + 1

    mph_df = df[df['hour'] == start_popular_hour]
    most_popular_hour_count = mph_df['hour'].count()
    
    print("  The most popular hour for journeys to start was between {}:00 and {}:00 during which {} journeys began.".format(start_popular_hour, end_popular_hour, most_popular_hour_count))

    print("\n\n\nSection performance statistics: ")
    print("   These statistics took %s seconds to calculate." % (time.time() - start_time))
    print('-'*80)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nSTATION STATISTICS\n')
    start_time = time.time()

    # Display most commonly used start station
    most_popular_start = df['Start Station'].mode()[0]
    print("  {} was the most popular station for starting travelling.".format(most_popular_start))

    # Display most commonly used end station
    most_popular_end = df['End Station'].mode()[0]
    print("  The station most commonly used to end a journey was {}.".format(most_popular_end))

    # Display most frequent combination of start station and end station trip
    most_popular_combination = df['combination'].mode()[0]
    combination_df = df[df['combination'] == most_popular_combination]
    combination_count = combination_df['combination'].count()
    print("  The most popular combination was {} which was used {} times.".format(most_popular_combination, combination_count))
    
    print("\n\n\nSection performance statistics: ")
    print("   These statistics took %s seconds to calculate." % (time.time() - start_time))
    print('-'*80)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nTRAVEL TIME STATISTICS\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("  The total travel time for the parameters you input was {} seconds.".format(total_travel_time))

    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("  The mean travel time for the parameters you input was {} seconds.".format(mean_travel_time))
    
    print("\n\n\nSection performance statistics: ")
    print("   These statistics took %s seconds to calculate." % (time.time() - start_time))
    print('-'*80)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nUSER STATISTICS\n')
    start_time = time.time()

    # Display counts of user types    
    subscriber_df = df[df['User Type'] == "Subscriber"]
    subscriber_count = subscriber_df['User Type'].count()
    customer_df = df[df['User Type'] == "Customer"]
    customer_count = customer_df['User Type'].count()
    dependent_df = df[df['User Type'] == "Dependent"]
    dependent_count = dependent_df['User Type'].count()
    if subscriber_count == 0:
        print("  There were no subscriber users in the period specified.")
    elif subscriber_count == 1:
        print("  There was 1 user who was a subscriber in the period specified.")
    else:
        print("  There were {} users who were subscribers in the period specified.".format(subscriber_count))
    if customer_count == 0:
        print("  There were no customer users in the period specified.")
    elif customer_count == 1:
         print("  There was 1 user who was a customer in the period specified.")
    else:
        print("  There were {} users who were customers in the period specified.".format(customer_count))
    if dependent_count == 0:
        print("  There were no dependent users in the period specified.")
    elif dependent_count == 1:
         print("  There was 1 user who was a dependent in the period specified.")    
    else:
        print("  There were {} users who were dependents in the period specified.".format(dependent_count))

    # Display counts of gender
    columns_present = df.columns
    gender_check = "Gender" in columns_present
    if gender_check == True:
        female_df = df[df['Gender'] == "Female"]
        female_count = female_df['Gender'].count()
        male_df = df[df['Gender'] == "Male"]
        male_count = male_df['Gender'].count()

        print("\n  The number of female users for the period was {} and the number of male users was {}.".format(female_count, male_count))

    # Display earliest, most recent, and most common year of birth
    birth_year_check = "Birth Year" in columns_present
    if birth_year_check == True:
        earliest_birth_year = (df['Birth Year'].min())
        print("\n  The earliest year of birth was {}.".format(int(earliest_birth_year)))
        most_recent_birth_year = (df['Birth Year'].max())
        print("  The youngest user was born in {}.".format(int(most_recent_birth_year)))
        mode_birth_year = (df['Birth Year'].mode())
        mode_birth_year = (int(mode_birth_year))
        print("  The most common year of birth was {}.".format(mode_birth_year))
    print("\n\n\nSection performance statistics: ")
    print("   These statistics took %s seconds to calculate." % (time.time() - start_time))
    print('-'*80)

def raw_data(df):
    """Displays raw data on bikeshare users."""

    # Handles user input and then loops to display raw data based on input
    print('\nRAW DATA')
    
    df = df.drop(['hour', 'month', 'weekday', 'combination'], axis = 1)
    count = 0
    extra_count = 5
    while True:    
        raw_data = str(input('\nWould you like to view raw journey data? Enter yes or no: ')).lower()
        print("  OK. Let's view raw data for results {} to {}.".format(count, extra_count))
        if raw_data == 'yes':
            print(df.iloc[[count]])
            print(df.iloc[[count+1]])
            print(df.iloc[[count+2]])
            print(df.iloc[[count+3]])
            print(df.iloc[[count+4]])
            count += 5
            extra_count += 5
        elif raw_data == 'no':
            break
        else:
            print("  I'm sorry. I didn't understand your input.\n")      

    print('-'*80) 
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        # Restart loop based on user input
        print('\nRESTART')            
        restart = input('\nWould you like to start this program again? Enter yes or no: ')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
    
    
    
    
