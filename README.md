#### Note
All the problems I've implemented in Python as currently use Python mostly.

#### Problem 1
To run the program python3 should be installed
```
python3 probelem1.py

press return key. Now provide inputs and press control + d
```

#### Probelm 2
To run the program python3 should be installed
```
python3 probelem2.py

press return key. Now provide inputs and press control + d
```


#### Probelm 3
Problem 3, I've used Flask to implement rest api.
To run the application locally
```
docker build -t calc:0.1 .

docker run -p 5000:5000 calc:0.1
```

#### In production environment
We can run this docker image on kubernetes and istio injection enabled on the namespace.
We can utilize envoy's rate limiting, authN/authZ, mutual TLS and other policies.
So that we don't have to implement cross cutting concerns in api development along with business logic.

#### Thing we can improve
If this api is public api for inside organization or outside organization we can add Open API Spec docs.
Based on load testing we can choose framework and implement this in way so that it can scale quickly.
