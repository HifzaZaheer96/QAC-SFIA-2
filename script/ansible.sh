#!/bin/bash
source  /var/lib/jenkins/.bashrc
ansible-playbook -i inventory.cfg playbook.yml --start-at-task="install packages"