#!/bin/bash

git push
ssh jmtrivial.info "cd cln; git pull"
make
./upload.sh
