# coding: utf-8

from abc import abstractmethod, ABCMeta

class Report(object):

    __metaclass__ = ABCMeta

    def __init__(self):
        self._title = '月次報告'
        self._text = ['順調', '最高']

    def output_report(self):
        self._output_start()
        self._output_head()
        self._output_body_start()
        self._output_body()
        self._output_body_end()
        self._output_end()

    def output_body(self):
        for line in self._text:
            self._output_line(line)

    @abstractmethod
    def _output_line(self, line):pass
    @abstractmethod
    def _output_start(self):pass
    @abstractmethod
    def _output_head(self):pass
    @abstractmethod
    def _output_body_start():pass
    @abstractmethod
    def _output_body_end(self):pass
    @abstractmethod
    def _output_end(self):pass


class PlainTextReport(Report):

    def _output_line(self, line):
        print(line)

    def _output_start(self):
        pass

    def _output_head(self):
        print('*** %s ***'.format(self._text))

    def _output_body_start():
        pass

    def _output_body_end(self):
        pass

    def _output_end(self):
        pass


if __name__ == '__main__':
    PlainTextReport().output_body()
