import jsons
import requests

class MakeRequest:

    @classmethod
    def post(cls, url, data, headers={}, options={}, auth=()):
        headers = { 'Content-Type': 'application/json', }
        response = requests.post(url=url, json=jsons.dump(data), auth=auth, headers=headers)
        return response
    
    @classmethod
    def get(cls, url, headers={}, options={}, auth=()):
        headers = { 'Content-Type': 'application/json', }
        response = requests.get(url=url, auth=auth, headers=headers)
        return response