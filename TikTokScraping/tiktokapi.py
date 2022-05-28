import requests
import json

url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

json_file = json.loads(open('thefasttrackgirl.json', 'r+').read())
all_data = []
headers = {
	"X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com",
	"X-RapidAPI-Key": "c45ae8004amshe4c887937ff8b87p18fadejsn91357195fc44"
}

for video in json_file:
    all_data.append({'name': video['id'], 'videourl': video['webVideoUrl']})
    print({'name': video['id'], 'videourl': video['webVideoUrl']})

with open('result_pack4.json', 'a') as f:
    for element in all_data:
        querystring = {"url": element['videourl']}
        response = requests.request("GET", url, headers=headers, params=querystring)
        result = json.loads(response.text)
        video_url = result['video']
        element = json.dumps({'name': element['name'], 'url': video_url})
        print(element)
        f.write(str(element) + ',' + '\n')
        print('Success!')
    f.close()
