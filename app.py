#!/usr/bin/env python3

from aws_cdk import core

from rds_pg_qs.vpc_stack import VpcStack
from rds_pg_qs.rds_stack import RdsStack
from rds_pg_qs.bastion_stack import BastionStack

email_address = "ivanoot@amazon.com"

app = core.App()
vpc_stack = VpcStack(app, "rds-pg-qs-vpc")
rds_stack = RdsStack(app, "rds-pg-qs-rds", vpc=vpc_stack.vpc)
bastion_stack = BastionStack(app, "rds-pg-qs-bastion", vpc=vpc_stack.vpc, rds_sg=rds_stack.rds_sg,
                             secret=rds_stack.secret)
app.synth()
