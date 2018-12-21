# snapshotalyzer

Acloud.guru project to manage ec2 instances remotely using boto3

##Git

Version control for this project is managed through Github
Requires a github repository in github, then use commands to import/export

`git clone snapshotalyzer`
`git status`
`git add <files>`
`git commit` #add comments to file or use -m "<comments>"
`git push`


## Config

pipenv is used to manage the environment
`pip3 install pipenv`

create a python3 project from the home dir of shotalyzer
`pipenv --three`

shotty uses the config file created by the AWS cli. e.g.

`aws configure --profile shotty`

Shotty uses boto3 and click for CLI features
`pipenv install boto3`
`pipenv install click`

iPython for development purposes
`pipenv install -d ipython`

## Running

`pipenv run python shotty\shotty.py <command> <--project=PROJECT>`

*command* is list,start,stop
*project* is optional