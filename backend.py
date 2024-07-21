import requests

API_KEYS = "ed69921f2894e1208d2fbdab923f217f"

def get_data(place, forecast_days):
    url =f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEYS}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data

