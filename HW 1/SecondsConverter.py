# Program for converting seconds into days, hours, minutes and seconds


# SecondsConverter methods takes in the number of seconds from the user
def seconds_converter():
    seconds = int(input('Enter Seconds: '))
    days = int(seconds / 86400)
    remaining_seconds = seconds % 86400
    hours = int(remaining_seconds/3600)
    remaining_seconds = remaining_seconds % 3600
    minutes = int(remaining_seconds/60)
    remaining_seconds = remaining_seconds % 60

    if days >= 1:
        print('{} Days {} Hours {} Minutes {} Seconds'.format(days, hours, minutes, remaining_seconds))
    elif hours >= 1:
        print('{} Hours {} Minutes {} Seconds'.format(hours, minutes, remaining_seconds))
    elif minutes >= 1:
        print('{} Minutes {} Seconds'.format(minutes, remaining_seconds))
    else:
        print('{} Seconds'.format(remaining_seconds))


seconds_converter()

