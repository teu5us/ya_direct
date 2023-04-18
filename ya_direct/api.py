from tortilla import Wrap

def create(access_token: str, clid: str, refresh_token: str = '', lang='', sandbox: bool = False, **options):
    url = f'https://api.direct.yandex.com/json/v5'
    if sandbox:
        url = f'https://api-sandbox.direct.yandex.com/json/v5'
    wrapper = Wrap(part=url, **options)
    wrapper.config.headers['Accept'] = 'application/json'
    wrapper.config.headers['Authorization'] = f'Bearer {access_token}'
    wrapper.config.headers.update({
        'Accept-Language': lang,
        "Client-Login": clid,
    })
    return wrapper
    