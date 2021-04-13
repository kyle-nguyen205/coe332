#Homework 5

## Part A
The file used to create the pod is name-pod.yml. The command used to create the pod is:
```
>>> kubectl apply -f name-pod.yml
```

The command used to get the pod and its output is:
```
>>> kuebctl get pods --selector "greeting"
NAME         READY   STATUS    RESTARTS   AGE
hello-name   1/1     Running   0          52s
```

Checking the logs:
```
>>> kubectl logs hello-name
Hello,
```
The expected result was "Hello, $Name" but it seems like the $Name is blank until defined.

The commad used to delete the pod is:
```
>>> kubectl delete pods hello-name
```

## Part B
The existing file name-pod.yml was modified to add the environment variables. The new file is named name-pod-env.yaml. To create the pod:
```
>>> kubectl apply -f name-pod-env
```

Checking the logs:
```
>>> kubectl logs hello-name-env
Hello, Kyle
```

To delete the pod:
```
>>> kubectl delete pods hello-name-env
```
## Part C
The file used to create the deployment is name-deployment-env.yml. To create the deployment:
```
>>> kubectl apply -f name-deployment-env.yml
```

To get all the pods in the deployment and their IP addresses:
```
>>> kubectl get pods -o wide
NAME                                           READY   STATUS              RESTARTS   AGE    IP              NODE                         NOMINATED NODE   READINESS GATES
hello-name-deployment-5c56dc76f4-2zxhs         1/1     Running             0          5m     10.244.5.100    c04                          <none>           <none>
hello-name-deployment-5c56dc76f4-4ghbf         1/1     Running             0          5m     10.244.6.141    c03                          <none>           <none>
hello-name-deployment-5c56dc76f4-txfj7         1/1     Running             0          5m     10.244.7.97     c05                          <none>           <none>
```

Checking the logs:
```
>>> kubectl logs hello-name-deployment-5c56dc76f4-2zxhs
Hello, Kyle from 10.244.5.100
>>> kubectl logs hello-name-deployment-5c56dc76f4-4ghbf
Hello, Kyle from 10.244.6.141
>>> kubectl logs hello-name-deployment-5c56dc76f4-txfj7
Hello, Kyle from 10.244.7.97
```    
