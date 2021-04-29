import setuptools

with open("README.md") as fp:
    long_description = fp.read()

setuptools.setup(
    name="rds_pg_qs",
    version="0.0.1",
    description="An CDK Python app to bring a sample app backed by postgres",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="ivanoot",
    package_dir={"": "rds_pg_qs"},
    packages=setuptools.find_packages(where="rds_pg_qs"),
    install_requires=[
        "aws-cdk.core==1.72.0",
        "aws_cdk.aws_rds==1.72.0",
        "aws_cdk.aws_ec2==1.72.0",
        "aws_cdk.aws_secretsmanager==1.72.0",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)