import sys
import os
import path
sys.path.append(str(path.Path(os.getcwd()).parent))
from app.skills import calculate, datetime_, food, greeting, knowledge, music, news, weather
from neuralintents import GenericAssistant
from googletrans import Translator
from pathlib import Path



mappings = {
    "greeting": greeting.GreetingSkills.greeting,
    "ask_time": datetime_.DateTimeSkills.get_time,
    "ask_day": datetime_.DateTimeSkills.get_date,
    "ask_knowledge": knowledge.KnowledgeSkills.get_anwser,
    "ask_news": news.NewsSkills.get_news,
    "calculate": calculate.CalculateSkills.calculate,
    "ask_weather": weather.WeatherSkills.get_weather_forecast,
    "find_song": music.MusicSkills.get_song,
    "goodbye": greeting.GreetingSkills.bye,
    "ask_food": food.FoodSkills.get_food_info
}

class NLP:
    def __init__(self):
        d = Path(__file__).resolve().parents[1]
        self.assistant = GenericAssistant(os.path.join(d, "files/intents.json"), intent_methods=mappings)
        self.assistant.train_model()
        self.translator = Translator()

    def get_answer(self, question):
        question_en = self.translator.translate(question, dest='en').text
        ints = self.assistant._predict_class(question_en)
        if ints[0]['intent'] in mappings.keys():
            return mappings[ints[0]['intent']](question)



