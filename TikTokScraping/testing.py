import csv
import json
import re
import requests

url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"
headers = {
	"X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com",
	"X-RapidAPI-Key": "rapidkey"
}
raw_data = json.loads(open('thefasttrackgirl.json', 'r+').read())

with open('raw.txt', 'a') as f:
    for video_info in raw_data:
        name = re.search(r'\d+$', video_info['webVideoUrl']).group(0)
        print(name)
        querystring = {"url": video_info['webVideoUrl']}
        response = requests.request("GET", url, headers=headers, params=querystring)
        res = json.loads(response.text)['video'][0]
        print(res)
        f.write(name + ' ' + res + '\n')
    f.close()

raw_data = json.loads(open('thefasttrackgirl.json', 'r+').read())
i = 1
with open('result.csv', 'a') as o:
    writer = csv.writer(o)
    writer.writerow(['Video_id', 'Date Uploaded', 'Description', 'Duration', 'Likes', 'Shares', 'Comment Count',
                     'Play Count'])
    for video in raw_data:
        print(f'Cool +1. Total is : {i}')
        video_id = video['id']
        uploaded_date = re.search(r'\d{4}-\d{2}-\d{2}', video['createTimeISO']).group(0)
        description = video['text']
        duration = video['videoMeta']['duration']
        likes = video['diggCount']
        shares = video['shareCount']
        comments = video['commentCount']
        play_count = video['playCount']
        video_data = [video_id, uploaded_date, description, duration, likes, shares, comments, play_count]
        writer.writerow(video_data)
        i += 1

