#!/bin/sh

# Run this from root folder 
docker-compose config | docker stack deploy -c - $1