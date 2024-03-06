# example create metrics and alerts
from awsalarhostk.aws_base import AWSSDK

if __name__ == '__main__':
    try:
        sdk = AWSSDK()

        patern = '\"ERROR: Can not create cx_Oracle session pool.\"'
        metricname = 'OracleIssueTestCinque'
        alarmname = 'host OracleTestCinque'
        loggroupname = 'docker-host-dev-test'
        filtername = 'ERROR-Can-not-create-cx-Oracle-session-pool-test-cinque'
        topicname = 'host-oracle-test-cinque'
        email = 'dan.bordeanu@host.com'
        alarmdescription = 'issue with oracle connection Cinque'

        sdk.create_metric(loggroupname, filtername, patern, metricname, '1')

        arn = sdk.create_subscription(topicname, email)

        sdk.create_alarm(arn, metricname, alarmname, alarmdescription)
        sdk.disable_alarm(alarmname)
    except Exception as e:
        print (f'Exception:{e}')