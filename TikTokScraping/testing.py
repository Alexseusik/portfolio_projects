import csv
import json
import re
import requests

manual = ['6974830108343307526', '6976830373909024005', '6974881381553868037', '6977241250927840517',
          '6976810980537863429', '6976826683424918789', '6974842192703671558', '6977402087676087558',
          '6976807311801175301', '6976809242317606150', '6974814697732230406', '6975569254166940933',
          '6976316010005646598', '6976309195041787141', '6977228543893753093', '6977227106900004101',
          '6976313183854234885', '6976428999346277638']
url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"
headers = {
	"X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com",
	"X-RapidAPI-Key": "c45ae8004amshe4c887937ff8b87p18fadejsn91357195fc44"
}
raw_data = json.loads(open('thefasttrackgirl.json', 'r+').read())

with open('raw.txt', 'a') as f:
    for video_info in raw_data:
        if video_info['id'] in manual:
            name = re.search(r'\d+$', video_info['webVideoUrl']).group(0)
            print(name)
            querystring = {"url": video_info['webVideoUrl']}
            response = requests.request("GET", url, headers=headers, params=querystring)
            res = json.loads(response.text)['video'][0]
            print(res)
            f.write(name + ' ' + res + '\n')
        else:
            continue
    f.close()
'''
- Date Uploaded

- Description

- Length/Duration

- Likes

- Shares

- Comment Count

- Play Count
'''
# raw_data = json.loads(open('thefasttrackgirl.json', 'r+').read())
# i = 1
# with open('result.csv', 'a') as o:
#     writer = csv.writer(o)
#     writer.writerow(['Video_id', 'Date Uploaded', 'Description', 'Duration', 'Likes', 'Shares', 'Comment Count',
#                      'Play Count'])
#     for video in raw_data:
#         print(f'Cool +1. Total is : {i}')
#         video_id = video['id']
#         uploaded_date = re.search(r'\d{4}-\d{2}-\d{2}', video['createTimeISO']).group(0)
#         description = video['text']
#         duration = video['videoMeta']['duration']
#         likes = video['diggCount']
#         shares = video['shareCount']
#         comments = video['commentCount']
#         play_count = video['playCount']
#         video_data = [video_id, uploaded_date, description, duration, likes, shares, comments, play_count]
#         writer.writerow(video_data)
#         i += 1

