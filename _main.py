import datetime
import json
import requests
import datetime
import time
from secrets import token, user

#print("Enter the date of starting scrobbled:")
#date_time = input()
date_time = datetime.datetime(2022, 1, 1, 0, 0, 0)
print("Given Date:",date_time)
#print("UNIX timestamp:",
#    (time.mktime(date_time.timetuple())))

from_time = time.mktime(date_time.timetuple())
#print(type(int(date_time)))
print(from_time)

def get_track_list():
    query = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={}&api_key={}&limit=200&format=json".format(user, token)
    response = requests.get(query)
    response_json = response.json()
    l_artist = []
    l_name = []
    pages_count = response_json["recenttracks"]["@attr"]["totalPages"]
    pages_count_int = int(pages_count)
    print(pages_count_int)
    page: int = 1
    while page < pages_count_int:
        query2 = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={}&api_key={}&limit=200&format=json&pages{}".format(
        user, token,page)
        response = requests.get(query2)
        response_json = response.json()
        for i in response_json["recenttracks"]["track"]:
            l_artist.append(i["artist"]["#text"])
            l_name.append(i["name"])
        page += 1
        print('Page done')
        print(page)

    list = [l_artist, l_name]
    #print('done')
get_track_list()

#def get_track_