# WallStreetBots

## Description
r/WallStreetBets sentiment analysis bot with web UI

## Heroku
This app is deployed to heroku in seperate heroku apps named `wallstreetbots-client` and `wallstreetbots-client` on branches `heroku-server` and `heroku-client`, respectively. 

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
heroku logs --tail --app my-app
```
### To delete a branch:
```
git remote rm <branch-name>
```
