#!/bin/bash

ansible-playbook -i inventory.cfg playbook.yml --start-at-task="install packages"