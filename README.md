# Python Environment

A structured Python workspace for all things Python:

* Data engineering
* Machine learning projects
* Algorithm and problem-solving practice

**Goal:** To provide a single environment for developing Python skills in a professional, organized way, with reusable modules, notebooks, and practice challenges.

## Project Structure

* `src/` — Reusable Python modules and packages
* `notebooks/` — Jupyter notebooks for data exploration and visualisation, including analysis built against schemas and datasets from [sql-environment](https://github.com/Thembezakhe/sql-environment)
* `tests/` — Test cases for validating modules
* `ML_Projects/` — Machine learning projects reproducing examples from the book by Brian and Lisa
* `coding_challenges/` — Python algorithm and problem-solving practice
  * `leetcode/` — Medium to hard LeetCode Python challenges for skill building
  * `hackerrank/` — Python, problem-solving, and data engineering challenges for interview preparation
  * `coderbyte/` — Python coding challenges and skill assessments from Coderbyte
* `requirements.txt` — Python dependencies
* `.gitignore` — Files and folders excluded from version control

> **Scope:** All challenges across platforms (LeetCode, HackerRank, Coderbyte) are Python only. SQL challenges from any platform are organised by concept and maintained exclusively in the [sql-environment](https://github.com/Thembezakhe/sql-environment) repo under `InterviewPrep/`.

## Cross-Repository Work

Some projects in this environment connect directly to work in [sql-environment](https://github.com/Thembezakhe/sql-environment):

* **ETL Pipelines** — Python scripts and notebooks that extract, transform, and load data using SQLAlchemy or pandas, working against schemas designed and maintained in sql-environment
* **Data Exploration** — Jupyter notebooks that visualise or analyse datasets whose structure originates in sql-environment
* **Interview Preparation** — This repo covers the Python layer of interview prep; sql-environment covers the SQL layer. Together they represent a full-stack data engineering practice approach

## Tech Stack

Currently using:

* Python 3.11+
* Pandas, NumPy for data manipulation
* SQLAlchemy & psycopg2-binary for PostgreSQL integration
* Jupyter for notebooks
* pytest for testing
* VS Code as my text editor

*(Additional tools and libraries will be added as the environment expands)*

## Getting Started

1. Clone the repo:

   ```
   git clone https://github.com/Thembezakhe/python-environment.git
   ```
