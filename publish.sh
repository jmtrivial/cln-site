#!/bin/bash

git push
ssh jmtrivial.info "cd cln; git pull"
make
rsync -rav pdf/ jmtrivial.info:~/cln/pdf/
