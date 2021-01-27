# Food Blog Printer
Looks for "Print Recipe" links in food blogs and provides link.

### Setup
`python -m venv venv`
`source venv/bin/activate`
`pip install flask requests==2.22.0 beautifulsoup4==4.8.2 zappa flask_sqlalchemy`

### Local Testing
`python app.py runserver`

### Deploying First Time
```
zappa init
zappa deploy dev
```
Additionally had to add `lambda:DeleteFunctionConcurrency` to the Group Policy below


### Deploying Again
`zappa update dev`

### Taking Down
`zappa undeploy dev`

### Refs
`https://pythonforundergradengineers.com/deploy-serverless-web-app-aws-lambda-zappa.html`
