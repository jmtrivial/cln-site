#!/bin/bash

make && echo rsync -rav build/*.html jmtrivial.info:~/cln/ && { 
for i in css doc documents images js pdf; do
  echo rsync -rav $i/ jmtrivial.info:~/cln/$i/ 
done }
