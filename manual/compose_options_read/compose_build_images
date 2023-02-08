## BUILD vs IMAGES
---
### * Build
The build option means make a image from dockerfile and run container from image made by image which is made the beforestep.

- ex)
```
nginx:
    container_name: compose_nginx
    build: ./nginx
    restart: always
```
it makes image from dockerfile located in path *./nginx*
and run container using it

### * image
The image option means make a containger using image.

- ex)
```
nginx:
    container_name: compose_nginx
    image: djangoweb/nginx
    restart: always
```
it uses the image named djangoweb/nginx to run container.


