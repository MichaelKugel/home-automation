#!/bin/bash

#filename=data_secure2_$(date +%Y%m%d).txt
filename=data_gather_1_22032015.txt

echo "docker ps" >> $filename
docker ps >> $filename
echo "pstree" >> $filename
pstree >> $filename
echo "top -n 1 -b" >> $filename
top -n 1 -b >> $filename
echo "free -m" >> $filename
free -m >> $filename
echo "df" >> $filename
df >> $filename
echo "du" >> $filename
du >> $filename
echo "----->>>>> " >> $filename
