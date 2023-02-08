## COPY vs ADD 
----
### * COPY 
takes in a source and destination. 
        It only lets you copy in a local or directory from your host<br>
        (the machine-building the Docker image) 
        into the Docker image itself.
<br>
<br>
### * ADD  
it does that same but in addition, it also supports 2 other sources.

1. A URL instead of a local file/directory.
2. Extract tar from the source directory into the destination.

    > but using ADD to fetch remote file and copying is not typically ideal.<br>
    because the file will increase the overall Docker Image size.<br>
    and ADD will automatically expand tar files into the image file system

    ```Instead, we should use curl or wget to fetch remote files and remove them when no longer needed.```
            
        
Reference https://www.geeksforgeeks.org/difference-between-the-copy-and-add-commands-in-a-dockerfile/
<br>
<br>
## depends on & link & network
---

