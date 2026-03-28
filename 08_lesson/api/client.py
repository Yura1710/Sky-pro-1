import requests
from config import API_URL


class YouGileBaseClient:
    def __init__(self, token=None):
        self.base_url = API_URL
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })
        if token:
            self.session.headers.update({
                "Authorization": f"Bearer {token}"
            })

    def _request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(method, url, **kwargs)
        print(f"{method} {url} -> {response.status_code}")
        if response.status_code >= 400:
            return {"error": response.text, "status": response.status_code}
        return response.json() if response.text else {}
