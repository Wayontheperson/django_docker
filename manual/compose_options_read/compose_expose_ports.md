## EXPOSE vs PORTS
----
### Ports 
> Expose ports. Either specify both ports (HOST:CONTAINER), or just the container port <br>
>(a random host port will be chosen).

```
mysql:
    images: mysql:5.7
    ports:
        - "3306"
```

|Name|Command|State|Ports|
|:---:|:---:|:---:|:---:|
|mysql_1|docker-entrypoint.sh mysqld|up|0.0.0.0:32769->3306/tcp|

### Expose 
>Expose ports without publishing them to the host machine - they’ll only be accessible to linked services.<br> Only the internal port can be specified.

```
mysql:
    images: mysql:5.7
    expose:
        - "3306"
```
|Name|Command|State|Ports|
|:---:|:---:|:---:|:---:|
|mysql_1|docker-entrypoint.sh mysqld|up|3306/tcp|

