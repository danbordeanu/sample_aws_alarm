from botocore.exceptions import ClientError
from awsalarhostk.InitData import InitData


class Logs(InitData):
    def __init__(self):
        super(Logs, self).__init__()

    def logsgroup(self, loggroupname=None):
        '''
        Create dev log group
        :return:
        '''
        try:
            if loggroupname:
                loggroupname = loggroupname
            else:
                loggroupname = self.log_group_name

            self.client_logs.create_log_group(
                logGroupName=loggroupname,
            )
        except ClientError as Error:
            if Error.response['Error']['Code'] == 'EntityAlreadyExists':
                print('Group exists')
            else:
                print(f'Unexpected error:{Error}')

    def logsstream(self, loggroupname, logstreamname):
        '''
        Create FE dev logs stream
        :return: 
        '''
        try:
            if loggroupname:
                loggroupname = loggroupname
            else:
                loggroupname = self.log_group_name

            if logstreamname:
                logstreamname = logstreamname
            else:
                raise ValueError('logstreamname must be defined')

            self.client_logs.create_log_stream(
                logGroupName=loggroupname,
                logStreamName=logstreamname
            )
        except ClientError as Error:
            if Error.response['Error']['Code'] == 'EntityAlreadyExists':
                print('Group exists')
            else:
                print(f'Unexpected error:{Error}')

    def metricfilter(self, loggroupname, filtername, filterpatern, metricname, value):
        '''
        create metric filter
        :param loggroupname:
        :param filtername:
        :param filterpatern:
        :param metricname:
        :param value:
        :return:
        '''
        try:
            print(loggroupname, filtername, filterpatern, metricname, value)
            put_metric = self.client_logs.put_metric_filter(
                logGroupName=loggroupname,
                filterName=filtername,
                filterPattern=filterpatern,
                metricTransformations=[
                    {
                        'metricName': metricname,
                        'metricNamespace': self.namespace,
                        'metricValue': value,
                    },
                ]
            )
            print(put_metric)
        except ClientError as Error:
            if Error.response['Error']['Code'] == 'EntityAlreadyExists':
                print('Object exists')
            else:
                print(f'Unexpected error:{Error}')
