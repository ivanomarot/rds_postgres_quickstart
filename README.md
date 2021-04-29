# Postgres (RDS) Quickstart

## Overview

This project contains an [AWS Cloud Development Kit](https://aws.amazon.com/cdk/) (CDK) based solution that provisions 
a database using [Amazon RDS for PostgreSQL](https://aws.amazon.com/rds/postgresql/) and an EC2 based bastion host that
uses [pgbench](https://www.postgresql.org/docs/10/pgbench.html) to send transactions periodically
to the database.

You can use this project for proofs-of-concept where you need to emulate an application sending regular database
transactions or for stress testing existing PostgreSQL installations.

## Default specifications

- PostgreSQL version 11.8 with a single 
  [SMALL](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-ec2.InstanceSize.html) instance.
- Logical replication enabled (useful to enable CDC replication)
- EC2 bastion host of instance size t3.micro accessible through SSM
- Pgbench runs every minute, during periods of 30 seconds (-T 30), and simulates transactions from 10 clients (-c 10). 
  This is performed with a sequence of SQL statements running against for 4 tables:

    * pgbench_branches  
    * pgbench_tellers  
    * pgbench_accounts
    * pgbench_history
    
## How to deploy?

Prerequisites:

- Install CDK in your computer or
  [set up an AWS Cloud 9 environment](https://docs.aws.amazon.com/cloud9/latest/user-guide/create-environment.html).
- Configure your AWS credentials locally for 
  [programmatic access](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys).

Deployment steps:

1. Clone this repository
1. Install dependencies

    ```bash
    sudo pip3 install -r requirements.txt
    ```

1. Boootstrap CDK

    ```bash
    cdk bootstrap
    ```

1. Deploy all the stacks

    ```bash
    cdk deploy --require-approval never "*" 
    ```

## Changing specifications

If you want to customize the parameters that control the workload generated by pgbench, you can use 
[AWS System Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-sessions-start.html)
to log into the instance. The pgbench utility is configured in the operative system scheduler as shown below.

```bash
sudo cat /etc/cron.d/pgbench_cron
*/2 * * * * root pgbench -c 10 -T 30 -h your_rds.rds.amazonaws.com -p 5432 -U postgres test
```

## Clean up

Remove your AWS resources:

```bash
cdk destroy "*"
```