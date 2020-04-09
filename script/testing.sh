#!/bin/bash
# source  ~/.bashrc
# source /var/lib/jenkins/workspace/"Pipeline 1"/venv/bin/activate
# coverage run -m pytest ./test/testing.py
# coverage report

source /var/lib/jenkins/.bashrc

python3 -m /var/lib/jenkins/workspace/"Pipeline 1"/coverage run --source=. -m pytest test/testing.py
python3 -m /var/lib/jenkins/workspace/"Pipeline 1"/coverage report -m