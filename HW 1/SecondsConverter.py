# Program for converting seconds into days, hours, minutes and seconds


# SecondsConverter methods takes in the number of seconds from the user
def seconds_converter():
    seconds = int(input('Enter Seconds: '))
    days = int(seconds / 86400)                       # calculates the number of days in the given seconds
    remaining_seconds = seconds % 86400
    hours = int(remaining_seconds/3600)               # calculates the number of hours in the given seconds
    remaining_seconds = remaining_seconds % 3600
    minutes = int(remaining_seconds/60)               # calculates the number of minutes in the given seconds
    remaining_seconds = remaining_seconds % 60        # calculates the number of remaining seconds

    # Prints out the days, hours, minutes and seconds from the seconds input
    if days >= 1:
        print('{} Days {} Hours {} Minutes {} Seconds'.format(days, hours, minutes, remaining_seconds))
    elif hours >= 1:
        print('{} Hours {} Minutes {} Seconds'.format(hours, minutes, remaining_seconds))
    elif minutes >= 1:
        print('{} Minutes {} Seconds'.format(minutes, remaining_seconds))
    else:
        print('{} Seconds'.format(remaining_seconds))


seconds_converter()

