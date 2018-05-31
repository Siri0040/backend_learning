## Install Docker
Refer https://docs.docker.com/install/

## Tutorial 1

```text
docker build -t python_tut_v1:2.7.15 .
docker run -it --rm --name python_tut_v1 python_tut_v1:2.7.15
```


## Tutorial 2

```text
docker build -t python_tut_v2:2.7.15 .
docker run -it --rm --name python_tut_v2 python_tut_v2:2.7.15
```


## Tutorial 3

```text
docker build -t python_tut_v3:2.7.15 .
docker run -p 8888:8888 -it --rm --name python_tut_v3 python_tut_v3:2.7.15 
```

Open <IP>:8888 to access the notebook




