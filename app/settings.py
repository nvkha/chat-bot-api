import os
from dotenv import load_dotenv

load_dotenv()

WOLFRAMALPHA_API = {
    "key": os.getenv("WOLFRAMALPHA_APP_ID")
}

OPENWEATHER_API = {
    "key": os.getenv("OPENWEATHER_API_KEY")
}

ZING_MP3_API_KEY = {
    "key": os.getenv("ZING_MP3_API_KEY")
}

HUNGGINGFACE_API = {
    "key": os.getenv("HUNGGINGFACE_API_KEY")
}

ZALO_TTS_API = {
    "key": os.getenv("ZALO_TTS_API_KEY")
}