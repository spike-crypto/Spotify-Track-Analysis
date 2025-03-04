import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import matplotlib.pyplot as plt
import re

# Am setting up client credentials here
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials( 
    client_id='b57fac04e5894fdc80aa7a2557e9cb5f', 
    client_secret='fc2b1de953414776aa559deedffd5058'                                                                                          
))
# am fetching track details by URL
track_url = "https://open.spotify.com/track/0FIDCNYYjNvPVimz5icugS"
track_id = re.search(r'track/([a-zA-Z0-9]+)', track_url).group(1)
track = sp.track(track_id)
print(track)

#Extract meta data
track_data = {
    'Track Name' : track['name'],
    'Artist' : track['artists'][0]['name'],
    'Album' : track['album']['name'],
    'popularity' : track ['popularity'],
    'Duration (minutes)' : track['duration_ms']/60000
}

#diplaying track metadata
print(f"\nTrack Name:{track_data['Track Name']}")
print(f"Artist:{track_data['Artist']}")
print(f"Album:{track_data['Album']}")
print(f"popularity:{track_data['popularity']}")
print(f"Duration:{track_data['Duration (minutes)']:.2f}minutes")

#coverting meta data to data frame
df = pd.DataFrame([track_data])
print("\nTrack Data as DataFrame:")
print(df)

#save meta data in csv file
df.to_csv(path_or_buf="C:\\Users\\balam\\OneDrive\\Desktop\\spotify_track_data.csv", index=False)



# visualization
features = ['popularity','Duration(minutes)']
values = [track_data['popularity'],track_data['Duration (minutes)']]

plt.figure (figsize=(8,5))
plt.bar(features,values,color='skyblue',edgecolor='black')
plt.title(f"Track Metadata for{track_data['Track Name']}")
plt.ylabel('Value')
plt.show()