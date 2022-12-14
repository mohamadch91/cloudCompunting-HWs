# Step one

In this step we will create a simple Docker image that will contain a CURL command line tool to send a request to the google.com website.
then we will upload the image to the docker hub.
pull  the image from the docker hub and create container from it.

run the container and send a request to the google.com website.

- [Step one](#step-one)
  - [1.1 Dockerfile](#11-dockerfile)
    - [Results](#results)
  - [1.2 Push image to docker hub](#12-push-image-to-docker-hub)
    - [Results](#results-1)
  - [1.3 Pull image from docker hub](#13-pull-image-from-docker-hub)
    - [1.3.1](#131)
    - [Results](#results-2)
    - [1.3.2](#132)
    - [Results](#results-3)


## 1.1 Dockerfile

first we need too create Dockerfile with alpine base image and install curl package.

```Dockerfile
FROM alpine:latest
RUN apk add --update curl
ENTRYPOINT ["curl"]
```
### Results

- [Dockerfile](./Dockerfile)
## 1.2 Push image to docker hub

now we need to push the image to the docker hub.

```bash
docker build -t curl .
docker tag curl:latest mohamadch91/curl:latest
docker push mohamadch91/curl:latest
```
### Results
![Builded image](./images/build.png)

![Push image](./images/push.png)

## 1.3 Pull image from docker hub

now we need to pull the image from the docker hub and create container from it.

### 1.3.1

since we have image on local , delete image from local 

```bash
docker rmi mohamadch91/curl:latest
```
### Results
![Remove local image](./images/remove.png)

then we pull the image and run it
    
### 1.3.2 

```bash
docker pull mohamadch91/curl:latest
docker run -it --name curl mohamadch91/curl:latest google.com
```
### Results
![pull image](./images/pull-images.png)

![run google.com](./images/curl-google.png)

![run no redirect](./images/curl-google-no.png)

![run aut](./images/curl-aut.png)

![ terminal](./images/terminal.png)