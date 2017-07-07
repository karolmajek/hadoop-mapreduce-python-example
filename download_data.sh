#!/bin/bash

cd data

# wget http://content.udacity-data.com/courses/ud617/access_log.gz
# gunzip access_log.gz

wget -q http://content.udacity-data.com/courses/ud617/purchases.txt.gz
gunzip purchases.txt.gz
