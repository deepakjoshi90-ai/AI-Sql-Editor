from utils.gemini import ask_gemini
from utils.schema import get_database_schema
from utils.sql_executor import execute_sql


def audit_sql(sql_query):

    schema = get_database_schema()

    result = execute_sql(sql_query)

    if result["success"]:
        sql_error = "None"
        execution_result = f"""
Columns: {result["columns"]}
Rows: {result["rows"]}
"""
    else:
        sql_error = result["error"]
        execution_result = "SQL execution failed."

    prompt = f"""
You are an expert SQL auditor and SQL interview mentor.

DATABASE SCHEMA:
{schema}

USER SQL QUERY:
{sql_query}

SQL EXECUTION RESULT:
{execution_result}

SQL ERROR:
{sql_error}

Analyze the SQL query using the database schema and the actual SQL execution result.

Return your answer in exactly this structure:

STATUS:
Correct or Incorrect

PROBLEM:
Explain the main problem, if any.

EXPLANATION:
Explain what the SQL query is doing and why it is correct or incorrect.

CORRECTED SQL:
Provide corrected SQL if the query is incorrect.
If it is correct, write:
No correction required.

INTERVIEW TIP:
Give one useful SQL interview tip related to this query.

Keep the explanation beginner-friendly and concise.
"""

    return ask_gemini(prompt)