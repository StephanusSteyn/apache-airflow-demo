# Apache Airflow Demo

A demonstration project for Apache Airflow 3.1.6 with Python 3.13, set up using `uv` for fast and modern Python package management.

## Purpose
This project is used to test out Apache Airflow for orchestrating and monitoring data pipelines.

## Setup Steps

### 1. Prerequisites

Ensure you have the following installed:
- `uv` (Python package manager)
- Git
- GitHub CLI (`gh`)

### 2. Initialize Git Repository

```bash
# Navigate to the project directory
cd apache-airflow-demo

# Initialize a new git repository
git init

# Rename the default branch to main
git branch -m main
```

### 3. Create GitHub Repository

```bash
# Create a public GitHub repository and add it as remote origin
gh repo create apache-airflow-demo --public --source=. --remote=origin
```

### 4. Set Up Python Environment with uv

```bash
# Initialize uv project with Python 3.13
uv init --python 3.13

# Create virtual environment
uv venv

# Activate the virtual environment
source .venv/bin/activate
```

### 5. Install Apache Airflow

Set the Airflow home directory:

```bash
export AIRFLOW_HOME=~/airflow
```

Install Apache Airflow 3.1.6 with Python 3.13 constraints:

```bash
uv add "apache-airflow==3.1.6" --constraint https://raw.githubusercontent.com/apache/airflow/constraints-3.1.6/constraints-3.13.txt
```

### 6. Verify Installation

```bash
# Activate virtual environment (if not already activated)
source .venv/bin/activate

# Check Airflow version
airflow version
```

You should see: `3.1.6`

## Next Steps

To start using Airflow:

1. **Initialize the database:**
   ```bash
   source .venv/bin/activate
   airflow db migrate
   ```

2. **Create an admin user:**
   ```bash
   airflow users create \
       --username admin \
       --firstname Admin \
       --lastname User \
       --role Admin \
       --email admin@example.com
   ```

3. **Start the Airflow webserver:**
   ```bash
   airflow webserver --port 8080
   ```

4. **Start the Airflow scheduler (in a new terminal):**
   ```bash
   source .venv/bin/activate
   airflow scheduler
   ```

5. **Access the Airflow UI:**
   Open your browser and navigate to `http://localhost:8080`

## Project Structure

```
apache-airflow-demo/
├── .git/                # Git repository
├── .venv/              # Virtual environment (created by uv)
├── .python-version     # Python version specification (3.13)
├── pyproject.toml      # Project configuration and dependencies
├── main.py             # Main Python file
└── README.md           # This file
```

## Configuration

- **Python Version:** 3.13
- **Airflow Version:** 3.1.6
- **Airflow Home:** `~/airflow`
- **Package Manager:** uv
- **Constraints:** Python 3.13 constraint file from Apache Airflow

## Resources

- [Apache Airflow Documentation](https://airflow.apache.org/docs/apache-airflow/stable/)
- [uv Documentation](https://github.com/astral-sh/uv)
- [GitHub Repository](https://github.com/StephanusSteyn/apache-airflow-demo)
