from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
from datetime import datetime
import json
from iso8601 import parse_date

DEVELOPER_KEY = "AIzaSyAXMxQYAQEbepn_r4UL2XlKZSK3Qh2yKeU"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

b = input ("Дата загрузки(0 - Все по порядку, 1 - Посл.неделя,2 - Посл.месяц,3 - Посл.год): ")
a = input ("Упорядочить по(0 - Все по порядку,1 - дате,2 - просмотрам,3 - рейтингу): ")

if a == '1':
    ord = 'date'
if a == '2':
    ord = 'viewCount'
if a == '3':
    ord = 'rating'
if a == '0':
    ord = 'date'

if b == '1':
    datediff = 7
if b == '2':
    datediff = 31
if b == '3':
    datediff = 365
if b == '0':
    datediff = 7

datenow = datetime.now()
datenow = datenow.strftime("%Y-%m-%d")

PT = None
PTCount = 0

a1 = open('output.txt', 'w')

def youtube_search(q, token,  max_results=50, order=ord):

  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  search_response = youtube.search().list(
    q=q,
    type="video",
    pageToken=token,
    order = order,
    part="id,snippet",
    maxResults=max_results

  ).execute()

  global PT
  global ord
  global PTCount
  PT = search_response.get('nextPageToken')
  search_response['pageToken']=PT
  PTCount = PTCount + 1
  videos = []

  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append(search_result)
  try:
      nexttok = search_response["nextPageToken"]
      return(nexttok, videos)
  except Exception as e:
      nexttok = "last_page"
      return(nexttok, videos)

def glav():
    global PT
    global f
    global a1
    global datediff
    global PTCount
    f = open('requests.txt')
    for line in f:
        while PTCount <= 18:
            test = youtube_search(line,PT)
            for video in test[1]:
                datevid = parse_date(video['snippet']['publishedAt'])
                datevid = datevid.strftime("%Y-%m-%d")
                d1 = datetime.strptime(datenow, "%Y-%m-%d")
                d2 = datetime.strptime(datevid, "%Y-%m-%d")
                d = (d1-d2).days
                if (d <= datediff):
                    a1.close()
                    vid_id = (video['id']['videoId'])
                    a1 = open('output.txt', 'a')
                    a1.write("https://www.youtube.com/watch?v="+vid_id + '\n')
    return
glav()
PT = None
PTCount = 0
if b == '0' and a != '0':
    datediff = 31
    glav()
    datediff = 365
    PT = None
    PTCount = 0
    glav()
if a == '0' and b != '0':
    ord = 'viewCount'
    PT = None
    PTCount = 0
    glav()
    ord = 'rating'
    PT = None
    PTCount = 0
    glav()
if a == '0' and b == '0':
    datediff = 31
    glav()
    datediff = 365
    PT = None
    PTCount = 0
    glav()
    ord = 'viewCount'
    datediff = 7
    PT = None
    PTCount = 0
    glav()
    datediff = 31
    PT = None
    PTCount = 0
    glav()
    datediff = 365
    PT = None
    PTCount = 0
    glav()
    ord = 'rating'
    datediff = 7
    PT = None
    PTCount = 0
    glav()
    datediff = 31
    PT = None
    PTCount = 0
    glav()
    datediff = 365
    PT = None
    PTCount = 0
    glav()
