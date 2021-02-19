import pychromecast
import sys
from gtts import gTTS
import os
import time
import argparse
import socket


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
    time.sleep(1)
    while mc.status.player_is_playing:
        time.sleep(1)

def generate_audio(text, language, save_path):
    tts = gTTS(text=text, lang=language)
    tts.save(save_path)

def main(device_name, text, language):
    #get local ip address
    ip_address = socket.gethostbyname(socket.gethostname())

    audio_path = "./GoogleHomeSpeak/audio.mp3"
    #set local server url
    voice_url = "http://{}:8000".format(ip_address)

    generate_audio(text, language, audio_path)
    fetch_play(device_name, voice_url)
    os.remove(audio_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='GoogleHomeSpeak')
    parser.add_argument('device_name', help='Google Home device name.')
    parser.add_argument('text', help='Text spoken by Google Home.')
    parser.add_argument('--language', '-l', default="ja",
                        help='Text language setting. \
                        Default setting is Japanese. \
                        Set to "en" if you use English.')
    args = parser.parse_args()
    main(args.device_name, args.text, args.language)
