import os
import time
import yt_dlp  # https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py
from threading import Thread
from queue import Queue

from yt_concate.pipeline.steps.step import Step
from yt_concate.settings import VTT_DIR, CAPTIONS_DIR
from yt_concate.logger import logger


def get_ydl():
    # set options for yt-dlp
    # # https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py
    options = {
        'writesubtitles': True,
        'writeautomaticsub': True,
        'skip_download': True,  # 只下載字幕
        # 'subtitlesformat': 'srt', # nothing to do with this option
        'subtitleslangs': ['en'],
        # 'outtmpl': 'downloads\\captions\\vtt\\' + '%(id)s.%(ext)s',
        'outtmpl': VTT_DIR + '%(id)s.%(ext)s',  # use the video ID as the output filename
    }
    # Create a yt_dlp object and pass in the options
    return yt_dlp.YoutubeDL(options)


class Worker(Thread):
    def __init__(self, q: object, n: int):
        Thread.__init__(self)
        self.queue = q
        self.num = n
        self.ydl = get_ydl()  # 取得一個物件

    def run(self):
        while self.queue.qsize() > 0:  # 如果工作清單還有未完成的項目
            msg = self.queue.get()  # 那就繼續從工作清單中取出任務條
            self.ydl.download(msg)  # 執行一個下載的方法  msg = URL


class DownloadCaptions(Step):
    def process(self, data: list, inputs: dict, utils):
        # data is now YT object list
        logger.info("download captions ............")
        dl_list = []
        cap_no = 0
        exclude_id_list = self.get_exclude_ids(inputs['exclude_vid']) if os.path.exists(inputs['exclude_vid']) else []
        print(inputs['exclude_vid'])
        print(exclude_id_list)

        for yt in data:
            if yt.vid in exclude_id_list:  # 例外不下
                logger.debug(f"{yt.vid} is excluded. ")
                continue
            if yt.is_caption_files_exists():  # 存在不下
                logger.debug(f"{yt.caption_filepath} file exists. Skip.")
                cap_no += 1
            else:
                dl_list.append(yt.url)  # 剩下需要下載的才裝在這裡
        logger.info(f"Total {cap_no} caption files in {CAPTIONS_DIR}.")
        # input("Press any key ... ")
        logger.info("Below are video links not having captions files")
        logger.debug(dl_list)
        logger.info(f"Start to download all the other {len(dl_list)} files that donse not have subtitle.")

        my_queue = Queue()

        for dl_url in dl_list:
            my_queue.put([dl_url, ])

        # 建立 4 個 worker
        my_worker = []
        for i in range(4):
            my_worker.append(Worker(my_queue, i))

        # considering multi-threading here ...
        # Measure the execution time of a line of code
        start_time = time.time()
        for i in range(4):
            my_worker[i].start()

        # try:
        #     get_ydl().download(dl_list)
        # except:
        #     print('Error when downloading caption.')

        for i in range(4):
            my_worker[i].join()
        elapsed_time = time.time() - start_time
        logger.debug(f"The elapsed time is {elapsed_time}")

        return data

    # def check_caption_exists(self, filepath: str):
    #     check = os.path.exists(filepath) and os.path.getsize(filepath) > 0
    #     return check

    def get_exclude_ids(self, exclude_filepath):
        with open(exclude_filepath, 'r') as f:
            exclude_id_list = f.read().splitlines()
        return exclude_id_list
