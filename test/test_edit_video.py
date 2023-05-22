from unittest import TestCase
from yt_concate.pipeline.steps import EditVideo

import data_for_test as data


class TestEditVideo(TestCase):
    def test_process(self):
        d = EditVideo()
        found_list = d.process(data.found, None, None)
        # data is a found list which has the video filepath needed to be merged
        print(f"The file is concatenent.")
