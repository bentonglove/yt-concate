from yt_concate.logger import logger
from yt_concate.pipeline.steps.step import Step


class Preflight(Step):

    def process(self,  data, inputs, utils):
        logger.info('Preflight ............')
        logger.info('Create required folders for downloads and outputs.')
        utils.create_dirs()
