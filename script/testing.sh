#!/bin/bash
source  /var/lib/jenkins/.bashrc
# source /var/lib/jenkins/workspace/"Pipeline 1"/venv/bin/activate
coverage run -m --source=. pytest ./test/testing.py
coverage report