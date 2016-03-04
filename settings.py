import json


def get_secret(api, secret):
    """
    Return
    Args:
        api: asd
        secret: asd
    return: asd
    """
    with open("secrets.json") as f:
        content = f.read()
    return json.loads(content).get(api).get(secret)


SLACK = {
    'token': get_secret(api='slack', secret='token')
}

SHARE_TRIGGER = "@share"
