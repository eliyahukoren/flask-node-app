# Deploy flask app to the heroku
View app on the [web](https://eli-flask-note.herokuapp.com/)

## Steps

1. Create app on heroku

2. Create github/Gitlab or any other repository


### Local run:

```
git remote set-url origin [repository URL]

docker-compose build

docker-compose up
```

[Local App](http://127.0.0.1:8000)

### Deploy to heroku:

```
git remote set-url origin [Heroku URL]

git push
```