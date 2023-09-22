# Weather App

# prompt user for city and state or zip code
# request weather forecast from OpenWeatherMap
# print in a readable format
# APPID = "061b1d096c35c4becdf0adec17e79675"

# functions to get city
def weather_get_city_celsius():
    import requests

    # prompt user for city info
    user_city = str(input("Enter city name: "))
    user_state = str(input("State: "))
    user_country = str(input("Country: "))

    user_inputs = []
    if len(user_city) > 0:
        user_inputs.append(user_city)

    if len(user_state) > 0:
        user_inputs.append(user_state)

    if len(user_country) > 0:
        user_inputs.append(user_country)

    weather_string = ",".join(user_inputs)
    # print(user_inputs)

    api_key = "061b1d096c35c4becdf0adec17e79675"
    weather_url = "http://api.openweathermap.org/geo/1.0/direct?q=" + weather_string + "&appid=061b1d096c35c4becdf0adec17e79675"

    # return response
    response = requests.get(weather_url)

    # error check
    status_code = response.status_code

    if status_code != 200:
        print("Apologies! Please try again later.")
        quit()

    # convert json and to long/lat, return Indexerror if city/state/country is typed incorrectly or not found
    try:
        results = response.json()
        target_location = results[0]

        longitude = target_location["lon"]
        latitude = target_location["lat"]

        print("Just a moment - looking up current weather data for " + target_location["name"] + ", " + target_location["state"] + ", " + target_location["country"])

        weather_url = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(latitude) + "&lon=" + str(longitude) + "&appid=061b1d096c35c4becdf0adec17e79675&units=metric"

        response = requests.get(weather_url)

        status_code = response.status_code

        # check errors and results
        if status_code == 200:
            data = response.json()
            # getting the main block
            weather_main = data['main']
            # getting weather results
            temperature = weather_main['temp']
            humidity = weather_main['humidity']
            temp_min = weather_main['temp_min']
            temp_max = weather_main['temp_max']
            pressure = weather_main['pressure']
            feels_like = weather_main['feels_like']
            weather_report = data['weather']
            clouds = data['clouds']
            # print in a readable format
            degree_sign = u"\N{degree sign}"
            print(f"{user_city.upper():-^50}")
            print(f"Longitude: {longitude}")
            print(f"Latitude: {latitude}")
            print(f"Current Temperature: {temperature}", degree_sign, "C")
            print(f"Feels like: {feels_like}", degree_sign, "C")
            print(f"Min Temperature: {temp_min}", degree_sign, "C")
            print(f"Max Temperature: {temp_max}", degree_sign, "C")
            print(f"Current Humidity: {humidity} %")
            print(f"Current Pressure: {pressure} hPa")
            print(f"Cloud Cover: {clouds['all']} %")
            print(f"If you go outside, you'll see {weather_report[0]['description']}.")
        else:
            # showing the error message
            print("Apologies! Please try again later.")
            quit()
    except IndexError:
        print("Location not found. Please try again.")


def weather_get_city_fahrenheit():
    import requests

    # prompt user for city info
    user_city = str(input("Enter city name: "))
    user_state = str(input("State: "))
    user_country = str(input("Country: "))

    user_inputs = []
    if len(user_city) > 0:
        user_inputs.append(user_city)

    if len(user_state) > 0:
        user_inputs.append(user_state)

    if len(user_country) > 0:
        user_inputs.append(user_country)

    weather_string = ",".join(user_inputs)
    # print(user_inputs)

    api_key = "061b1d096c35c4becdf0adec17e79675"
    weather_url = "http://api.openweathermap.org/geo/1.0/direct?q=" + weather_string + "&appid=061b1d096c35c4becdf0adec17e79675"

    # return response
    response = requests.request("GET", weather_url)

    # error check
    status_code = response.status_code

    if status_code != 200:
        print("Apologies! Please try again later.")
        quit()

    # convert json and to long/lat and return Indexerror if city/state/country is typed incorrectly
    try:
        results = response.json()
        target_location = results[0]

        longitude = target_location["lon"]
        latitude = target_location["lat"]

        print("Just a moment - looking up current weather data for " + target_location["name"] + ", " + target_location["state"] + ", " + target_location["country"])

        weather_url = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(latitude) + "&lon=" + str(longitude) + "&appid=061b1d096c35c4becdf0adec17e79675&units=imperial"

        response = requests.request("GET", weather_url)
        status_code = response.status_code

        # check errors and results
        if status_code == 200:
            data = response.json()
            # getting the main block
            weather_main = data['main']
            # getting weather results
            temperature = weather_main['temp']
            humidity = weather_main['humidity']
            temp_min = weather_main['temp_min']
            temp_max = weather_main['temp_max']
            pressure = weather_main['pressure']
            feels_like = weather_main['feels_like']
            weather_report = data['weather']
            clouds = data['clouds']
            # print in a readable format
            degree_sign = u"\N{degree sign}"
            print(f"{user_city.upper():-^50}")
            print(f"Longitude: {longitude}")
            print(f"Latitude: {latitude}")
            print(f"Current Temperature: {temperature}", degree_sign, "F")
            print(f"Feels like: {feels_like}", degree_sign, "F")
            print(f"Min Temperature: {temp_min}", degree_sign, "F")
            print(f"Max Temperature: {temp_max}", degree_sign, "F")
            print(f"Current Humidity: {humidity} %")
            print(f"Current Pressure: {pressure} hPa")
            print(f"Cloud Cover: {clouds['all']} %")
            print(f"If you go outside, you'll see {weather_report[0]['description']}.")
        else:
            # showing the error message
            print("Apologies! Please try again later.")
            quit()
    except IndexError:
        print("Location not found. Please try again.")


def weather_get_zip_celsius():
    import requests

    while True:
        # prompt user for zipcode
        user_zip = str(input("Enter zipcode: "))

        if len(user_zip) == 5:
            user_zip = str(user_zip)
        else:
            print("Please try again. Incorrect zipcode.")

        api_key = "061b1d096c35c4becdf0adec17e79675"
        weather_url = "http://api.openweathermap.org/geo/1.0/zip?zip=" + str(user_zip) + ",us&appid=061b1d096c35c4becdf0adec17e79675&units=metric"

        # return response
        response = requests.request("GET", weather_url)

        # error check
        status_code = response.status_code

        if status_code == 200:
            # convert json and to long/lat
            results = response.json()
            target_location = results

            # for target_location in results:
            longitude = target_location["lon"]
            latitude = target_location["lat"]
            city_name_by_zipcode = target_location["name"]

            print("Just a moment - looking up current weather data for " + user_zip + ": " + city_name_by_zipcode)

            weather_url = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(latitude) + "&lon=" + str(longitude) + "&appid=061b1d096c35c4becdf0adec17e79675&units=metric"

            response = requests.request("GET", weather_url)

            status_code = response.status_code

            # check errors and results
            if status_code == 200:
                data = response.json()
                # getting the main block
                weather_main = data['main']
                # getting weather results
                temperature = weather_main['temp']
                humidity = weather_main['humidity']
                temp_min = weather_main['temp_min']
                temp_max = weather_main['temp_max']
                pressure = weather_main['pressure']
                feels_like = weather_main['feels_like']
                report = data['weather']
                clouds = data['clouds']
                # print in a readable format
                degree_sign = u"\N{degree sign}"
                print(f"{user_zip.upper():-^50}")
                print(f"City: {city_name_by_zipcode}")
                print(f"Current Temperature: {temperature}", degree_sign, "C")
                print(f"Feels like: {feels_like}", degree_sign, "C")
                print(f"Min Temperature: {temp_min}", degree_sign, "C")
                print(f"Max Temperature: {temp_max}", degree_sign, "C")
                print(f"Current Humidity: {humidity} %")
                print(f"Current Pressure: {pressure} hPa")
                print(f"Cloud Cover: {clouds['all']} %")
                print(f"If you go outside, you'll see {report[0]['description']}.")
            else:
                # showing the error message
                print("Apologies! Zipcode not found. Please try again.")
                break
        else:
            print("Apologies! Not found. Please try again.")
            break
        break


def weather_get_zip_fahrenheit():
    import requests

    while True:
        # prompt user for zipcode
        user_zip = str(input("Enter zipcode: "))

        if len(user_zip) == 5:
            user_zip = str(user_zip)
        else:
            print("Please try again. Incorrect zipcode.")

        api_key = "061b1d096c35c4becdf0adec17e79675"
        weather_url = "http://api.openweathermap.org/geo/1.0/zip?zip=" + str(user_zip) + ",us&appid=061b1d096c35c4becdf0adec17e79675&units=imperial"

        # return response
        response = requests.request("GET", weather_url)

        # error check
        status_code = response.status_code

        if status_code == 200:
            # convert json and to long/lat
            results = response.json()
            target_location = results

            # for target_location in results:
            longitude = target_location["lon"]
            latitude = target_location["lat"]
            city_name_by_zipcode = target_location["name"]

            print("Just a moment - looking up current weather data for " + user_zip + ": " + city_name_by_zipcode)

            weather_url = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(latitude) + "&lon=" + str(longitude) + "&appid=061b1d096c35c4becdf0adec17e79675&units=imperial"

            response = requests.request("GET", weather_url)

            status_code = response.status_code

            # check errors and results
            if status_code == 200:
                data = response.json()
                # getting the main block
                weather_main = data['main']
                # getting weather results
                temperature = weather_main['temp']
                humidity = weather_main['humidity']
                temp_min = weather_main['temp_min']
                temp_max = weather_main['temp_max']
                pressure = weather_main['pressure']
                clouds = data['clouds']
                feels_like = weather_main['feels_like']
                report = data['weather']
                # print in a readable format
                degree_sign = u"\N{degree sign}"
                print(f"{user_zip.upper():-^50}")
                print(f"City: {city_name_by_zipcode}")
                print(f"Current Temperature: {temperature}", degree_sign, "F")
                print(f"Feels like: {feels_like}", degree_sign, "F")
                print(f"Min Temperature: {temp_min}", degree_sign, "F")
                print(f"Max Temperature: {temp_max}", degree_sign, "F")
                print(f"Current Humidity: {humidity} %")
                print(f"Current Pressure: {pressure} hPa")
                print(f"Cloud Cover: {clouds['all']} %")
                print(f"If you go outside, you'll see {report[0]['description']}.")
            else:
                # showing the error message
                print("Apologies! Zipcode not found. Please try again.")
                break
        else:
            print("Apologies! Not found. Please try again.")
            break
        break


def weather_celsius():
    while True:
        print("Please enter 'C' for a new city/state, 'Z' for a new zipcode,  or 'B' to go Back:")
        operation_weather_c = str(input(">>> "))
        print("-"*50)
        if operation_weather_c.lower() == "c":
            weather_get_city_celsius()
            print("-"*50)
        elif operation_weather_c.lower() == "z":
            weather_get_zip_celsius()
            print("-"*50)
        elif operation_weather_c.lower() == "b":
            print("Back to the beginning!")
            break
        else:
            print("Please enter 'C' for a new city/state, 'Z' for a new zipcode, or 'B' to go Back:")


def weather_fahrenheit():
    while True:
        print("Please enter 'C' for a new city/state, 'Z' for a new zipcode,  or 'B' to go Back:")
        operation_weather_f = str(input(">>> "))
        print("-"*50)
        if operation_weather_f.lower() == "c":
            weather_get_city_fahrenheit()
            print("-"*50)
        elif operation_weather_f.lower() == "z":
            weather_get_zip_fahrenheit()
            print("-"*50)
        elif operation_weather_f.lower() == "b":
            print("Back to the beginning!")
            break
        else:
            print("Please enter 'C' for a new city/state, 'Z' for a new zipcode, or 'B' to go Back:")


def main():
    print("Hello! Welcome to the Super Awesome Weather App!")
    print("You can search by city and state (two-letter abbreviation) or by zipcode below:")
    print("-"*50)
    while True:
        print("First, would you like temperatures in Celsius or Fahrenheit? \n Enter 'C' for Celsius or 'F' for Fahrenheit \n Or 'X' to Exit")
        operation_temperature = str(input(">>> "))
        print("-"*50)
        if operation_temperature.lower() == "c":
            weather_celsius()
            print("-"*50)
        elif operation_temperature.lower() == "f":
            weather_fahrenheit()
            print("-"*50)
        elif operation_temperature.lower() == "x":
            print("Done!")
            quit()


if __name__ == "__main__":
    main()
