import urllib.request
import json
import os
import time

from yt_concate.pipeline.steps.step import Step, StepException
from yt_concate.logger import logger


class GetVideoList(Step):

    def process(self, data, inputs: dict, utils) -> list:
        # data is empty
        logger.info('get video list ............')

        channel_id = inputs['channel_id']

        # if the saved video_links_file exists, then return the vidoe url list to the next step
        if utils.video_list_file_exists(channel_id):   # i.e. UCKSVUHI9rbbkXhvAXK-2uxA.txt
            logger.debug(f"Found existing video url list file of channel id: {channel_id}")
            return self.read_file(utils.get_video_list_filepath(channel_id))

        logger.debug('Current working directory:', os.getcwd())
        logger.info(f"{channel_id}.txt does not exist.")

        logger.info("get video_links_list from the YouTube channel")
        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'
        page_items = 50
        first_url = f"{base_search_url}key={inputs['api_key']}&channelId={inputs['channel_id']}&part=snippet," \
                    f"id&order=date&maxResults={page_items}"
        video_links_list = []
        url = first_url

        logger.debug('Query from YouTube channel for the video list...')
        # considering multi-threading here ...
        start_time = time.time()
        while True:
            logger.debug(f"query from {url}")
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)
            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links_list.append(base_video_url + i['id']['videoId'])
            try:
                next_page_token = resp['nextPageToken']
                url = f"{first_url}&pageToken={next_page_token}"
            except KeyError:
                message = KeyError
                if message:
                    raise StepException(message)
                break
        elapsed_time = time.time() - start_time
        logger.debug(f'The elapsed time to get video list is {elapsed_time}')

        self.write_to_file(video_links_list, utils.get_video_list_filepath(channel_id))
        return video_links_list

    def read_file(self, video_links_file: str) -> list:
        # read video_links_list from the saved file
        with open(video_links_file, 'r') as f:
            video_links_list = f.read().splitlines()
        return video_links_list

    def write_to_file(self, video_links_list: list, filepath: str):
        # write video_links_list to the saved file
        with open(filepath, 'w') as f:
            for item in video_links_list:
                f.write(f"{item}\n")
        return None
