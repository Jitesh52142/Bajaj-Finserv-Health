import requests
import json

REGISTRATION_DETAILS = {
    "name": "jitesh bawaskar",
    "regNo": "0832AD221027",  
    "email": "jiteshbawaskar05@gmail.com"
}

GEN_WEBHOOK_URL = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"
SUBMIT_SQL_URL = "https://bfhldevapigw.healthrx.co.in/hiring/testWebhook/PYTHON"

def generate_webhook():
    response = requests.post(GEN_WEBHOOK_URL, json=REGISTRATION_DETAILS)
    if response.status_code == 200:
        data = response.json()
        print("Webhook & Token received.")
        return data['webhook'], data['accessToken']
    else:
        print("Failed to generate webhook.")
        print(response.status_code, response.text)
        return None, None

def submit_query(webhook_url, access_token, final_sql_query):
    headers = {
        "Authorization": access_token,
        "Content-Type": "application/json"
    }
    payload = {
        "finalQuery": final_sql_query
    }
    response = requests.post(SUBMIT_SQL_URL, headers=headers, json=payload)
    if response.status_code == 200:
        print("SQL query submitted successfully!")
        print(response.json())
    else:
        print("Failed to submit query.")
        print(response.status_code, response.text)

if __name__ == "__main__":
    webhook_url, access_token = generate_webhook()

    if webhook_url and access_token:
        final_sql_query = """
        SELECT DISTINCT p.name AS patient_name
        FROM Patients p
        JOIN Appointments a ON p.patient_id = a.patient_id
        JOIN Doctors d ON a.doctor_id = d.doctor_id
        JOIN Departments dept ON d.department_id = dept.department_id
        WHERE dept.name = 'Cardiology';
        """
        submit_query(webhook_url, access_token, final_sql_query)
