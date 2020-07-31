from abc import ABC, abstractmethod


class Website(ABC):
    def __init__(self, url, classname):
        self._url = url
        self._classname = classname

    @abstractmethod
    def get_all_jobs(self):
        pass

    def get_jobs(self):
        pass
