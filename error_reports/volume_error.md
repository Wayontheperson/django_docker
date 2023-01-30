# Anonymous volume docker

## Issue :
-   When run docker compose up, **anonymous volume** had been made  
```
DRIVER    VOLUME NAME
local     compose_test_postgres_data
local     compose_test_redis_data
local     ddf1b251e2eb7364261ff6ac35317c79cf39733a6c465341a42f9c8c008f0fad
```
---
<br>

## How to solve :
1.  Check what image mounts anonymous volume
    - Checked using docker volume rm  
    - In this case *ddf1b251e2eb7364261ff6ac35317c79cf39733a6c465341a42f9c8c008f0fad* was mounted on flower container
2. Inspect dockerfile 
    - Flower image is pulled from docker hub and it doesn't show dockerfile but using *docker inspect* \*container name\* we can inspect dockerfile 
    - From flower dockerfile
         ```
            "Volumes": {
                "/data": {},
                "/var/lib/redis/data": {}
            },
        ```
        "/data" is initially mounted by flower image, but "/var/lib/redis/data" is mounted by docker-compose.yml

        ```
        flower:
            container_name: flower
            image: mher/flower
            environment:
            - CELERY_BROKER_URL = 'redis://redis:6379/0'
            - FLOWER_PORT = 5555
            restart: always
            volumes:
            - flower_data:/var/lib/flower/data/
            expose:
        ```
3. Modify docker-compose.yml volume
    ```
            before:

            volumes:
                - flower_data:/var/lib/flower/data/
            
            after:

            volumes:
                - flower_data:/data/
    ```
---
<br>

## Result :

```
DRIVER    VOLUME NAME
local     compose_test_flower_data
local     compose_test_postgres_data
local     compose_test_redis_data
```

Anonymous volume removed
<br> 

date 2023.01.30
<br>
Resolves: #1
