# AWS End-to-End Data Engineering Pipeline

## 📌 Project Overview

This project demonstrates an end-to-end Data Engineering pipeline built using AWS services. It ingests raw sales data, performs ETL transformations using AWS Glue and PySpark, stores curated data in Amazon S3, and enables analytics through Amazon Athena. Apache Airflow (MWAA) is used to orchestrate the workflow, while CloudWatch and SNS provide monitoring and notifications.

---

## 🏗️ Architecture

(Add architecture.png here)

---

## 🛠️ Tech Stack

- Python
- SQL
- AWS S3
- AWS Glue
- PySpark
- Amazon Athena
- Apache Airflow (MWAA)
- CloudWatch
- SNS

---

## 📂 Folder Structure

```text
architecture/
data/
scripts/
glue/
airflow/
sql/
docs/
screenshots/
```

---

## 🔄 Pipeline Workflow

1. Load raw CSV data.
2. Upload raw data to Amazon S3.
3. Process and clean data using AWS Glue (PySpark).
4. Store transformed data as Parquet in S3.
5. Register data in AWS Glue Catalog.
6. Query curated data using Amazon Athena.
7. Schedule and monitor the workflow using Apache Airflow.
8. Receive alerts through CloudWatch and SNS.

---

## 🚀 Features

- End-to-End ETL Pipeline
- Automated Data Transformation
- AWS Glue Integration
- Athena Analytics
- Apache Airflow Orchestration
- CloudWatch Monitoring
- SNS Notifications

---

## 📈 Future Enhancements

- Kafka Streaming
- Docker
- Terraform
- CI/CD Pipeline
- Data Quality Framework
