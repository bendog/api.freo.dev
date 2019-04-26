# api.freo.dev

## setup local dev environment with pipenv

    pipenv install

activate with 

    pipenv shell

## deployment

first update the settings files.  
_Note: you'll need access to the settings s3 bucket for this to work._

    ./get_settings.sh

then use zappa to deploy the changes

    zappa update

or if it's the first run

    zappa deploy
    zappa certify
