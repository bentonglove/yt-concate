from yt_concate.model.found import Found
from yt_concate.pipeline.steps.step import Step
from yt_concate.logger import logger


class Search(Step):

    def process(self, data: list, inputs, utils) -> list:
        logger.info("Search keyword...........")
        # data is a YT list
        # search_word = "incredible"
        search_word = inputs["search_word"]
        found = []
        for yt in data:
            captions = yt.captions
            if not captions:
                continue
            for caption in captions:
                if search_word in caption:
                    time = captions[caption]
                    found.append(Found(yt, caption, time))
                if len(found) >= inputs['limit']:
                    break  # 找到10個就停了吧
        return found
