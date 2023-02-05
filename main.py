import datetime
import json
import requests
import datetime
import time
import xlsxwriter
import pylast
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
    l_id = []
    l_artist = []
    l_name = []
    pages_count = response_json["recenttracks"]["@attr"]["totalPages"]
    pages_count_int = int(pages_count)
    print(pages_count_int)
    page: int = 1
#    while page < pages_count_int:
    while page < 2:
        query2 = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={}&api_key={}&limit=200&format=json&pages{}".format(
        user, token, page)
        response = requests.get(query2)
        response_json = response.json()
        for i in response_json["recenttracks"]["track"]:
            l_artist.append(i["artist"]["#text"])
            l_name.append(i["name"])
            l_id.append(i["mbid"])
        page += 1
        print('Page done')
        print(page)
        l_full = [l_artist, l_name]
#       print(l_id)
#    workbook = xlsxwriter.Workbook('Example2.xlsx')
#    worksheet = workbook.add_worksheet()
#    row = 0
#    column = 0
#    for item in l_id:
#        worksheet.write(row, column, item)
#        row += 1
#    row = 0
#    column_2 = column + 1
#    for item in l_artist:
#        worksheet.write(row, column_2, item)
#        row += 1
#    row = 0
#    column_3 = column_2 + 1
#    for item in l_name:
#        worksheet.write(row, column_3, item)
#        row += 1
#    workbook.close()

#    list = [l_artist, l_name]
    #print('done')
    return l_full
get_track_list()

def get_track_duration(self):
    track_list = get_track_list()
    track_duration = []
    x: int = 0
    y: int = 0
    length = len(track_list)
    while x < length:
#            x = 0
#            y = 0
            track = pylast.Track("{}", "{}", self.network).format(track_list[x],track_list[y])
            duration = track.get_duration()
            track_duration.append(duration)
            x += 1
            y += 1
    print(track_duration)
get_track_duration(self)



