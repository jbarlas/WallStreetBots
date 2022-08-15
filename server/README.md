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
## `.env`
Ensure that there is a file `server/.env` which contains the following information:
```
# PRAW
client_secret=<client-secret-value>

# Firebase
firebase-config=<firebase-config-as-single-line-json>
```