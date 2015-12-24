
# Goal

Using Django framework create an application that per request:

http://<server>/stat/get will return a result in JSON with following options:

```
{
    "result": "success" or "error",
    "error": <string>, //returned if result="error"
    "cities": <number>, //total number of cities
    "users": <number> //total number of users
}
```

# Test
```sh
make test
```

# Install
```
/bin/bash install.sh
docker run rflynn:flashpoint_stat
```

# Redhat

https://docs.docker.com/engine/installation/rhel/
