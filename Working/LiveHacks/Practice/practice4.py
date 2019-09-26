temperature = int(input("Enter the temperature (Celsius): "))
windspeed = int(input("Enter the wind speed (km/h): "))
print("The wind chill factor is:", end="")
print(13.12 + (0.6215 * temperature) - (11.37 * windspeed ** 0.16) + (0.3965 * temperature * windspeed ** 0.16))
