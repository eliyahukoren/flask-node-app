# Deploy django app in docker image to the heroku



Youtube link to [Deploy Django image to heroku](https://www.youtube.com/watch?v=Oy71OgKZbOQ)

View app on the [web](https://eli-simple-django-app.herokuapp.com/)

## Steps

1. docker build -t django-mysite:v1 .
2. docker run -p 8000:8000 django-mysite:v1
3. docker tag django-mysite:v1 elik0ren/django-mysite
4. docker push elik0ren/django-mysite
5. create app on heroku
6. change Docker file, uncomment for heroku deploy
7. heroku container:push web -a=eli-simple-django-app
8. heroku container:release -a eli-simple-django-app web


>Helpers
```
git remote rename heroku origin
git remote set-url origin https://github.com/eliyahukoren/simple-django-heroku.git
git remote set-url origin https://git.heroku.com/eli-flask-simple-app.git
docker tag django-mysite:v1 elik0ren/django-mysite
docker images
docker push elik0ren/django-mysite
```


heroku [doc](https://devcenter.heroku.com/articles/local-development-with-docker-compose#pushing-your-containers-to-heroku
)

heroku [doc](https://devcenter.heroku.com/articles/build-docker-images-heroku-yml)


Youtube [docker push](https://www.youtube.com/watch?v=EIHY_CY5J0k)