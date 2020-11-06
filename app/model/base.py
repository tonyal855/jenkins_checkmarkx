import json

class Base():

    def buildResult(self, message, data=None, status=None):
        result = {}
        result["message"] = message
        result['status'] = status
        if data:
            result["data"] = data
        return result
