# Bajaj Finserv Health Qualifier Test :

## Overview

This Python script is designed to solve the SQL problem presented in the **Bajaj Finserv Health Qualifier 1 Challenge**. It works by:

1. **Generating a webhook** on startup.
2. **Identifying the question** based on the registration number (odd or even).
3. **Submitting the correct SQL query** to a given endpoint.

---

## Candidate Information

- **Name**: Jitesh Bawaskar
- **Registration Number**: 0832AD221027
- **Email**: jiteshbawaskar05@gmail.com

---

## How It Works

The script automates the following steps:

1. When the script runs, it sends a registration request to generate a webhook URL and an authentication token.
2. Based on the last digit of the registration number (odd or even), the correct SQL query is determined and executed.
3. The SQL query is then sent to the webhook for validation.

