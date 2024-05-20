# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===

# File: tests/test_app.py

"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'

# POST /sort-names
# names=Joe,Alice,Zoe,Julia,Kieran
#  Expected response (200 OK):

"""
#  Alice,Joe,Julia,Kieran,Zoe
"""
def test_post_sorted_names(web_client):
    response = web_client.post('/sorted-names', data={'names': 'Joe,Alice,Zoe,Julia,Kieran'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Joe,Julia,Kieran,Zoe'

# POST /sort-names
# names=Alice,Julia,Zoe,Joe,Kieran
#  Expected response (200 OK):
"""
#  Alice,Joe,Julia,Kieran,Zoe
"""
def test_post_partially_sorted_names(web_client):
    response = web_client.post('/sorted-names', data={'names': 'Alice,Julia,Zoe,Kieran'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Julia,Kieran,Zoe'

# POST /sort-names
# names=
#  Expected response Invalid response code:
"""
#  You didn't submit any names!
"""
def test_post_no_names(web_client):
    response = web_client.post('/sorted-names')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "You didn't submit any names!"

# GET /names?add=Eddie
#  Parameters:
#    name: Eddie
#  Expected response (200 OK):
"""
Julia, Alice, Karim, Eddie
"""
def test_add_eddie(web_client):
    response = web_client.post('/names', data={'names': 'Eddie, Farim'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice, Eddie, Farim, Julia, Karim'
