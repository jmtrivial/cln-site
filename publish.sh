#!/bin/bash

git push
make && rsync -av build/*.html jmtrivial.info:~/cln/ && { 
for i in css docs images js pdf; do
  rsync -rav $i/ jmtrivial.info:~/cln/$i/ 
done }
