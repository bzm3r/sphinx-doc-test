#!/bin/bash

# change to the myproject docs folder
cd ./myproject/docs || exit

# activate the virtual environment
source ../../.venv/bin/activate
cp index_template index.rst
rm -rf ./_*
rm -rf ./*.rst
cp index_template index.rst

make clean
make html
