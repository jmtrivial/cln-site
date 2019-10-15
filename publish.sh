#!/bin/bash

git push
make && rsync -av build/*.html murol:/var/www/cln.jmfavreau.info/ && { 
for i in css docs images js pdf; do
  rsync -rav $i/ murol:/var/www/cln.jmfavreau.info/$i/ 
done }
