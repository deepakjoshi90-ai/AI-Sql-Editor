from utils.db import get_connection


def execute_sql(sql_query):

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(sql_query)

        # SELECT query
        if cursor.description:
            columns = [column[0] for column in cursor.description]
            rows = cursor.fetchall()

            return {
                "success": True,
                "columns": columns,
                "rows": rows,
                "error": None
            }

        # INSERT / UPDATE / DELETE
        connection.commit()

        return {
            "success": True,
            "columns": [],
            "rows": [],
            "error": None
        }

    except Exception as e:

        return {
            "success": False,
            "columns": [],
            "rows": [],
            "error": str(e)
        }

    finally:
        cursor.close()
        connection.close()