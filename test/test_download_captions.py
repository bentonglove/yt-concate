from unittest import TestCase
from yt_concate.pipeline.steps import DownloadCaptions

import data_for_test as data


class TestDownloadCaptions(TestCase):
    def test_process(self):
        dc = DownloadCaptions()

        dc.process(data.yt_list, None, None)
