#!/bin/bash
source --limit @/var/lib/jenkins/workspace/"Pipeline 1"/playbook.retry
docker stack deploy --compose-file docker-compose.yml stackthemegenerator 