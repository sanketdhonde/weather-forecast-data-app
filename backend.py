import requests

API_KEYS = ed69921f2894e1208d2fbdab923f217f

def get_data(place, forecast_days, kind):
    url =f"http://api.openweathermap.org/data/2.5/forecast?q={placd}&appid={API_KEYS}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["lsit"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    if kind == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if kind == "Sky":
        filtered_data = [dict["weather"]["main"] for dict in filtered_data]
    return filtered_data

if __name__=="main":
    print(get_data(place="Tokyo", forecast_days=3, kind="Temperature"))
