#!/bin/bash

if [ -d "ai42" ]; then
	rm -rf ai42
	mkdir ai42
else
	mkdir ai42
fi
mkdir ai42/logging
cp log.py ai42/logging
cp __init__.py ai42
cp progressbar.py ai42
python setup.py sdist bdist_wheel
