import * as cdk from '@aws-cdk/core';
import * as dynamodb from '@aws-cdk/aws-dynamodb';
import * as lambda from '@aws-cdk/aws-lambda';
import * as path from 'path';

export class CdkAppStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    /**
     * Create DynamoDBs
     */
    const customerInfoDb = new dynamodb.Table(this, 'customerInfoDb', {
      partitionKey: {
        name: 'clientID',
        type: dynamodb.AttributeType.STRING,
      },
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
      removalPolicy: cdk.RemovalPolicy.DESTROY
    });

    const policiesDb = new dynamodb.Table(this, 'policiesDb', {
      partitionKey: {
        name: 'policyID',
        type: dynamodb.AttributeType.STRING,
      },
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
      removalPolicy: cdk.RemovalPolicy.DESTROY
    });
    

    /**
     * Create Lambda Functions
     */

    const getCustomerDetails = new lambda.Function(this, 'getCustomerDetails', {
      runtime: lambda.Runtime.PYTHON_3_8,
      handler: 'lambda_function.lambda_handler',
      environment: {
        customerTable: customerInfoDb.tableName,
        policiesTable: policiesDb.tableName
      },
      code: lambda.Code.fromAsset(path.join(__dirname, '..', '..', 'lambda', 'menu-option'))
    });

    const selectionFulfilment = new lambda.Function(this, 'selectionFulfilment', {
      runtime: lambda.Runtime.PYTHON_3_8,
      handler: 'lambda_function.lambda_handler',
      environment: {
        customerTable: customerInfoDb.tableName,
        policiesTable: policiesDb.tableName
      },
      code: lambda.Code.fromAsset(path.join(__dirname, '..', '..', 'lambda', 'selectionFulfilment'))
    });

    const populateDB = new lambda.Function(this, 'populateDB', {
      runtime: lambda.Runtime.PYTHON_3_8,
      handler: 'lambda_function.lambda_handler',
      environment: {
        customerTable: customerInfoDb.tableName,
        policiesTable: policiesDb.tableName
      },
      functionName: 'populateDBLambda',
      code: lambda.Code.fromAsset(path.join(__dirname, '..', '..', 'lambda', 'populateDB'))
    });

    /**
     * Grant Full permission to customerInfoDb from Funtion getCustomerDetails and selectionFulfilment
     */

    customerInfoDb.grantReadWriteData(getCustomerDetails);
    customerInfoDb.grantReadWriteData(selectionFulfilment);
    customerInfoDb.grantReadWriteData(populateDB);

    /**
     * Grant Full permission to policiesDb from Funtion selectionFulfilment
     */

    policiesDb.grantReadWriteData(selectionFulfilment);
    policiesDb.grantReadWriteData(populateDB);

  }
}
