# get all video list from a YouTube channel

# pip install google-api-python-client
# import google.auth.credentials
from googleapiclient.discovery import build
from settings import Google_API_Key

CHANNEL_ID = 'UC4JX40jDee_tINbkjycV4Sg'  # TechWithTim


def get_all_video_in_channel(channel_id):
    api_key = Google_API_Key
    youtube = build('youtube', 'v3', developerKey=api_key)
    videos = []
    next_page_token = None

    while True:
        request = youtube.search().list(
            part='id,snippet',
            channelId=channel_id,
            maxResults=50,
            pageToken=next_page_token,
            type='video'
        )
        response = request.execute()

        videos += response['items']

        if 'nextPageToken' in response:
            next_page_token = response['nextPageToken']
        else:
            break
    return videos


videos_list = get_all_video_in_channel(CHANNEL_ID)

# print the video titles
for video in videos_list:
    print(video['snippet']['title'])

print(len(videos_list))
