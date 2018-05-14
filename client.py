from authlib.client import OAuthClient
import requests


# TODO: update
client = OAuthClient(
    client_id='',
    client_secret='',
    api_base_url='https://api.github.com/',
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize',
    client_kwargs={'scope': 'user:email'},
)


# TODO: uncomment
#token = client.fetch_access_token(grant_type='client_credentials')
#print(token)


# TODO: remove
fake_token = {
    'access_token': 'dca6f1125fb4874e058887a098dadf91f0e1e70d',
    'token_type': 'bearer',
    'scope': 'user:email'
}


r = requests.get('http://127.0.0.1:5000/', headers={'Authorization': 'Bearer {access_token}'.format(**fake_token)})
print()
print(r.text)
print()
r.raise_for_status()
