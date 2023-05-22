import os

# Abslute refernce. starting from the project base down through to the steps folder
from yt_concate.pipeline.steps import (Preflight, GetVideoList, InitializeYT, DownloadCaptions,
                                       Convert2Srt, ReadCaption, Search, DownloadVideos, EditVideo)
# Relative reference. meaning pipeline folder.
from pipeline import Pipeline
# relative reference. meaning setting.py file
from settings import SupercarBlondie_CID, Google_API_Key, DOWNLOADS_DIR

info = {'api_key': Google_API_Key,
        'channel_id': SupercarBlondie_CID,
        'exclude_vid': os.path.join(DOWNLOADS_DIR, "exclude_vid.txt"),
        'search_word': 'incredible',
        'limit': 10,
        }


def main():
    steps = [
        Preflight(),
        GetVideoList(),         # -> a video URL list
        InitializeYT(),         # -> an YT obj list
        DownloadCaptions(),     # -> data keep. Donwload captions to a dir
        Convert2Srt(),          # -> data keep
        ReadCaption(),          # -> YT obj list and upload the caption into it
        Search(),               # -> Found obj list
        DownloadVideos(),       # -> data keep. Download videos to a dir
        EditVideo(),            # -> None. Combine videos.
    ]

    p = Pipeline(steps)
    p.run(info)


if __name__ == '__main__':
    main()
