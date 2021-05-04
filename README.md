# vital-python

The official Python Library for [Vital API](https://docs.tryvital.io)


# Install
```
pip install vital
```

# Calling Endpoints

```
from vital import Client

# Available environments are 'sandbox', 'development', and 'production'.
client = Client(client_id='***', secret='***', environment='sandbox')
```

# Supported Endpoints

```
<!-- Dates have to be url encoded -->
start_date =  urllib.parse.quote((datetime.now()-timedelta(days=1)).isoformat())
end_date =  urllib.parse.quote(datetime.now().isoformat())

client.LinkToken.create(user_key="user_key")
client.Body.get(user_key=**,start_date, end_date)
client.Activity.get(user_key=**,start_date, end_date)
client.Sleep.get(user_key=**,start_date, end_date)
client.SourceSpecific.get(user_key=**,start_date, end_date)
client.User.create(client_user_id=**)
client.User.providers(user_key=**)
client.User.get(client_user_id=**)
```


# Installing locally 
```
poetry build --format sdist
tar -xvf dist/*-`poetry version -s`.tar.gz -O '*/setup.py' > setup.py
```