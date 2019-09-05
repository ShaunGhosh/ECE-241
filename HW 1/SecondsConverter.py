def SecondsConverter(seconds):
    NumberOfDays = int(seconds / 86400)
    remainingSeconds = seconds % 86400
    NumberOfHours = int(remainingSeconds/3600)
    remainingSeconds = remainingSeconds % 3600
    NumberOfMinutes = int(remainingSeconds/60)
    remainingSeconds = remainingSeconds % 60

    if NumberOfDays >=1:
        print('{} Days {} Hours {} Minutes {} Seconds'.format(NumberOfDays, NumberOfHours, NumberOfMinutes, remainingSeconds))
    elif NumberOfHours >= 1:
        print('{} Hours {} Minutes {} Seconds'.format(NumberOfHours, NumberOfMinutes, remainingSeconds))
    elif NumberOfMinutes >= 1:
        print('{} Minutes {} Seconds'.format(NumberOfMinutes, remainingSeconds))
    else:
        print('{} Seconds'.format(remainingSeconds))




days = SecondsConverter(3500000)