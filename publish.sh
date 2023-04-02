#!/bin/bash

git push
make -j && rsync -av build/*.html build/*json jmtrivial.info:/var/www/cln.jmfavreau.info/ && {
for i in css docs images js pdf; do
  rsync -rav $i/ jmtrivial.info:/var/www/cln.jmfavreau.info/$i/ 
done }
