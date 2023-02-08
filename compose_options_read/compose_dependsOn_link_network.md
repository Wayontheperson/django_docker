### * depends on
it is a keyword to set the _**order**_ in which services must start and stop.

For example, suppose we want our web application, which we'll build as a web-app image, to start after our Postgres container. Let's have a look at the docker-compose.yml file:

```
services:
  db:
    image: postgres:latest
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
    ports:
      - 5432:5432
  web-app:
    image: web-app:latest
    ports:
      - 8080:8080
    depends_on:
      - db
```

Docker will pull the images and run the containers based on the given dependencies. So, in this case, the Postgres container is the first in the queue to run.

**BUT**
> depends on doesn't guarantee dependency services. <br>
if you want to guarantee it use **_condition_** attribute

### - condition
condition options 
* service_started
* service_healthy &larr; need **_healthcheck_** option
* service_completed_successfully

for example
```
# docker-compose.yml
version: '3'
services:

    db:
        image: postgres
        volumes:
          - postgres_data:/var/lib/postgresql/data/
        healthcheck:
          test: pg_isready -U postgres -d postgres
          interval: 10s
          timeout: 3s
          retries: 3

    django:
        container_name: django
        build: ./djangoweb
        image: djangoweb/django
        restart: always
        command: uwsgi --ini uwsgi.ini
        volumes:
          - ./djangoweb:/srv/compose_test
          - ./log:/var/log/uwsgi
        depends_on:
            db:
              condition: service_healthy
        env_file:
          - ./.env.dev
```

### * Link

this instructs links containers over a network <br>
When we link containers, Docker creates environment variables and adds containers to the known hosts list so they can discover each other.

```
services:
  db:
    image: postgres:latest
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
    ports:
      - 5432:5432
  web-app:
    images: web-app:latest
    ports:
      - 8080:8080
    links:
      - db
```

### * Network

Docker-compose deprecates _Link_ it since version 2 because of the **_network_** 
<br>
**_network_** make applications are linked with complex networking

### bridge network
### overlay network

---
Reference 

1.https://docs.docker.com/compose

2.https://www.baeldung.com/ops/docker-compose-links-depends-on