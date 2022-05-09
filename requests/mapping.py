class Mapping:
    def __init__(self):
        self._mapping = dict()

    def get(self):
        return self._mapping.copy()

    def set(self, pair):
        key, val = pair
        self._mapping[key] = val

    def reset(self):
        self._mapping.clear()

