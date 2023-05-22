import os

from yt_concate.pipeline.steps.step import Step
from yt_concate.logger import logger


class ReadCaption(Step):
    def process(self, data: list, inputs, utils) -> list:
        logger.info("Read caption files ......")
        # data is a YT list
        for yt in data:
            if not os.path.exists(yt.caption_filepath):  # if it is not a file, then move to the next
                continue
            captions = {}
            with open(yt.caption_filepath, 'r') as f:
                time_line = False
                caption = None
                time = None
                for line in f:
                    line = line.strip()
                    if '-->' in line:  # the line with this significat string is identified as the timeline
                        time_line = True
                        time = line
                        continue
                    if time_line:  # obvioudly the next line after timeline must be the subtitle
                        caption = line
                        captions[caption] = time
                        time_line = False  # this is a toggle flag
            yt.captions = captions
        return data  # return a YT list
