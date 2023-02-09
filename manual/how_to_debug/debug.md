## How to debug containerized django with debugpy
---
### * debug in vscode 

- How to Setting

1.  Make **launch.json** file and locate in directory ***.vscode***
<br> ex)<br>
    ```
    {
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Remote Attach",
            "type": "python",
            "request": "attach",
            "port": 5678,
            "host":"localhost",
            "pathMappings": [
                  {
                    "localRoot": "${workspaceFolder}/djangoweb",
                    "remoteRoot": "/srv/djangoweb"
                    }
                ],
            }
        ]
    }
    ```
2. Modify docker-compose.yml 
    ```
    django:
        container_name: django
        build: ./djangoweb
        image: djangoweb/django
        restart: always
        command: uwsgi --ini uwsgi.ini
        expose:
        - 8000
        volumes:
        - ./djangoweb:/srv/compose_test
        - ./log:/var/log/uwsgi
        depends_on:
        db:
            condition: service_healthy
        redis:
            condition: service_healthy
        env_file:
        - ./.env
        environment:
        POSTGRES_PASSWORD: /run/secrets/db_password
        secrets:
        - POSTGRES_PASSWORD
        
    debug:
        container_name: debug_django
        image: djangoweb/django
        restart: always
        command: python manage.py runserver 0.0.0.0:8000 --nothreading --noreload
        volumes:
        - ./djangoweb:/src/compose_test
        depends_on:
        db:
            condition: service_healthy
        env_file:
        - ./.env
        environment:
        POSTGRES_PASSWORD: /run/secrets/db_password
        secrets:
        - POSTGRES_PASSWORD
    ``` 
    >❓ Why make debug container?<br>
        if debug container is not exist you should stop container and change command option in docker-compose.yml<br>
        However if you make debug container, you can debug without stopping container which is running service.
    > 

3. Modify manage.py
```
import os
import sys
import debugpy
from django.conf import settings

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'raptor_platform.settings')

    # start new section
    if settings.DEBUG:
        # if os.environ.get('RUN_MAIN') or os.environ.get('WERKZEUG_RUN_MAIN'):
        print(os.environ.get("RUN_MAIN"))
        debugpy.listen(("0.0.0.0", 5678))
        debugpy.wait_for_client()
        print('Attached!')
    # end new section

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

```

>✔ tip)<br> 
if you run runserver with the --noreload flag you should remove the line<br> ***if os.environ.get('RUN_MAIN') or os.environ.get('WERKZEUG_RUN_MAIN'):***

> --noreload flag <br>
Disables the auto-reloader. This means any Python code changes you make while the server is running will not take effect if the particular Python modules have already been loaded into memory.
<br>❗ It means --noreload flag doesn't make environment valuable **"RUN_MAIN**, **"WERKZEUG_RUN_MAIN"**


