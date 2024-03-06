from os import environ
from awsalarhostk.helpers.sns import Sns
from awsalarhostk.helpers.alarm import Alarm
from awsalarhostk.helpers.logsgroup import Logs
from awsalarhostk.helpers.secrets import HiddenSecrets


class AWSSDK:
    def __init__(self, region=None, namespace=None):
        '''
        :param region:
        :param Namespace:
        '''
        self.ACCESS_KEY = environ.get('ACCESS_KEY', 'AKIA5JFUVFGKPNICRTHW')
        self.SECRET_KEY = environ.get('SECRET_KEY', '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')
        if region:
            self.region = region
        else:
            self.region = 'us-east-1'

        if namespace:
            self.Namespace = namespace
        else:
            self.Namespace = 'LogMetrics'

    @staticmethod
    def create_logs_group(loggroupname):
        '''
        :param loggroupname
        :return:
        '''
        assert isinstance(loggroupname, str), 'Log group value must be specified'
        logs_deploy = Logs()
        logs_deploy.logsgroup(loggroupname=loggroupname)

    @staticmethod
    def create_logs_stream(loggroupname, logstreamname):
        '''
        :param loggroupname:
        :param logstreamname:
        :return:
        '''
        assert isinstance(loggroupname, str), 'Log group value must be specified:EG: ' \
                                              'docker-host-dev-test'
        assert isinstance(logstreamname, str), 'Log stream name value must be specified: ' \
                                               'docker-be'
        logs_deploy = Logs()
        logs_deploy.logsstream(loggroupname=loggroupname, logstreamname=logstreamname)

    @staticmethod
    def create_metric(loggroupname, filtername, filterpatern, metricname, value):
        '''
        :param loggroupname:
        :param filtername:
        :param filterpatern:
        :param metricname:
        :param value:
        :return:
        '''
        assert isinstance(loggroupname, str), 'Log group value must be specified:EG:docker-host-dev-test'
        assert isinstance(filtername, str), 'Filter name must be specified:EG: ' \
                                            'ERROR-Can-not-create-cx-Oracle-session-pool-test'
        assert isinstance(filterpatern, str), 'Filter patern must be specified:EG:' \
                                              '\"ERROR: Can not create cx_Oracle session pool.\"'
        assert isinstance(metricname, str), 'Metric name must be specified:EG:OracleIssueTest'
        metric_deploy = Logs()
        metric_deploy.metricfilter(loggroupname=loggroupname, filtername=filtername,
                                   filterpatern=filterpatern, metricname=metricname, value=value)

    @staticmethod
    def create_subscription(topicname, email):
        '''
        :param topicname:
        :param email:
        :return:
        '''
        assert isinstance(topicname, str), 'Topic name must be defined:EG:host-oracle-tes'
        assert isinstance(email, str), 'Email endpoint:EG:dan.bordeanu@host.com '
        sns_deploy = Sns()
        sns_arn = sns_deploy.create_topic(topicname=topicname)
        print(sns_arn)
        sns_deploy.create_subscribtion(topic=sns_arn, email=email)
        return sns_arn

    @staticmethod
    def create_alarm(topic, metricname, alarmname, alarmdescription):
        '''
        Create alarm
        :param topic:
        :param metricname:
        :param alarmname:
        :param alarmdescription:
        :return:
        '''
        assert isinstance(topic, dict), 'Topic ARN name must be defined:EG:' \
                                        'arn:aws:sns:us-east-1:913059424666:host-oracle-test'
        assert isinstance(metricname, str), 'Metric name must be specified:EG:OracleIssueTest'
        assert isinstance(alarmname, str), 'Alarm name must be specified:EG:host OracleTest'
        assert isinstance(alarmdescription, str), 'Alarm description must be specified:' \
                                                  'EG:Connection  issue with ORACLE DB test'

        alarm_deploy = Alarm()
        alarm_deploy.create_alarm(topic=topic, metricname=metricname, alarmname=alarmname,
                                  alarmdescription=alarmdescription)

    @staticmethod
    def disable_alarm(alarmname):
        '''
        Disable alarm
        :param alarmname:
        :return:
        '''
        assert isinstance(alarmname, str), 'Alarm name must be defined'
        alarm_deploy = Alarm()
        alarm_deploy.disable_alarm(alarmname=alarmname)

    @staticmethod
    def create_secrets(name, description, secretstring):
        # TODO get kmsid as argument
        assert isinstance(name, str), 'Name of the secret must be specified:EG:MyTestDatabaseSecret'
        assert isinstance(description, str), 'Description of the secret:EG:My test database secret created with the CLI'
        assert isinstance(secretstring,
                          str), 'Secret string, EG:{"username":"david","password":"BnQw!XDWgaEeT9XGTT29"}'

        secret = HiddenSecrets()
        secret.create_hidden_secrets(name=name, description=description, secretstring=secretstring)

    @staticmethod
    def print_secrets(name):
        assert isinstance(name, str), 'Name of the secret must be specified:EG:MyTestDatabaseSecret'
        secret = HiddenSecrets()
        secret.get_secret(name=name)
