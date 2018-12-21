# snapshotalyzer

Acloud.guru project to manage ec2 instances remotely using boto3

##Git

Version control for this project is managed through Github
`git clone snapshotalyzer`
`git status`
`git add <files>`
`git commit` #add comments to file or use -m "<comments>"
`git push`


## Config

shotty uses the config file created by the AWS cli. e.g.

`aws configure --profile shotty`

Shotty uses boto3 and click for CLI features
`pipenv install boto3`
`pipenv install click`

## Running

`pipenv run python shotty\shotty.py`