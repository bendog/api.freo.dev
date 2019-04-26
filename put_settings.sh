#!/bin/bash
# upload settings file to s3
aws --profile bendog s3 cp settings.json s3://api.freo.dev.config/settings.json
aws --profile bendog s3 cp zappa_settings.json s3://api.freo.dev.config/zappa_settings.json
