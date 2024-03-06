# create logs group and streams
from awsalarhosk.aws_base import AWSSDK

if __name__ == '__main__':
    try:
        sdk = AWSSDK()

        loggroupname = 'docker-host-dev-test'
        logstreamname = 'docker-fe'

        sdk.create_logs_group(loggroupname)
        sdk.create_logs_stream(loggroupname, logstreamname)

    except Exception as e:
        print (f'Exception:{e}')