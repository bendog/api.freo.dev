#!/bin/bash
# get settings file from s3
aws --profile bendog s3 cp s3://api.freo.dev.config/settings.json settings.json 
aws --profile bendog s3 cp s3://api.freo.dev.config/zappa_settings.json zappa_settings.json 
