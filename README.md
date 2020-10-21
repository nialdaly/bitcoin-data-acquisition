# Bitcoin Data Acquisition
The following project will demonstrate the process of creating a serverless bitcoin data acquisition pattern. This pattern pulls Bitcoin price data from [Coinbase](https://www.coinbase.com) at 1 minute intervals. Coinbase provides an [API](https://developers.coinbase.com) that developers can use to buy, sell and access cryptocurrency price data. The data is then persisted in AWS DynamoDB, Amazon's proprietary NoSQL database solution.

The project makes use of Docker, AWS Lambda, Amazon CloudWatch, AWS DynamoDB, Serverless Framework and the Coinbase Digital API.

## Prerequisites
* [Serverless Framework](https://www.serverless.com/framework/docs/providers/aws/guide/installation/)
* [Serverless Python Requirements](https://www.serverless.com/plugins/serverless-python-requirements)
* [awscli](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
* [AWS Account with AWS CLI Access configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)
* [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation)
* [Coinbase Account & API Credentials](https://developers.coinbase.com/docs/wallet/api-key-authentication)
* [Docker](https://hub.docker.com/editions/community/docker-ce-desktop-mac/)
[Virtualenv]()

## Getting Started
This project assumes that you have installed and configured the AWS Command Line Interface (CLI). In the root directory, run the following command to create a Python virtual environment, assuming that you have the `virtualenv` package installed.
```
virtualenv venv --python=python3
```

The virtual environment can then be activated using the following command.
```
source venv/bin/activate
```

The Python packages needed by the Lambda function are specified in the `requirements.txt` file. They can be installed in the `venv` virtual environment with the following command.
```
pip install -r requirements.txt
```

The resources can then be deployed by running `serverless deploy` which will use CloudFormation to provision the Lambda function and the DynamoDB table.

## Resource Cleanup
The resources created in this pattern can be deleted using the `serverless remove` command. To deactivate the virtual environment, `venv`, simply run `deactivate`.

## Additional Resources
*[Handle Python packaging in Lambda](https://www.serverless.com/blog/serverless-python-packaging)