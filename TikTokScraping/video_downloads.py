import progressbar
import json
import urllib.request

pbar = None

videosurl = [el['url'] for el in json.loads(open('data.json').read())]
print(videosurl)


def show_progress(block_num, block_size, total_size):
    global pbar
    if pbar is None:
        pbar = progressbar.ProgressBar(maxval=total_size)
        pbar.start()

    downloaded = block_num * block_size
    if downloaded < total_size:
        pbar.update(downloaded)
    else:
        pbar.finish()
        pbar = None


with open('raw.txt', 'r+') as f:
    for line in f:
        name, url = line.strip().split()
        urllib.request.urlretrieve(url, filename=f'videos/{name}.mp4', reporthook=show_progress)
