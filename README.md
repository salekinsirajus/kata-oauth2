# Server (protected resource)

```
pip install -r requirements.txt

FLASK_DEBUG=1 FLASK_APP=hello.py flask run
```

# Client

```
curl --header 'Authorization: Bearer dca6f1125fb4874e058887a098dadf91f0e1e70d' 'http://127.0.0.1:5000/'
```
