from botocore.exceptions import ClientError
from awsalarhostk.InitData import InitData
import base64

class HiddenSecrets(InitData):
    def __init__(self):
        super(HiddenSecrets, self).__init__()

    def create_hidden_secrets(self, name, description, secretstring):
        '''
        :param name:
        :param description:
        :param secretstring:
        :return:
        '''
        try:
            # description = 'My test database secret created with the CLI',
            # name = 'MyTestDatabaseSecret',
            # secretString = '{"username":"david","password":"BnQw!XDWgaEeT9XGTT29"}'
            self.client_secrets_manager.create_secret(
                Description=description,
                Name=name,
                SecretString=secretstring,
                KmsKeyId=self.KmsKeyId,

            )
        except ClientError as Error:
            if Error.response['Error']['Code'] == 'ResourceExistsException':
                print('Object exists')
            else:
                print(f'Unexpected error:{Error}')

    def get_secret(self, name):
        '''
        :param name:
        :return:
        '''
        try:
            get_secret_value_response = self.client_secrets_manager.get_secret_value(SecretId=name)
            print (f'Secret value response:{get_secret_value_response}')
            if 'SecretString' in get_secret_value_response:
                secret = get_secret_value_response['SecretString']
                print(f'Secret string:{secret}')
            else:
                decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
                print(decoded_binary_secret)
        except ClientError as Error:
            if Error.response['Error']['Code'] == 'DecryptionFailureException':
                raise Error
            elif Error.response['Error']['Code'] == 'InternalServiceErrorException':
                raise  Error
            elif Error.response['Error']['Code'] == 'InvalidParameterException':
                raise  Error
            elif Error.response['Error']['Code'] == 'InvalidRequestException':
                raise  Error
            elif Error.response['Error']['Code'] == 'ResourceNotFoundExceptoon':
                raise  Error
            print(f'Unexpected error:{Error}')
