import time, requests, webbrowser
from playsound import playsound

# Recommended music : https://www.youtube.com/watch?v=dQw4w9WgXcQ
mp3Link = 'Your path to your music' # Path to mp3 file' #example : 'C:\\Users\\Vince\\Desktop\\Your_music.mp3'
xboxLink = 'https://www.xbox.com/en-ca/configure/8WJ714N3RBTL'
outOfStockString = 'Out of stock'

while True:
    resp = requests.get(xboxLink)
    if resp.ok:
        if outOfStockString in resp.text:
            print("nope")
        else:
            webbrowser.open(xboxLink)
            playsound(mp3Link)
            quit()
    time.sleep(5.0)
