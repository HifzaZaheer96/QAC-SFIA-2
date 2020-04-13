#!/bin/bash
source  /var/lib/jenkins/.bashrc
coverage run -m --source=. pytest ./test/testing.py
coverage report