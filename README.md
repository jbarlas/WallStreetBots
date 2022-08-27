# WallStreetBots

## Description
r/WallStreetBets sentiment analysis bot with web UI

## Heroku
This app is deployed to heroku in seperate heroku apps named `wallstreetbots-client` and `wallstreetbots-client` on branches `heroku-server` and `heroku-client`, respectively. 

## Adding remote branches
```
git remote add heroku-server https://git.heroku.com/my-app-server
git remote add heroku-client https://git.heroku.com/my-app-client
```
### To push changes to server:
```
git subtree push --prefix server heroku-server master
```
### To push changes to client:
```
git subtree push --prefix client heroku-client master
```
### To view deployment logs:
```
heroku logs --tail --remote <branch-name>
```
### To delete a branch:
```
git remote rm <branch-name>
```
