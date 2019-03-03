class Chatmanager(object):
    def __init__(self):
        self._msg = []
        self._index = 0

    def add_msg(self, msg):
        print(msg, self._index)
        self._msg.append(msg)
        self._index += 1

    def get_last_msg(self):
        return self._msg[self._index - 1]

    def is_outdated(self, index):
        return self._index > index
