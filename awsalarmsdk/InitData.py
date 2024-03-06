from os import environ
import boto3


class InitData:
    # pylint: disable=R0903
    # pylint: disable=R0902
    '''
    init
    :return:
    '''
    def __init__(self):
        '''
        Config for aws boto3 client
        :rtype: object
        :return:
        '''
        try:
            # pylint: disable=R0902

            # access key
            # pylint: disable = C0103
            self.ACCESS_KEY = environ.get('ACCESS_KEY', 'AKIA5JFUVFGKPNICRTHW')
            self.SECRET_KEY = environ.get('SECRET_KEY', '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')
            self.KmsKeyId = environ.get('KMSKEY_ID', '765124fd-2e19-4b8c-9d0c-0a68090bc649')

            # hardcoded values
            self.region = environ.get('REGION', 'us-east-1')
            self.log_group_name = 'docker-host-dev-test'
            self.metric_name = 'OracleIssueTest'
            self.topic = 'host-oracle-test'
            self.endpoint = 'dan.bordeanu@hostOD.com'
            self.namespace = 'hostMetrics'
            self.alarmname = 'host OracleTest'
            self.comparationoperator = 'GreaterThanOrEqualToThreshold'


            # clients
            self.client_cloudwatch = boto3.client('cloudwatch',
                                                  aws_access_key_id=self.ACCESS_KEY,
                                                  aws_secret_access_key=self.SECRET_KEY,
                                                  region_name=self.region
                                                  )
            self.client_logs = boto3.client('logs',
                                            aws_access_key_id=self.ACCESS_KEY,
                                            aws_secret_access_key=self.SECRET_KEY,
                                            region_name=self.region
                                            )

            self.client_sns = boto3.client('sns',
                                           aws_access_key_id=self.ACCESS_KEY,
                                           aws_secret_access_key=self.SECRET_KEY,
                                           region_name=self.region
                                           )
            self.client_secrets_manager = boto3.client('secretsmanager',
                                                  aws_access_key_id=self.ACCESS_KEY,
                                                  aws_secret_access_key=self.SECRET_KEY,
                                                  region_name=self.region
                                                  )

        # pylint: disable=W0703
        except BaseException as error:
            print(f'There is some generic problem:{error}')
