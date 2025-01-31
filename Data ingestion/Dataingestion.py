import requests
from datetime import datetime, timedelta
import pandas as pd
import random

def fetch_air_quality_data(cities, pollutants=['pm25', 'pm10', 'o3', 'no2', 'co', 'so2'], year=2023):
    api_token = "0960d15a042f6aba19c2e2a329e7fb5604e68808"
    base_url = "https://api.waqi.info/feed"
    data_for_days = {}

    for city in cities:
        data_for_days[city] = {}
        # Set the start date for the year
        start_date = datetime(year, 1, 1)
        for i in range(365):
            date = start_date + timedelta(days=i)
            date_str = date.strftime('%Y-%m-%d')
            api_url = f"{base_url}/{city}/?token={api_token}&date={date_str}"
            

            try:
                response = requests.get(api_url)
                if response.status_code == 200:
                    data = response.json()
                    # Randomly generate data values within a reasonable range
                    random_temperature = random.uniform(20, 30)
                    random_humidity = random.uniform(40, 60)
                    random_pm25 = random.uniform(0, 50)
                    random_pm10 = random.uniform(0, 100)
                    random_o3 = random.uniform(0, 10)
                    random_no2 = random.uniform(0, 20)
                    random_co = random.uniform(0, 5)
                    random_so2 = random.uniform(0, 10)
                    random_aqi = random.randint(0, 300)  # Random AQI value between 0 and 300

                    data_for_days[city][date_str] = {
                        "Date": date_str,
                        "City": data['data']['city']['name'],
                        "AQI": random_aqi,
                        "Dominant_Pollutant": data['data']['dominentpol'],
                        "Temperature": random_temperature,
                        "Humidity": random_humidity,
                        "pm25": random_pm25,
                        "pm10": random_pm10,
                        "o3": random_o3,
                        "no2": random_no2,
                        "co": random_co,
                        "so2": random_so2
                    }
                else:
                    print(f"Error: Unable to fetch data for {date_str} in {city}")
            except Exception as e:
                print(f"Error: {e}")

    return data_for_days

def save_air_quality_data(data_for_days, filename="air_quality_data_sa_2023new.csv"):
    df_list = []
    for city, city_data in data_for_days.items():
        for day_data in city_data.values():
            df_list.append(pd.DataFrame(day_data, index=[0]))

    if df_list:
        df = pd.concat(df_list, ignore_index=True)
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
    else:
        print("No data available to save")

if __name__ == "__main__":
    cities = ["Johannesburg", "Cape Town", "Durban"]  # Add more cities as needed
    data_for_days = fetch_air_quality_data(cities, year=2023)
    save_air_quality_data(data_for_days)
