# coding: utf-8

class Report(object):

    def __init__(self, title, text, formatter):
        self._title = title
        self._text = text
        self._formatter = formatter

    def output_report(self):
        self._formatter.output_report(self._title, self._text)


class Formatter(object):

    def output_report(self, title, text):
        assert False


class HTMLFormatter(Formatter):

    def output_report(self, title, text):
        print('<html>')
        print('<head>')
        print('<title>{}</title>'.format(title))
        print('</head>')
        print('<body>')
        for line in text:
            print("<p>{}</p>".format(line))
        print('</body>')
        print('</html>')


class PlainTextFormatter(Formatter):

    def output_report(self, title, text):
        print('*** {} ***'.format(title))
        for line in text:
            print(line)


class CallableReport(object):

    def __init__(self, title, text, formatter):
        self._title = title
        self._text = text
        self._formatter = formatter

    def output_report(self):
        self._formatter(self._title, self._text)


class CallableFormatter(object):

    def __init__(self, decoration='***'):
        self._decoration = decoration

    def __call__(self, title, text):
        print('{decoration}{content}{decoration}'.format(
            decoration=self._decoration,
            content=title)
        )
        for line in text:
            print(line)


if __name__ == '__main__':
    report = Report('月次報告', ['順調！', '最高です！'],
                    PlainTextFormatter())
    report.output_report()
    print('-' * 50)

    report = Report('月次報告', ['順調！', '最高です！'],
                    HTMLFormatter())
    report.output_report()
    print('-' * 50)

    report = CallableReport('月次報告', ['順調！', '最高です！'],
                    CallableFormatter())
    report.output_report()
