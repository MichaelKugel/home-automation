#!/bin/bash
echo "docker ps" >> data4.txt
docker ps >> data4.txt
echo "pstree" >> data4.txt
pstree >> data4.txt
echo "free -m" >> data4.txt
free -m >> data4.txt
echo "du" >> data4.txt
du >> data4.txt
echo "df" >> data4.txt
df >> data4.txt
echo "top -b -n 1" >> data4.txt
top -b -n 1 >> data4.txt
echo "----->>>>>" >> data4.txt
date >> data4.txt

