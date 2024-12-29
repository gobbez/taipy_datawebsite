from taipy.gui import Gui
import taipy.gui.builder as tgb

from pages import home
from pages.trends import trends_page
from pages.chatbotai import chatbotai_page
from pages.weather import weather_page


def load_navbar():
    """Add a navbar to switch from one page to the other """
    with tgb.Page() as navbar:
        tgb.navbar()
    return navbar


# Run the application
if __name__ == "__main__":
    navbar = load_navbar()
    home = home.load_home()
    trends = trends_page.load_trends()
    chatbot_istat = chatbotai_page.load_chatbot()
    weather = weather_page.load_meteo()
    pages = {
        "/": navbar,
        "Home": home,
        "Trends": trends,
        "Chatbot": chatbot_istat,
        "Weather": weather
    }

    gui = Gui(pages=pages)
    gui.run(title="Vignate Insights")
