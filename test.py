import requests
import json

accesstoken = None

def authorization():
    url = "https://accounts.spotify.com/api/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        'grant_type': 'client_credentials',
        'client_id': '4bccc573832b4cb2b9934b5d2af6cadf',
        'client_secret' : "f41c73aa5eb14aa4883f329ecc0717d5"
    }
    authr = requests.post(url=url,headers=headers,data=data)
    accesstoken = json.loads(authr.text)
    return accesstoken

def get_artist(accesstoken):
    url = 'https://api.spotify.com/v1/artists/0TnOYISbd1XYRBk9myaseg'
    headers = {"Authorization":'Bearer {}'.format(accesstoken)}
    response = requests.get(url=url,headers=headers)
    return response.text

if __name__ == "__main__":
    accesstoken = authorization()
    artist_name = input("Enter artist name:")
    header={"Authorization":"Bearer {}".format(accesstoken['access_token'])}
    url = 'https://api.spotify.com/v1/search?q={}&type=artist'.format(artist_name)
    response = requests.get(url=url,headers=header)
    response = json.loads(response.text)
    for count,artist in enumerate(response["artists"]['items']):
        print(count+1,artist['name'])
    choice = int(input("Choose artist enumeration: "))
    # print(response["artists"]["items"][choice-1])
    # artist_details = get_artist(accesstoken['access_token'])
    artistid = response["artists"]["items"][choice-1]['uri'].split(':')[2]
    url = "https://api.spotify.com/v1/artists/{}/top-tracks?market=GB".format(artistid)
    response = requests.get(url=url,headers=header)
    response = json.loads(response.text)
    # print(response)
    songids = ''
    for songs in response['tracks']:
        print(songs["name"])
        songids = songids + songs['id'] + "," 
    print(songids)
    url = "https://api.spotify.com/v1/audio-features?ids={}".format(songids)
    response = requests.get(url=url,headers=header)
    print(response.text)