import os
import logging
from pathlib import Path
import pandas as pd
from taipy.gui import Gui
import taipy.gui.builder as tgb
from pandasai import SmartDataframe


def load_chatbot():
    # API KEY
    os.environ["PANDASAI_API_KEY"] = 'YOUR_PANDASAI_API_KEY'

    THIS_FOLDER = Path(__file__).parent.resolve()
    istatcsv_path = THIS_FOLDER / '../../files/Dati ISTAT Vignate - Dati.csv'
    beta_icon = THIS_FOLDER / 'betabtn.png'

    def answer(question):
        """AI model will answer with text or images"""
        # Load Csv and AI
        df_istat = pd.read_csv(istatcsv_path)
        df_istat = df_istat.dropna()
        df_istat_ai = SmartDataframe(df_istat)
        answer = df_istat_ai.chat(question)
        return answer

    def submit_question(state):
        """Receive user input and send answer"""
        state.ai_answer = answer(state.question)

    def quick1(state):
        q = "How many residenti in Vignate 2023"
        state.question = q
        state.ai_answer = answer(q)

    def quick2(state):
        q = "What's the year with more Citt. Stranieri?"
        state.question = q
        state.ai_answer = answer(q)

    def quick3(state):
        q = "How many 0 a 14 anni in 2023?"
        state.question = q
        state.ai_answer = answer(q)

    def quick4(state):
        q = "What's the età media 2023?"
        state.question = q
        state.ai_answer = answer(q)

    question = "What's the year with more residents in Vignate?"
    ai_answer = answer(question)
    description = (f"In this page you can ask questions to a simple PandasAI chatbot, with Istat dataset access"
                   f"You can click on the pre-made questions."
                   f"It's a beta, it may respond incorrectly.")

    """Page with AI CHATBOT"""
    # Define the page layout
    with tgb.Page() as chatbotai:
        with tgb.layout(columns="5 10 1"):
            tgb.text(value="# ChatBot AI - Vignate", mode="md")
            tgb.image(content="{beta_icon}", width="64px", height="64px")
            tgb.button(label='Informations', hover_text=description, class_name="secondary")
        with tgb.layout(columns="5 15"):
            tgb.input(label="Ask a question..", value="{question}", width="500px")
            tgb.button(label='Ask', id='submit', on_action=submit_question)
        tgb.text(value="{ai_answer}", mode="pre", class_name="taipy-text")
        tgb.text(value="### Pre-made questions", mode="md")
        with tgb.layout(columns="10 20 70 350"):
            tgb.button(label="Residents 2023", on_action=quick1)
            tgb.button(label="Year with more extracomunitaries", on_action=quick2)
            tgb.button(label="0-14 years 2023", on_action=quick3)
            tgb.button(label="Average Age 2023", on_action=quick4)
    return chatbotai