#!/bin/bash
source  ~/bashrc
source /var/lib/jenkins/workspace/"Pipeline 1"/venv/bin/activate
coverage run -m pytest ./test/testing.py
coverage report
