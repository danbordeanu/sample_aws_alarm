from botocore.exceptions import ClientError
from awsalarhostk.InitData import InitData


class Alarm(InitData):
    def __init__(self):
        super(Alarm, self).__init__()

    def create_alarm(self, topic, metricname, alarmname, alarmdescription, operator=None):
        '''
        create create_alarm
        :param topic:
        :param metricname:
        :param alarmname:
        :param alarmdescription:
        :param operator
        :return:
        '''
        try:
            if operator:
                operator = operator
            else:
                operator = self.comparationoperator
            self.client_cloudwatch.put_metric_alarm(
                AlarmName=alarmname,
                ComparisonOperator=operator,
                EvaluationPeriods=1,
                MetricName=metricname,
                Namespace=self.namespace,
                Period=300,
                Statistic='Sum',
                Threshold=1.0,
                DatapointsToAlarm=1,
                ActionsEnabled=True,
                OKActions=[],
                AlarmActions=[
                    topic['TopicArn']
                ],
                AlarmDescription=alarmdescription,
                Dimensions=[]
            )
        except ClientError as Error:
            if Error.response['Error']['Code'] == 'EntityAlreadyExists':
                print('Object exists')
            else:
                print(f'Unexpected error:{Error}')

    def disable_alarm(self, alarmname):
        '''
        disable create_alarm
        :param alarmname:
        :return:
        '''
        try:
            self.client_cloudwatch.disable_alarm_actions(AlarmNames=[alarmname])
        except ClientError as Error:
            print(f'Unexpected error:{Error}')

    def enable_alarm(self, alarmname):
        '''
        enable alarm
        :param alarmname:
        :return:
        '''
        try:
            self.client_cloudwatch.enable_alarm_actions(AlarmNames=[alarmname])
        except ClientError as Error:
            print(f'Unexpected error:{Error}')

    def delete_alarm(self, alarmname):
        '''
        delete alarm
        :param alarmanem:
        :return:
        '''
        try:
            self.client_cloudwatch.delete_alarms(AlarmNames=[alarmname])
        except ClientError as Error:
            print(f'Unexpected error:{Error}')
