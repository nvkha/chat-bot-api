
import sys
import os
os.chdir("..")
sys.path.append(os.getcwd())
import datetime
import requests
from app.utils.crypto import CryptoUtils
from app.settings import ZING_MP3_API_KEY

SECRET_KEY = b'10a01dcf33762d3a204cb96429918ff6'

class MusicSkills:

    @classmethod
    def get_song(cls, question): 
        question = cls.__question_reprocess(question)
        id = cls.__find_song_id(question)
        ctime = datetime.datetime.now().timestamp()
        url = 'https://zingmp3.vn/api/song/get-song-info?'
        a = f'ctime={ctime}id={id}'    
        path = '/song/get-song-info' + CryptoUtils.get_hash_256(a.encode())
        sig = CryptoUtils.get_hmac_512(path.encode(), SECRET_KEY)
        complete_url = url + f"id={id}&ctime={ctime}&sig={sig}&api_key={ZING_MP3_API_KEY['key']}"

        a_session = requests.Session()
        a_session.get(complete_url)
        cookies = a_session.cookies
        
        try:
            response = requests.get(complete_url, verify=False, cookies=cookies)
            data = response.json()
       
            song_url = data['data']['streaming']['default']['128']
            return song_url
            '''
            song = requests.get(song_url)
            song = song.content
            with open("sounds\song.mp3", "wb") as f:
                f.write(song)
            '''
        except Exception as e: 
            print(e)
            return None
        
    
    def __find_song_id(question):
        url_info = f'http://ac.mp3.zing.vn/complete?type=artist,song,key,code&num=500&query={question}'

        try:
            response = requests.get(url_info)
            song_info = response.json()
            song_info = song_info['data'][0]['song'][0]
            id = song_info['id']
            return id
        except:
            return None

    def __question_reprocess(question):
        question = question.lower()
        return question.replace("tìm", "").replace("bài", "").replace("hát", "")
