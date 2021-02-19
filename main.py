import pychromecast
import sys
from gtts import gTTS
import os
import time

def fetch_play(device_name, voice_url):
    #search Google Home with Chromecast device name
    chromecasts, _ = pychromecast.get_listed_chromecasts(friendly_names=[device_name])
    if len(chromecasts) == 0:
        print("Not found Google Home.")
        sys.exit(1)

    googleHome = chromecasts[0]
    googleHome.wait()
    mc = googleHome.media_controller

    if mc.status.player_is_playing:
        print("Music is running. Stop music.")
        mc.stop()
        mc.block_until_active(timeout=30)

    print("Playing...")
    mc.play_media(voice_url, "audio/mp3")
    while mc.status.player_is_playing:
        time.sleep(1)

def generate_audio(text, language, save_path):
    tts = gTTS(text=text, lang=language)
    path = ""
    tts.save(save_path)

def main():
    generate_audio(text, language, audio_path)
    fetch_play(device_name, voice_url)
    os.remove(audio_path)
