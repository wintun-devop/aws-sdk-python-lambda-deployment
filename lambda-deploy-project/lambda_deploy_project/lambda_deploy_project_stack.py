from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_lambda as _lambda
)
import os
from constructs import Construct

class LambdaDeployProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # Define the Lambda function
        cwd = os.getcwd()
        my_lambda = _lambda.Function(
            self, 'MyLambda',
            runtime=_lambda.Runtime.PYTHON_3_12,
            handler='lambda_function.handler',
            code=_lambda.Code.from_asset(os.path.join(cwd, "lambdas/lambda1"))
        )
        """ 
        #The code that defines your stack goes here
        #example resource
        queue = sqs.Queue(
            self, "LambdaDeployProjectQueue",
            visibility_timeout=Duration.seconds(300),
        ) 
        """
