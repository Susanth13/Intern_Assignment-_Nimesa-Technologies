import requests

url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
response = requests.get(url).json()
print(response)

while True:
    print("\n1. Get weather\n2. Get Wind Speed\n3. Get Pressure\n0. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
        for item in response['list']:
            if date in item['dt_txt']:
                temp = item['main']['temp']
        if temp:
            print(f"Temperature on {date}: {temp}°C")
        else:
            print("no data for the given date")
    elif choice == '2':
        date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
        for item in response['list']:
            if date in item['dt_txt']:
                wind = item['wind']['speed']
        if wind:
            print(f"wind speed on {date}  is {wind}")
        else:
            print("no data for the given date")

    elif choice == '3':
        date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
        for item in response['list']:
            if date in item['dt_txt']:
                pressure = item['main']['pressure']
        if pressure:
            print(f"pressure on {date} is {pressure}")
        else:
            print("no data for the given date")
    elif choice == '0':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
