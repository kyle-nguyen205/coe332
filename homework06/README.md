# Homework 6

This homework covers using Kubernetes to set up multiple deployments and services. 

## Step 1

First, a Persistent Volume Claim (PVC) is created.
```
>>> kubectl apply -f kn8435-test-redis-pvc.yml

```

## Step 2

The deployment for the Redis database is then created with a volumeMount associated with the PVC in step 1.
```
>>> kubectl apply -f kn8435-test-redis-deployment.yml
```

## Step 3

The service for the Redis databse is finally created.
```
>>> kubectl apply -f kn8435-test-redis-service.yml
```
At this point, you can verify if the database is working properly by spinning up a debug deployment and running some commands inside.
```
>>> kubectl apply -f deployment-python-debug.yml
>>> kubectl exec -it <deployment pod name> /bin/bash
>>> [pod] pip install redis
>>> [pod] python3
>>> [pod] [python3] 
> import redis
> rd = redis.StrictRedis(host=<Redis service IP>, port=6379, db=0)
> rd.set('key1', 'hw6_test')
TRUE
> rd.get('key1')
b'hw6_test'
```
If we open up another shell window and delete the redis pod, a new one will be created that maintains the same redis database. Repeating the rd.get command will show the same b'hw6_test' value.

## Step 4

For convenience, the kdnguyen205/hw3 image from dockerhub will be used. Create the flask deployment.
```
>>> kubectl apply -f kn8435-test-flask-deployment.yml
```

### Step 5

Finally, a service for the flask app will be created.
```
>>> kubectl apply -f kn8435-test-flask-service.yml
```
Note that the flask app has not been tested to work on Kubernetes since that is outside the scope of this homework, but all deployments and services can be properly created.
