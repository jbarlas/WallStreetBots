# Server
## Setup

### Installation
#### Virtual Environemnt
Install the virtual environment using:
```bash
python -m venv /path/to/new/virtual/environment
```
(Windows) Activate the virtual environment:
```bash
source venv/Scripts/Activate
```

#### Praw Bot
Log into your Reddit account and create a new app [here](https://www.reddit.com/prefs/apps) and input the information generated from the application into a file `PRAW/secret.py`:
##### Read Only
```
reddit = praw.Reddit(client_id="",      # your client id
                    client_secret="",   # your client secret
                    user_agent="")      # your user agent

``` 
##### Authorized
```
reddit_authorized = praw.Reddit(client_id="",       # your client id
                                client_secret="",   # your client secret
                                user_agent="",      # your user agent
                                username="",        # your reddit username
                                password="")        # your reddit password
```