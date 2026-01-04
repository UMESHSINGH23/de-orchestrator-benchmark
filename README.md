# Data Engineering Project – Technical Submission (Part 2)
Course: Data Engineering  
Instructor: Prof. Raja Hashim Ali  
Submission: Part 2 – Technical Implementation 
**Group:** WS25-DE21 [Student A : UMESH SINGH] [STUDENT B : TALATCAN] 
## Project Overview
This project implements an end-to-end data engineering pipeline designed to ingest, clean, transform, analyze, and evaluate a real-world dataset. The pipeline follows a modular and reproducible structure aligned with industry-style data workflows.

The project answers predefined research questions using data analysis and simple machine learning techniques. All figures and tables are generated programmatically, and the entire pipeline is orchestrated using Apache Airflow to demonstrate logical task sequencing and pipeline design.

This repository represents the complete technical backbone for the final report and presentation.

## Dataset

The dataset used in this project is:
- **Name:** Pakistan Largest Ecommerce Dataset  
- **Source:** [https://www.kaggle.com/datasets/zusmani/pakistans-largest-ecommerce-dataset]  
- **Description:** This dataset contains transaction-level ecommerce data including order details, customer information, product categories, prices, and timestamps. It is used to analyze sales behavior and build analytical insights aligned with the research questions.

Note: The raw dataset is not included in this repository due to size constraints. A small sample (if required) is placed under the `data/sample/sample_data.csv.
## Research Questions

RQ1: [How do sales trends vary across different product categories over time?]

RQ2: [What are the seasonal patterns in customer purchasing behavior in Pakistan’s e-commerce market?]

## How to Run the Code

### 1. Clone the Repository
```bash
git clone [https://github.com/UMESHSINGH23/de-orchestrator-benchmark.git]
cd project-Benchmarking Workflow Orchestrators (Airflow vs Luigi vs Prefect) for Tabular ETL


## Project Structure
de-orchestrator-benchmark/
├── dags/.              # Airflow DAGs
├── src/                # Core business logic

        ├── data_ingestion/
        ├── data_cleaning/
        ├── feature_engineering/
        ├── modeling/
        └── evaluation/
<br>
├── data/.              # Datasets
<br>
├── figures/            # Plots & charts
├── tables/.            # Result tables
<br>
├── requirements.txt
<br>
└── README.md
<br>
---

## ⚙️ Technologies Used
- Python
- Apache Airflow
- Pandas
- NumPy
- Scikit-learn

---

## Pipeline Flow
1. Data Ingestion
2. Data Cleaning
3. Feature Engineering
4. Model Training
5. Model Evaluation

---

## Use Case
This structure reflects how data pipelines are implemented in:
- E-commerce
---

## Future Improvements
- Add data validation
- Add logging & monitoring
- Add CI/CD
- Deploy using Docker

---

## Author
Umesh Singh  
MSc Data Science | Germany
