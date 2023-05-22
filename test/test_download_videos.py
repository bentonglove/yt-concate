from unittest import TestCase
from yt_concate.pipeline.steps import DownloadVideos

import data_for_test as data


class TestDownloadVideos(TestCase):
    def test_process(self):
        d = DownloadVideos()
        found_list = d.process(data.found, None, None)
        for found in found_list:
            print(f"I need to get {found.yt.vid} time : {found.time}")
