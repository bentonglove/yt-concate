from abc import abstractmethod, ABCMeta


class Step(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def process(self, data, inputs, utils):
        pass


class StepException(Exception):
    pass
