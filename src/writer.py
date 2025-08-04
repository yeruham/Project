import json


class Writer:

    @staticmethod
    def write_json(url, data):
        with open(url, 'w') as f:
            json.dump(data, f)