#!/bin/sh

# Run this from project's root folder 

exec docker-compose -f docker-compose.yml -f docker-compose.prod.yml config | docker stack deploy -c - $1
