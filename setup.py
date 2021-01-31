# -*- coding: utf-8 -*-
import os

from setuptools import find_packages
from setuptools import setup


base_dir = os.path.dirname(__file__)
setup(
    name='elastalert',
    version='0.2.4',
    description='Runs custom filters on Elasticsearch and alerts on matches',
    author='Quentin Long',
    author_email='qlo@yelp.com',
    setup_requires='setuptools',
    license='Copyright 2014 Yelp',
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': ['elastalert-create-index=elastalert.create_index:main',
                            'elastalert-test-rule=elastalert.test_rule:main',
                            'elastalert-rule-from-kibana=elastalert.rule_from_kibana:main',
                            'elastalert=elastalert.elastalert:main']},
    packages=find_packages(),
    package_data={'elastalert': ['schema.yaml', 'es_mappings/**/*.json']},
    install_requires=[
        'apscheduler>=3.3.0',
        'aws-requests-auth>=0.3.0',
        'boto3>=1.4.4',
        'cffi>=1.11.5',
        'configparser>=3.5.0',
        'croniter>=0.3.16',
        'elasticsearch>=7.0.0,<8.0.0',
        'envparse>=0.2.0',
        'exotel>=0.1.3',
        'jira>=2.0.0',
        'jsonschema>=3.0.2',
        'mock>=2.0.0',
        'prison>=0.1.2',
        'prometheus_client>=0.6.0',
        'py-zabbix>=1.1.3',
        'PyStaticConfiguration>=0.10.3',
        'python-dateutil>=2.6.0,<2.9.0',
        'PyYAML>=5.1',
        'requests>=2.10.0',
        'sortedcontainers>=2.2.2',
        'stomp.py>=4.1.17',
        'texttable>=0.8.8',
        'twilio>=6.0.0,<6.1',
        'tzlocal<3.0'
    ]
)
