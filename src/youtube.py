from youtube_api import YouTubeDataAPI
import json

api_key = json.load(open("../data/api.json"))["apiKey"]
yt = YouTubeDataAPI(api_key)

def search(searchQuery: str) -> list:
    searches = yt.search(q=searchQuery, max_results=5)
    print("Retrieved: " + searches[0]["video_title"])
    return searches

coolThing = search("disturbed down with the sickness")