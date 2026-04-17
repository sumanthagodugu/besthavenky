#!/bin/bash
cd /home/ec2-user
 nohup python3 app.py > app.log 2>&1 &
