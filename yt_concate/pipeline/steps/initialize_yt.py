from yt_concate.model.yt import YT
from yt_concate.pipeline.steps.step import Step
from yt_concate.logger import logger


class InitializeYT(Step):
    def process(self, data, inputs, utils) -> list:
        # data is an URL link list
        logger.info("Initilize YT objects")
        return [YT(url) for url in data]    # an YT obj list
