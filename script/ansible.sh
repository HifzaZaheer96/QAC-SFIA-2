#!/bin/bash
sudo apt-get update
sudo apt-get install python -y
mkdir -p ~/.local/bin
echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc
source ~/.bashrc
## install ansible with pip
pip install --user ansible
# check that ansible has been installed
ansible --version


ansible-playbook -i inventory.cfg playbook.yml --start-at-task="install packages"