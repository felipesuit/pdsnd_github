import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }




#FIRST FUNCTION
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # INITIAL MESSAGE
    print('Hello! Let\'s explore some US bikeshare data!, \n What city do you want to explore? \n We have these 3 cities in our base: chicago, new york city, washington \n Please, write the city name correctly' )
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    # GET INPUT REQUESTED FROM USER, IF THE USER ENTERS THE VALUE IN CAPITAL LETTERS, CONVERT THEM IN LETTERS TO AVOID ERRORS
    city = input().lower()  
    
    while city not in CITY_DATA.keys() :
     # IF THE CITY NOT IN THE KEYS, SEND THE ERROR MESSAGE
        print("Please enter a valid city name")
      # REQUEST TO THE USER A VALID CITY NAME, IF THE USER ENTERS THE VALUE IN CAPITAL LETTERS, CONVERT THEM IN LETTERS TO AVOID ERRORS
        city = input().lower()
    #esto le agregue
    #print('\n Do you want to see the first 5 rows of city information? write yes or no') 
    #see_citydata = input().lower()
    #see_citydata_list = ['yes']
    #while see_citydata in see_citydata_list : 
    #df_city = pd.read_csv(CITY_DATA[city],index_col=0)  
    #df_city.head()
    
    
    

    # TO DO: get user input for month (all, january, february, ... , june)
    
    print('\n What month do you want to explore? \n The month can be:  january, february, march, april, may, june, all (to filter by every month in the list) \n Please, write the month name correctly')
    
    # GET INPUT REQUESTED FROM USER, IF THE USER ENTERS THE VALUE IN CAPITAL LETTERS, CONVERT THEM IN LETTERS TO AVOID ERRORS
    month = input().lower()
    
    # A LIST OF MONTHS WAS CREATED TO COMPARE WITH THE INPUT
    # THE LIST HAS UNTIL JUNE BECAUSE THE DATA HAS NO MORE MONTHS
    month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
   


    while month not in month_list :
         # IF THE MONTH NOT IN THE MONTH_LIST, SEND THE ERROR MESSAGE
        print("Please enter a valid month")
        
       # REQUEST TO THE USER A VALID MONTH, IF THE USER ENTERS THE VALUE IN CAPITAL LETTERS, CONVERT THEM IN LETTERS TO AVOID ERRORS
        month = input().lower()
        
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('\n What day of week do you want to explore? \n The day of week can be:  monday, tuesday, wednesday, thursday, friday, saturday, sunday, all (to filter by every day in the list) \n Please, write the day of week correctly')
    
    # GET INPUT REQUESTED FROM USER, IF THE USER ENTERS THE VALUE IN CAPITAL LETTERS, CONVERT THEM IN LETTERS TO AVOID ERRORS
    day = input().lower()
    # A LIST OF DAYS WAS CREATED TO COMPARE WITH THE INPUT
    day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
   


    while day not in day_list :
        # IF THE DAY NOT IN THE DAY_LIST, SEND THE ERROR MESSAGE
        print("please enter a valid day")
        
       # REQUEST TO THE USER A VALID DAY OF WEEK, IF THE USER ENTERS THE VALUE IN CAPITAL LETTERS, CONVERT THEM IN LETTERS TO AVOID ERRORS
        day = input().lower()
        
    

    print('-'*40)
    return city, month, day




# FUNCTION TO FILTER THE DATA BY THE INPUTS FROM THE USER

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
    # CREATE A DATAFRAME READING THE CORRECT FILE (CONCATENATING THE CITY WITH ".CSV")
    df = pd.read_csv(CITY_DATA[city],index_col=0) #FIRST COLUMN AS THE INDEX
    
    # CLEANNING DATA, DELETE ROWS WITH NaNs
    df.dropna(axis=0, inplace = True) # INPLACE IS USED TO MODIFY THE DATAFRAME
    
       
    # CONVERT "Start time" TO DATETIME FORMAT
    df['Start Time'] = pd.to_datetime(df['Start Time']) 
    # EXTRACT THE MONTH FROM START TIME
    df['month'] = df['Start Time'].dt.month
    # EXTRACT THE DAY FROM START TIME
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # CREATE A MONTH DICTIONARY FOR FILTER THE DATA BY MONTH
    month_dict = {"january":1, 'february':2, 'march':3, 'april':4, 'may':5, 'june':6}
    
    #IF IT IS MONTH IS DIFFERENT  FROM ALL, FILTER BY THE USER SELECTED MONTH
    if month !='all' :
        month_filter = df["month"] == month_dict[month]
        df = df.loc[month_filter]
    
    #IF IT IS DAY IS DIFFERENT  FROM ALL, FILTER BY THE USER SELECTED DAY
    if day !='all' :
        day_filter = df["day_of_week"] == day.title()
        df = df.loc[day_filter]
    
    # THIS IS FOR RESET THE INDEX AFTER DROPING NaN AND MAKING THE FILTERS
    df.reset_index(drop=True, inplace = True) 
    
    return df
    




# FUNCTION time_stats IS CREATED

def time_stats(df): 
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    # THIS IS FOR THE CALCULATION OF THE RUN TIME
    start_time = time.time()

    # TO DO: display the most common month
    
    most_common_month = df['month'].mode()[0]
    print ('The most common month is:',most_common_month )
    

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print ('The most common day of week is:',most_common_day)

    # TO DO: display the most common start hour
 
    # THE TIME IS EXTRACTED FROM "Start Time"
    df['hour'] =df['Start Time'].dt.hour
    
    most_common_hour = df['hour'].mode()[0]
    print ('la hora  mas popular es:',most_common_hour)
    
    # THIS IS FOR THE CALCULATION OF THE RUN TIME
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




# FUNCTION station_stats IS CREATED
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    # THIS IS FOR THE CALCULATION OF THE RUN TIME
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_used_start_station = df['Start Station'].mode()[0]
    print ('The most commonly used start station is: ',most_common_used_start_station)

    # TO DO: display most commonly used end station
    most_common_used_end_station = df['End Station'].mode()[0]
    print ('The most commonly used end station is: ',most_common_used_end_station)

    # TO DO: display most frequent combination of start station and end station trip

    # CALCULATED FIELD IS CREATED BY CONTAINING START STATION AND END STATION
    df['startstation-endstation'] = df['Start Station']+' - '+df['End Station']
    most_common_combination = df['startstation-endstation'].mode()[0]
    print ('The most requent combination of start station and end station trip is: ',most_common_combination)
    
    # THIS IS FOR THE CALCULATION OF THE RUN TIME
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




# FUNCTION trip_duration_stats IS CREATED
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    # THIS IS FOR THE CALCULATION OF THE RUN TIME
    start_time = time.time()

    # TO DO: display total travel time
    
    # THE TRIP DURATION IS ADDED TO HAVE THE TOTAL TRAVEL TIME
    total_travel_time = df['Trip Duration'].sum()
    print ('The display total travel time is: ',round(total_travel_time/8640, 1), ' days') # 1 DAY = 8640 SEGS
    
    
    # TO DO: display mean travel time
   
    # THE TRIP DURATION FIELD IS AVERAGE TO HAVE THE MEAN TRAVEL TIME
    mean_travel_time = df['Trip Duration'].mean()
    print ('The mean travel time is: ',round(mean_travel_time/60,1), ' minutes') # 1 MINUTE = 60 SEGS
    
    # THIS IS FOR THE CALCULATION OF THE RUN TIME
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




# FUNCTION user_stats IS CREATED
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    # THIS IS FOR THE CALCULATION OF THE RUN TIME
    start_time = time.time()

    # TO DO: Display counts of user types
    
    user_types = df['User Type'].value_counts()
    print('The counts of user types are: \n\n',user_types, '\n')
    
    
    # TO DO: Display counts of gender
    
    # IF THE CITY CONSULTED DOES NOT HAVE A GENDER FIELD, THEN SEND A MESSAGE THAT IT DOES NOT HAVE
    try:
        user_gender = df['Gender'].value_counts()
        print('The counts by every gender are: \n',user_gender,'\n')
    except:
        print("The requested data base does not have gender field")

    # TO DO: Display earliest, most recent, and most common year of birth
  
    # IF THE CITY CONSULTED DOES NOT HAVE A BIRTH YEAR FIELD, THEN SEND A MESSAGE THAT IT DOES NOT HAVE
    try:
        user_earliestbirthyear = df['Birth Year'].min() 
        print('The earliest birth year is: \n',int(user_earliestbirthyear),'\n')
        user_mostrecentbirthyear = df['Birth Year'].max()
        print('The most recent birth year is: \n',int(user_mostrecentbirthyear),'\n')
        user_mostcommonbirthyear = df['Birth Year'].mode()[0]
        print('The most recent birth year is: \n',int(user_mostcommonbirthyear),'\n')
        
    except:
        print("The requested data base does not have Birth Year field")
    
    
    
    # THIS IS FOR THE CALCULATION OF THE RUN TIME
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # DEFINING VARIABLE end = 10
        end  = 10
                  
        # ASK USER IF HE WANTS TO SEE THE FIRST 10 ROWS OF DATA
        View_Rows = input('Do you want to see the first 10 rows of raw data? type yes or no').lower()
        
        while View_Rows == 'yes':
            # IN CASE "end" IS GREATER THAN THE NUMBER OF ROWS, ASSIGN "end" AS THE NUMBER OF ROWS REMAINING FROM THE DATAFRAME
            if end > df.shape[0]:
                end = df.shape[0]
            # SHOW THE FIRST 10 ROWS BETWEEN "end" AND "end" - 10
            print(df.iloc[end-10:end]) 
            # MAKES A LINE TO BETTER VIEW THE REQUESTED DATA
            print('--'*40) 
            # MOVE THE SELECTION INDEX "end" TO SHOW THE FOLLOWING 10 ROWS IN CASE THE USER REQUESTS
            end = end + 10  
            # WITH THIS, THE VARIABLE View_Rows IS OVERWRITTEN
            View_Rows = input('Do you want to see the next 10 rows of raw data? type yes or no').lower()
            
            
            
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()







