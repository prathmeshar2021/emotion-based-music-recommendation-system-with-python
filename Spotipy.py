import spotipy
import spotipy.oauth2 as oauth2
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time

auth_manager = SpotifyClientCredentials('3a5223af606048028594818c5fa40809','8d770d16cb984245af08462f14832363')
sp = spotipy.Spotify(auth_manager=auth_manager)

def getTrackIDs(user, playlist_id):
    track_ids = []
    playlist = sp.playlist(playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        if track is not None:  # Add check to skip None items
            track_ids.append(track['id'])
    return track_ids


def getTrackFeatures(id):
    track_info = sp.track(id)

    name = track_info['name']
    album = track_info['album']['name']
    artist = track_info['album']['artists'][0]['name']
    url = track_info['external_urls']['spotify']

    track_data = [name, album, artist, url]
    return track_data





# Code for creating dataframe of feteched playlist

emotion_dict = {0:"Angry",1:"Disgusted",2:"Fearful",3:"Happy",4:"Neutral",5:"Sad",6:"Surprised"}
music_dist={0:"2bwaaVtX2fs24efENfEqKr",1:"0n81ha8dSdYLDVc8VpCPsd",2:"6knJbFQAvmTGLl2ktA72a7",3:"37i9dQZF1DX14CbVHtvHRB",4:"3gRfnX2lcTThpZ3QXjVCDf",5:"6knJbFQAvmTGLl2ktA72a7",6:"37i9dQZF1DWWhejoFhUUFy"}

'''
Code can def be modularised into a function but i tried to write it when i was extremely sleepy so thought screw it and repeated code block

Uncomment for fetching updated playlists
'''

track_ids = getTrackIDs('spotify', music_dist[0])
track_list = []
for i in range(len(track_ids)):
    time.sleep(.3)
    track_data = getTrackFeatures(track_ids[i])
    track_list.append(track_data)
df = pd.DataFrame(track_list, columns = ['Name', 'Album', 'Artist', 'URL'])
df.to_csv('songs/angry.csv')
print("CSV Generated")

track_ids = getTrackIDs('spotify', music_dist[1])
track_list = []
for i in range(len(track_ids)):
    time.sleep(.3)
    track_data = getTrackFeatures(track_ids[i])
    track_list.append(track_data)
df = pd.DataFrame(track_list, columns = ['Name', 'Album', 'Artist', 'URL'])
df.to_csv('songs/disgusted.csv')
print("CSV Generated")

track_ids = getTrackIDs('spotify', music_dist[2])
track_list = []
for i in range(len(track_ids)):
    time.sleep(.3)
    track_data = getTrackFeatures(track_ids[i])
    track_list.append(track_data)
df = pd.DataFrame(track_list, columns = ['Name', 'Album', 'Artist', 'URL'])
df.to_csv('songs/fearful.csv')
print("CSV Generated")

track_ids = getTrackIDs('spotify', music_dist[3])
track_list = []
for i in range(len(track_ids)):
    time.sleep(.3)
    track_data = getTrackFeatures(track_ids[i])
    track_list.append(track_data)
df = pd.DataFrame(track_list, columns = ['Name', 'Album', 'Artist', 'URL'])
df.to_csv('songs/happy.csv')
print("CSV Generated")

track_ids = getTrackIDs('spotify', music_dist[4])
track_list = []
for i in range(len(track_ids)):
    time.sleep(.3)
    track_data = getTrackFeatures(track_ids[i])
    track_list.append(track_data)
df = pd.DataFrame(track_list, columns = ['Name', 'Album', 'Artist', 'URL'])
df.to_csv('songs/neutral.csv')
print("CSV Generated")

track_ids = getTrackIDs('spotify', music_dist[5])
track_list = []
for i in range(len(track_ids)):
    time.sleep(.3)
    track_data = getTrackFeatures(track_ids[i])
    track_list.append(track_data)
df = pd.DataFrame(track_list, columns = ['Name', 'Album', 'Artist', 'URL'])
df.to_csv('songs/sad.csv')
print("CSV Generated")

track_ids = getTrackIDs('spotify', music_dist[6])
track_list = []
for i in range(len(track_ids)):
    time.sleep(.3)
    track_data = getTrackFeatures(track_ids[i])
    track_list.append(track_data)
df = pd.DataFrame(track_list, columns = ['Name', 'Album', 'Artist', 'URL'])
df.to_csv('songs/surprised.csv')
print("CSV Generated")




# Regenerate CSV files for all emotions
for i in range(7):
    track_ids = getTrackIDs('spotify', music_dist[i])
    track_list = []
    for j in range(len(track_ids)):
        time.sleep(.3)
        track_data = getTrackFeatures(track_ids[j])
        track_list.append(track_data)
    df = pd.DataFrame(track_list, columns=['Name', 'Album', 'Artist', 'URL'])
    df.to_csv(f'songs/{emotion_dict[i].lower()}.csv', index=False)
    print(f"CSV Generated for {emotion_dict[i]}")

# Call regenerate_CSV() function when script is executed
if __name__ == "__main__":
    regenerate_CSV()

# track_ids = getTrackIDs('spotify',music_dist[0])
# track_list = []
# for i in range(len(track_ids)):
#     time.sleep(.3)
#     track_data = getTrackFeatures(track_ids[i])
#     track_list.append(track_data)
#     df = pd.DataFrame(track_list, columns = ['Name','Album','Artist']) # ,'Release_date','Length','Popularity'
#     df.to_csv('songs/angry.csv')
# print("CSV Generated")

# track_ids = getTrackIDs('spotify',music_dist[1])
# track_list = []
# for i in range(len(track_ids)):
#     time.sleep(.3)
#     track_data = getTrackFeatures(track_ids[i])
#     track_list.append(track_data)
#     df = pd.DataFrame(track_list, columns = ['Name','Album','Artist']) # ,'Release_date','Length','Popularity'
#     df.to_csv('songs/disgusted.csv')
# print("CSV Generated")

# track_ids = getTrackIDs('spotify',music_dist[2])
# track_list = []
# for i in range(len(track_ids)):
#     time.sleep(.3)
#     track_data = getTrackFeatures(track_ids[i])
#     track_list.append(track_data)
#     df = pd.DataFrame(track_list, columns = ['Name','Album','Artist']) # ,'Release_date','Length','Popularity'
#     df.to_csv('songs/fearful.csv')
# print("CSV Generated")

# track_ids = getTrackIDs('spotify',music_dist[3])
# track_list = []
# for i in range(len(track_ids)):
#     time.sleep(.3)
#     track_data = getTrackFeatures(track_ids[i])
#     track_list.append(track_data)
#     df = pd.DataFrame(track_list, columns = ['Name','Album','Artist']) # ,'Release_date','Length','Popularity'
#     df.to_csv('songs/happy.csv')
# print("CSV Generated")

# track_ids = getTrackIDs('spotify',music_dist[4])
# track_list = []
# for i in range(len(track_ids)):
#     time.sleep(.3)
#     track_data = getTrackFeatures(track_ids[i])
#     track_list.append(track_data)
#     df = pd.DataFrame(track_list, columns = ['Name','Album','Artist']) # ,'Release_date','Length','Popularity'
#     df.to_csv('songs/neutral.csv')
# print("CSV Generated")

# track_ids = getTrackIDs('spotify',music_dist[5])
# track_list = []
# for i in range(len(track_ids)):
#     time.sleep(.3)
#     track_data = getTrackFeatures(track_ids[i])
#     track_list.append(track_data)
#     df = pd.DataFrame(track_list, columns = ['Name','Album','Artist']) # ,'Release_date','Length','Popularity'
#     df.to_csv('songs/sad.csv')
# print("CSV Generated")

# track_ids = getTrackIDs('spotify',music_dist[6])
# track_list = []
# for i in range(len(track_ids)):
#     time.sleep(.3)
#     track_data = getTrackFeatures(track_ids[i])
#     track_list.append(track_data)
#     df = pd.DataFrame(track_list, columns = ['Name','Album','Artist']) # ,'Release_date','Length','Popularity'
#     df.to_csv('songs/surprised.csv')
# print("CSV Generated")