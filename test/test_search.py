import os
from unittest import TestCase

from yt_concate.pipeline.steps import Search
from yt_concate.pipeline.steps import ReadCaption
import data_for_test as data


class TestSearch(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        DUT_HOME = 'D:\\60.workspace\\14.Python\\50.hahow\\yt-concate\\yt_concate'
        os.chdir(DUT_HOME)

    def test_process(self):
        # rd = ReadCaption()
        # d = rd.process(data.yt_list, None, None)

        s = Search()
        d = data.yt_list2
        f_list = s.process(d, None, None)
        print(f_list)
        print(f_list[0])
        # for i in range(len(f_list)):
        #     print(f"{f_list[i]}")
