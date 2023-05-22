from yt_concate.pipeline.steps.step import StepException
from yt_concate.utils import Utils


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs):
        data = None
        utils = Utils()
        for step in self.steps:
            try:
                data = step.process(data, inputs, utils)
            except StepException as e:
                print('Exception happened:', e)
                break
