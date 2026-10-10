from utils.db import get_connection


def get_database_schema():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()

    schema = ""

    for table in tables:
        table_name = table[0]

        schema += f"\nTable: {table_name}\n"

        cursor.execute(f"DESCRIBE `{table_name}`")
        columns = cursor.fetchall()

        for column in columns:
            schema += f"- {column[0]} ({column[1]})\n"

    cursor.close()
    connection.close()

    return schema