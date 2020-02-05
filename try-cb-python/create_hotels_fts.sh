#!/bin/bash
echo "This script will make the full text index needed for the travel-sample"
 
userName="Administrator"
userPass="password"
ftsRes="n"
echo
read -rsn1 -p "Proceeed? y/(n)" ftsRes 

if [ $ftsRes = "y" ] || [ $ftsRes = "Y" ] 
then
    curl -u "$userName":"$userPass" -XPUT http://localhost:8094/api/index/hotels  -H 'cache-control: no-cache'  -H 'content-type: application/json'  -d@./fts-hotels-index.json
else
    echo "FTS Index create cancelled. Exiting ..."
fi 

