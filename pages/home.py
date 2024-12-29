from taipy.gui import Gui
import taipy.gui.builder as tgb
from pathlib import Path


def load_home():
    intro = f"_Welcome!_"
    descr1 = "#### _This website lets you get insights on web trends_ "
    descr2 = "#### _You can ask question to the *ChatBot* on the data_ "
    descr3 = "#### _You can see weather informations_ "
    descr4 = "Website created by gobbez"

    THIS_FOLDER = Path(__file__).parent.resolve()
    image = THIS_FOLDER / 'home.png'

    with tgb.Page() as home:
        tgb.text(value="# HOME PAGE", mode="md")
        tgb.text(value="{intro}", mode="md")
        tgb.image(content="{image}", width="320", height="320")
        tgb.text(value="{descr1}", mode="md")
        tgb.text(value="{descr2}", mode="md")
        tgb.text(value="{descr3}", mode="md")
        tgb.text(value="{descr4}", mode="md")



    return home
