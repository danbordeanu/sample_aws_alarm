
from botocore.exceptions import ClientError
from awsalarhost0k.InitData import InitData

class Sns(InitData):
    def __init__(self):
        super(Sns, self).__init__()


    def create_topic(self, topicname):
        '''
        Create topic
        :param topicname:
        :return:
        '''
        try:
            topic = self.client_sns.create_topic(Name=topicname)
        except ClientError as Error:
            if Error.response['Error']['Code'] == 'EntityAlreadyExists':
                print('Group exists')
                topic = 'Object exists'
            else:
                print(f'Unexpected error:{Error}')
                topic = 'Unexpected error'
        return topic

    def create_subscribtion(self, topic, email):
        '''
        :param topic:
        :param email:
        :return:
        '''
        try:
            arn = topic['TopicArn']
            self.client_sns.subscribe(TopicArn=arn, Protocol='email',
                                                Endpoint=email)
        except ClientError as Error:
            if Error.response['Error']['Code'] == 'EntityAlreadyExists':
                print('Object exists')
            else:
                print(f'Unexpected error:{Error}')

