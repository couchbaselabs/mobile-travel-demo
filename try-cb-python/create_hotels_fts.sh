#!/bin/bash
curl -u Administrator:password -XPUT http://localhost:8094/api/index/hotels  -H 'cache-control: no-cache'  -H 'content-type: application/json'  -d@./fts-hotels-index.json
