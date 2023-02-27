# Insurance_Premium

```
conda create -p <env_name>
```

```
conda activate ins
```

```
git remote -v
```
BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname>
```
>Note: Image name for docker must be lower case

To list docker images
```
docker images
```
Run docker image
```
docker run -p 5000:5000(portnumber) -e PORT=5000 Imageid
```
TO STOP DOCKER CONTAINERS
```
docker stop <container_id>
```