import os
from yt_concate.settings import CAPTIONS_DIR, VIDEOS_DIR
from yt_concate.utils import Utils


class YT:
    def __init__(self, url):
        self.url = url
        self.vid = self.extract_id_from_url()
        self.caption_filepath = self.caption_filepath()
        self.video_filepath = self.video_filepath()
        self.captions = None

    def extract_id_from_url(self):
        return self.url.split("watch?v=")[-1]

    def caption_filepath(self):
        return os.path.join(CAPTIONS_DIR, self.vid+'.en.srt')

    def is_caption_files_exists(self) -> bool:
        filepath = self.caption_filepath
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0

    def video_filepath(self):
        return os.path.join(VIDEOS_DIR, self.vid + '.mp4')

    def __str__(self):
        return f"<YTobj~ id = {self.vid}>"

    def __repr__(self):
        content = ' : '.join([
            'vid = ' + str(self.vid),
            'caption_filepath = ' + str(self.caption_filepath),
            'video_filepath = ' + str(self.video_filepath),
        ])
        return f"<YTobj~ {content}>"

