import json
from isodate import parse_duration
from urllib.request import urlopen
from urllib.parse import urlparse
from urllib.error import HTTPError

api_key="AIzaSyAXMxQYAQEbepn_r4UL2XlKZSK3Qh2yKeU"
f = open('links.txt')
a = open('output.txt', 'w')
sec = input ("Введите минимальную длину в секундах: ")
for line in f:
    url_data = urlparse(line)
    video_id = url_data.query[2:][:11]
    searchUrl="https://www.googleapis.com/youtube/v3/videos?id="+video_id+"&key="+api_key+"&part=contentDetails"
    try:
        response = urlopen(searchUrl).read()
    except HTTPError:
        continue
    data = json.loads(response)
    all_data=data['items']
    contentDetails=all_data[0]['contentDetails']
    duration=contentDetails['duration']
    dur = parse_duration(duration)
    sectotal = dur.total_seconds()
    if (int(sectotal) >= int(sec)):
        a.write(line + '\n')
print ("Complete")
a.close()