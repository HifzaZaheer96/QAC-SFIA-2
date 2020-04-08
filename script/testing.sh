#!/bin/bash
source  ~/.bashrc
coverage run -m pytest ./test/testing.py
coverage report