# Data Uploader

## CircleCI Test Status
Dev:  [![CircleCI](https://circleci.com/gh/inuinana/data_uploader/tree/dev.svg?style=svg)](https://circleci.com/gh/inuinana/data_uploader/tree/dev)  
Master: [![CircleCI](https://circleci.com/gh/inuinana/data_uploader/tree/master.svg?style=svg)](https://circleci.com/gh/inuinana/data_uploader/tree/master)  

## How to run locally on Mac

## Get PostgreSQL Database and run
$ brew update  
$ brew doctor  
$ brew install postgres  
$ pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start

## Now run the app
$ cd docker-compose/test  
$ docker-compose build  
$ docker-compose up -d

## App can be found here 
http://0.0.0.0:8000/