import requests


def create_instance(id, api_key):
    """A python function for creating instances of gpus on the vastai platform"""

    url = f"https://console.vast.ai/api/v0/asks/{id}/?api_key={api_key}"


    payload = """{
        "client_id": "me",
        "image": "bobsrepo/pytorch:latest",
        "env": {
            "TZ": "UTC"
        },
        "price": 0.5,
        "disk": 20,
        "label": "my-instance",
        "extra": null,
        "onstart": null,
        "runtype": "ssh",
        "image_login": "-u bob -p 9d8df!fd89ufZ docker.io",
        "python_utf8": false,
        "lang_utf8": false,
        "use_jupyter_lab": false,
        "jupyter_dir": null,
        "create_from": null,
        "force": false
    }"""


    headers = {
        'Accept': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)