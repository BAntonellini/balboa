# Datacoves

## Commands

### AWS

```shell
pip install awscli
aws configure
aws s3 ls s3://datacoves-us-east-a-develop-test/amorera-dev/
aws s3 cp . s3://datacoves-us-east-a-develop-test/amorera-dev --recursive
aws s3 cp . s3:/datadrive-airflow-prod/orchestrate/dags --recursive
```
