
# {{ NAME }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# EXAMPLE


POST /sort-names
names: a list of names no spaces seperated by commas

```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# EXAMPLE

# POST /sort-names
# names=Joe,Alice,Zoe,Julia,Kieran
#  Expected response (200 OK):

"""
#  Alice,Joe,Julia,Kieran,Zoe
"""

# POST /sort-names
# names=Alice,Julia,Zoe,Joe,Kieran
#  Expected response (200 OK):
"""
#  Alice,Joe,Julia,Kieran,Zoe
"""

# POST /sort-names
# names=
#  Expected response Invalid response code:
"""
#  You didn't submit any names!
"""

# GET /names?add=Eddie
#  Parameters:
#    name: Eddie
#  Expected response (200 OK):
"""
Julia, Alice, Karim, Eddie
"""

# POST /submit
#  Parameters: none
#  Expected response (400 Bad Request):
"""
Please provide a name and a message
"""
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /home
  Expected response (200 OK):
  "This is my home page!"
"""
def test_get_home(web_client):
    response = web_client.get('/home')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'This is my home page!'

"""
POST /submit
  Parameters:
    name: Leo
    message: Hello world
  Expected response (200 OK):
  "Thanks Leo, you sent this message: "Hello world""
"""
def test_post_submit(web_client):
    response = web_client.post('/submit', data={'name': 'Leo', 'message': 'Hello world'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Leo, you sent this message: "Hello world"'
```

