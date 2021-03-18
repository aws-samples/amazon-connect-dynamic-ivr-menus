# CDK application is used for building all required resources

https://docs.aws.amazon.com/cdk/latest/guide/home.html

## Deployment using cdk-app (CloudFormation)

Before proceeding, make sure, you have CLI access to the AWS Account, where you would like to deploy your solution
https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html

Note: The default region is usually us-east-1. If you would like to deploy in another region, you can run: 
```bash
export AWS_DEFAULT_REGION=eu-central-1
```

```bash
npm install -g aws-cdk
npm install -g npm-check-updates
cd cdk-app
ncu -u
npm install
npm run build
cdk bootstrap
cdk deploy
```
After the stack is created, run the 'populateDBLambda' to insert dummy customer data:

aws lambda invoke --function-name populateDBLambda response.json

## Removal of resources

```
cdk destroy
```
