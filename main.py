import requests


def get_data(url: str):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
    except Exception as e:
        print(e)

    return None
