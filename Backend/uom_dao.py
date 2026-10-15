def get_uoms(connection):
    cursor = connection.cursor()
    query = ("Select * from uom")
    cursor.execute(query)

    ressponse = []
    for (uom_id, uom_name) in cursor:
        ressponse.append({
            'uom_id': uom_id,
            'uom_name': uom_name
        })
    return ressponse

if __name__ == "__main__":
    from sql_connection import get_sql_connection
    connection = get_sql_connection()
    print(get_uoms(connection))