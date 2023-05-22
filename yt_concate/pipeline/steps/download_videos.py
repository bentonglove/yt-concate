import os

from yt_concate.pipeline.steps.step import Step
import yt_dlp
from yt_concate.logger import logger


class DownloadVideos(Step):

    def process(self, data: list, inputs, utils):  # data is a found list
        logger.info("Download video files .....")
        # use set to clean the duplicate ones
        found_yt_set = set([found.yt for found in data])

        download_no = 0
        for yt in found_yt_set:
            print(yt)
            if os.path.exists(yt.video_filepath):  # 如果已經存在，就看下一支
                logger.info(f"{yt} file exists.")
                continue

            self.download_video(yt.url)
            download_no += 1
            if download_no > 10:  # 超過10支影片 就不要下載了
                break
        return data  # 要從 found物件裡面擷取 video clips

    def download_video(self, url: str) -> None:
        # the description for options
        # https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L184
        options = {
            'format': 'mp4',
            'outtmpl': 'downloads\\videos\\' + '%(id)s.%(ext)s',  # use the video ID as the output filename
        }
        # Create a yt_dlp object and pass in the options
        ydl = yt_dlp.YoutubeDL(options)
        # try:
        ydl.download([url])
        # except:
        #     print('Error when downloading caption.')
        return None
