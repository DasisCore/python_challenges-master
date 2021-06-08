rain = input('It is raining now? : ')
rain = str.lower(rain)
if rain == "yes":
    wind = input('Is the wind blowing now? : ')
    wind = str.lower(wind)
    if wind == "yes":
        print('"It is too windy for an umbrella"')
    else:
        print('"Take an umbrella"')
else:
    print('"Enjoy your day"')
