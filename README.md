


# AWSALARMSDK Python SDK

A python-based SDK for creating cloudwatch alerts and SNS alarms


## Introduction

This is a very simple way to create cloudwatch metrics based on filters and SNS alerts

## Installation


### Installing from artifactory


The project has been released as a python packaged stored in host artifactory repository.

#### Prerrequisites

Create the file: `~/.pip/pip.conf` in Linux, or `%HOME%/pip/pip.ini` in Windows and copy/paste the below configuration:

```bash
[global]
index-url = https://artifacts.host.com/artifactory/api/pypi/pypi-main-dev/simple

[search]
index = https://artifacts.host.com/artifactory/api/pypi/pypi-main-dev/

```

#### Building

```bash
python3 -m pip install --user --upgrade setuptools wheel
```

```bash
python3 setup.py sdist bdist_wheel
```

#### Uploading to artifactory

Create in project root directory file: .pypirc 

!!!NB!!! see setup.py for more info about overwriting pypirccommands

```bash
[distutils]
index-servers = local
[local]
repository: https://artifacts.host.com/artifactory/api/pypi/pypi-host-dev/
username: srvsredocker
password: XXXX
```

Upload package to artifactory

```bash
python3 setup.py sdist upload -r local
```

#### Installation

The package can be installed using **pip** :

**NB** be sure to use pip3 (for python 3)

Create local pip.conf file

```bash
[global]
index-url = https://artifacts.host.com/artifactory/api/pypi/pypi-main-dev/simple
[search]
index = https://artifacts.host.com/artifactory/api/pypi/pypi-main-dev/
```

```python
pip3 install host_host_awsalarhostk
```
Or if you need to use the proxy:

```python
pip3 install host_host_awsalarhostk --install  --no-cache-dir
```

Use this without changing pip.conf file:


```python
pip3 install --index-url https://artifacts.host.com/artifactory/api/pypi/pypi-main-dev/simple host_host_awsalarhostk
```



```python
from awsalarhostk.aws_base import AWSSDK
```


## Examples

The user can create log groups and metrics, metrics based on paterns, SNS alarms


##### Example 0: create log group


 
```python
from awsalarhostk.aws_base import AWSSDK
sdk = AWSSDK()
loggroupname = 'docker-host-dev-test'
sdk.create_logs_group(loggroupname)

```
 
 
##### Example 1: create log stream

```python
from awsalarhostk.aws_base import AWSSDK
sdk = AWSSDK()
logstreamname = 'docker-fe'
sdk.create_logs_stream(loggroupname, logstreamname)
``` 


##### Example 2: create metrics and alarm

```python
# example create metrics and alerts
from awsalarhostk.aws_base import AWSSDK

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
```

#### Example 3: disable alarm

```python
from awsalarhostk.aws_base import AWSSDK
sdk = AWSSDK()
alarmname = 'host OracleTestCinque'
sdk.disable_alarm(alarmname)
```

#### Example 4: create secret

__!!!NB!!!__ Secrets created are using KMSKeyId env variable for encryption (self.KmsKeyId = environ.get('KMSKEY_ID', '765124fd-2e19-4b8c-9d0c-0a68090bc649'))

```python
from awsalarhostk.aws_base import AWSSDK
sdk = AWSSDK()
sdk.create_secrets('host_MyTestDatabaseSecretOne', 'host_description', '{"username":"david","password":"BnQw!XDWgaEeT9XGTT29"}')
```

#### Example 5: read secret

```python
from awsalarhostk.aws_base import AWSSDK
sdk = AWSSDK()
sdk.print_secrets('host_MyTestDatabaseSecretOne')
```