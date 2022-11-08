### TEST FLINK
___
if you need to run this project, you should  to follow the next steps
* first is needed to install docker
* after install docker it's recommended to install docker-compose

later you install docker and docker-compose, we need to run the next command

```shell
docker-compose up -d
```

this command run the api and the database services in your machine

if you want to track the logs you can run the next command

```shell
docker logs -f <container-name>
```
this command allows to track the logs in our project

#### POSTMAN collection

if you want to know how to use the api, you can go to the documentation of postman

[POSTMAN](https://documenter.getpostman.com/view/148100/2s8YYPGKiE)

run migrations:
```shell
docker exec -ti <container-name> python manage.py makemigrations
```


```shell
docker exec -ti <container-name> python manage.py migrate
```

The project is prepared to deploy a Kubernetes environment, Feel free to try it!
```shell
kubectl apply -f ./k8s
```
###### the project runs in digitalocean cluster


#### WEB APP
https://webflink.petwarn.me

#### API
https://test.petwarn.me/company/