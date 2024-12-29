import asyncio
import python_weather
from taipy.gui import Gui
import taipy.gui.builder as tgb


async def get_weather():
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        weather = await client.get('Milan')

        # Get data
        wtime = weather.datetime
        wcountry = weather.country
        wregion = weather.region
        wcoord = weather.coordinates
        wtemp = str(weather.temperature) + "°C"
        whumidity = weather.humidity
        wprecipitations = weather.precipitation
        wdescription = weather.description
        wfeelslike = str(weather.feels_like) + "°C"
        wvisibility = weather.visibility
        wuv = weather.ultraviolet
        wwindspeed = weather.wind_speed
        wwinddirection = weather.wind_direction
        wpressure = weather.pressure

        # Get the weather forecast for one day
        for daily in weather.daily_forecasts:
            tomorrow = daily.date.strftime('%Y-%m-%d')
            tomorrow_high = str(daily.highest_temperature) + "°C"
            tomorrow_low = str(daily.lowest_temperature) + "°C"
            tomorrow_sunrise = daily.sunrise
            tomorrow_sunhours = daily.sunlight
            break

        return {
            "wtime": wtime,
            "wcountry": wcountry,
            "wregion": wregion,
            "wcoord": wcoord,
            "wtemp": wtemp,
            "whumidity": whumidity,
            "wprecipitations": wprecipitations,
            "wdescription": wdescription,
            "wfeelslike": wfeelslike,
            "wvisibility": wvisibility,
            "wuv": wuv,
            "wwindspeed": wwindspeed,
            "wwinddirection": wwinddirection,
            "wpressure": wpressure,
            "tomorrow": tomorrow,
            "tomorrow_high": tomorrow_high,
            "tomorrow_low": tomorrow_low,
            "tomorrow_sunrise": tomorrow_sunrise,
            "tomorrow_sunhours": tomorrow_sunhours
        }


def load_meteo():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    weather_data = loop.run_until_complete(get_weather())

    description = f"Weather conditions of Milan"
    today_prevision = f"It's {weather_data['wtime']} and the weather in Milan is {weather_data['wtemp']}"

    with tgb.Page() as meteo:
        with tgb.layout(columns="5 10"):
            tgb.text(value="# Weather - Milan", mode="md")
            tgb.button(label='Informations', hover_text=description, class_name="secondary")
        tgb.text(value="{today_prevision}", mode="pre")
        tgb.text(value="### Weather data", mode="md")
        tgb.text(value=f"Town: Milan", mode="pre")
        tgb.text(value=f"Nation: {weather_data['wcountry']}", mode="pre")
        tgb.text(value=f"Region: {weather_data['wregion']}", mode="pre")
        tgb.text(value=f"Coordinates: {weather_data['wcoord']}", mode="pre")
        tgb.text(value=f"-------", mode="pre")
        tgb.text(value=f"Precipitations: {weather_data['wprecipitations']}", mode="pre")
        tgb.text(value=f"Perceived Temperature: {weather_data['wfeelslike']}", mode="pre")
        tgb.text(value=f"Wind: {weather_data['wwindspeed']} -- {weather_data['wwinddirection']}", mode="pre")
        tgb.text(value=f"Pressure: {weather_data['wpressure']}", mode="pre")
        tgb.text(value=f"Visibility: {weather_data['wvisibility']}", mode="pre")

    return meteo
