import os
from .make_file import Makefile


class OnlineCompile(object):

    def __init__(self, code_str, lang, file_name, lesson_id):
        self._code_str = code_str
        self._lang = lang
        self._lesson_id = lesson_id

        make_file = Makefile(code_str, lang, file_name)
        make_file.make_file()

        self._file_path_dict = {
            "cpp": "/runfiles/%s.cpp" % file_name,
            "c": "/runfiles/%s.c" % file_name,
            "python": "/runfiles/%s.py" % file_name,
        }
        _file_path = os.path.dirname(os.path.abspath(__file__)) + self._file_path_dict[self._lang]

        self._lang_dict = {
            "cpp": "g++ %s -o %s && %s" % (_file_path, make_file.file_name, make_file.file_name),
            "c": "gcc %s -o %s && %s" % (_file_path, make_file.file_name, make_file.file_name),
            "python": "python %s" % _file_path,
        }

        self.run_cmd = self._lang_dict[self._lang]

    def run_code(self):
        return os.popen(self.run_cmd).read()

    def result(self):
        return self.run_code()
