def SecondsConverter():
    seconds = int(input('Enter Seconds: '))
    numberofdays = int(seconds / 86400)
    remainingseconds = seconds % 86400
    numberofhours = int(remainingseconds/3600)
    remainingseconds = remainingseconds % 3600
    numberofminutes = int(remainingseconds/60)
    remainingseconds = remainingseconds % 60

    if numberofdays >= 1:
        print('{} Days {} Hours {} Minutes {} Seconds'.format(numberofdays, numberofhours, numberofminutes, remainingseconds))
    elif numberofhours >= 1:
        print('{} Hours {} Minutes {} Seconds'.format(numberofhours, numberofminutes, remainingseconds))
    elif numberofminutes >= 1:
        print('{} Minutes {} Seconds'.format(numberofminutes, remainingseconds))
    else:
        print('{} Seconds'.format(remainingseconds))


SecondsConverter()

