
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

# Build

## OS X

```
docker-machine create -d virtualbox default
docker-machine run default
eval "$(docker-machine env default)" # magic os x docker command...
docker-compose build
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

