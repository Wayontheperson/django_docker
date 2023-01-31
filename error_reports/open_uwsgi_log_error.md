# uwsgi log can't open
## Issue:
- In vscode uwsgi couldn't open
    - error message
    ```
    The editor could not be opened due to an unexpected error: Unable to read file 'vscode-remote://ssh-remote+<numbers>/<path_to_uwsgi.log>
    ``` 

- But in terminal and the uwsgi docker container could open the logfile. even nginx log files ,which has been made with the same process, work well


