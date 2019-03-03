import os

class Makefile(object):

    def __init__(self, code_str, lang, file_name):
        self._code_str = code_str
        self._lang = lang
        self.file_name = file_name

        self._lang_dict = {
            "cpp": "/runfiles/%s.cpp" % self.file_name,
            "c": "/runfiles/%s.c" % self.file_name,
            "python": "/runfiles/%s.py" % self.file_name,
        }

    def make_file(self):
        run_path = os.path.dirname(os.path.abspath(__file__)) + self._lang_dict[self._lang]
        run_file = open(run_path, "w")
        run_file.write(self._code_str)
