from unittest import TestCase


# sys.path.append("D:\\60.workspace\\14.Python\\50.hahow\\yt-concate")
# sys.path.append("..")
# os.chdir("D:\\60.workspace\\14.Python\\50.hahow\\yt-concate\\yt_concate")
# rootDir = os.path.abspath('..\\..')
# sys.path.insert(0, rootDir)
from yt_concate.pipeline.steps import InitializeYT

import data_for_test as data


class TestInitializeYT(TestCase):
    def test_process(self):
        obj_list = InitializeYT().process(data.sample_url, None, None)
        print(obj_list)
        self.assertEqual(obj_list[0].url, data.sample_url[0])
        self.assertEqual(obj_list[0].vid, '3SoRlkMS2lQ')
        self.assertEqual(obj_list[0].caption_filepath, 'downloads\\captions\\3SoRlkMS2lQ.en.srt')
