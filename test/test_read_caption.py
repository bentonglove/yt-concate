import unittest

import os
import sys

import data_for_test as data

sys.path.append("D:\\60.workspace\\14.Python\\50.hahow\\yt-concate")
# sys.path.append("..")
# os.chdir("D:\\60.workspace\\14.Python\\50.hahow\\yt-concate\\yt_concate")
# rootDir = os.path.abspath('..\\..')
# sys.path.insert(0, rootDir)
from yt_concate.pipeline.steps import ReadCaption


class TestReadCaption(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        DUT_HOME = 'D:\\60.workspace\\14.Python\\50.hahow\\yt-concate\\yt_concate'
        os.chdir(DUT_HOME)

    def test_process(self):
        print('test1')
        rd = ReadCaption()
        d = rd.process(data.yt_list, None, None)
        n = 0
        for k in d:
            n += 1
            print(f"\n {n}. {k.vid}")
            print(k.captions)

        print(f"there are {n} captions.")

    def test_2(self):
        print('test2')


if __name__ == "__main__":
    unittest.main()
