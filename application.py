import requests
import time
import sys
import video_page_processor as processor

target_host = 'https://www.youtube.com/watch'
video = '8NXF6XO5g9c'


def get_video_page(url, video_id):
    param = {'v': video_id}
    try:
        resp = requests.get(url, params=param, timeout=2)
        if resp.status_code == requests.codes.ok:
            processor.process_node(resp.text)

    except requests.exceptions.ConnectionError:
        print('Connection dropped.')


if len(sys.argv) == 2:
    while True:
        get_video_page(target_host, sys.argv[1])
        time.sleep(1)
else:
    print('Usage: python application.py <video_id>')
