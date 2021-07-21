#!/bin/bash

g++ --shared -o libprocess.so process.cpp
python3 create_lib.py