#!/bin/bash

make && rsync -av build/*.html jmtrivial.info:~/cln/ && { 
for i in css doc images js pdf; do
  rsync -rav $i/ jmtrivial.info:~/cln/$i/ 
done }
