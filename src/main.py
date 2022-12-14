import os, json

from time import sleep

def loadJson():
    with open('./config.json') as f:
        return json.load(f)

def main():
    json = loadJson()
    if (json['title']):
        print(f"\33]0;{json['title']}\a", end='', flush=True)

    video = json['audioUrl']
    if (not video):
        video = input('Enter the video url: ')

    image = json['imageUrl']

    if (not image):
        image = input('Enter the image url: ')

    os.system(f"mpv --no-video {video} &>/dev/null &")
    os.system("clear")
    os.system(f"kitty +kitten icat '{image}'")

    while (True):
        if (input("Enter 'q' to quit: ") == 'q'):
            os.system("killall mpv")
            break
        sleep(0.5)
    
main()