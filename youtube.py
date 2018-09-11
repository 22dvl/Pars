from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
from datetime import datetime
import json
from iso8601 import parse_date

DEVELOPER_KEY = "AIzaSyAXMxQYAQEbepn_r4UL2XlKZSK3Qh2yKeU"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

b = input ("Дата загрузки(1 - Посл.неделя,2 - Посл.месяц,3 - Посл.год): ")
a = input ("Упорядочить по(1 - дате,2 - просмотрам,3 - рейтингу): ")

if a == '1':
    ord = 'date'
if a == '2':
    ord = 'viewCount'
if a == '3':
    ord = 'rating'

if b == '1':
    datediff = 7
if b == '2':
    datediff = 31
if b == '3':
    datediff = 365

PT = None
datenow = datetime.now()
datenow = datenow.strftime("%Y-%m-%d")

def youtube_search(q, max_results=50,order=ord,page_token=PT, published_After=None):

  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  search_response = youtube.search().list(
    q=q,
    type="video",
    publishedAfter=published_After,
    order = order,
    pageToken = page_token,
    maxResults=max_results
  ).execute()
  global PT
  PT = search_response.get('nextPageToken')



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


for i in range(30):
    test = youtube_search("spinners")
    print (test[1])
    for video in test[1]:
        datevid = parse_date(video['snippet']['publishedAt'])
        datevid = datevid.strftime("%Y-%m-%d")
        d1 = datetime.strptime(datenow, "%Y-%m-%d")
        d2 = datetime.strptime(datevid, "%Y-%m-%d")
        d = (d1-d2).days
        if (d <= datediff):
            print (video['id']['videoId'])
            print (video['snippet']['title'])
