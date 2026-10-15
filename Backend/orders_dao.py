from datetime import date
from sql_connection import get_sql_connection

def insert_order(connection, order):
    cursor = connection.cursor()

    query = ("INSERT INTO orders (customer_name, total, date) VALUES (%s, %s, %s)")
    data = (order['customer_name'], order['total'], date.today())
    cursor.execute(query, data)
    order_id = cursor.lastrowid

    order_details_query = ("INSERT INTO order_details (order_id, product_id, quantity, total_price) VALUES (%s, %s, %s, %s)")
    order_details_data = []
    for order_detail_record in order['order_details']:
        order_details_data.append([
            order_id,
            int(order_detail_record['product_id']),
            float(order_detail_record['quantity']), 
            float(order_detail_record['total_price'])
        ])
    cursor.executemany(order_details_query, order_details_data)

    connection.commit()
    return order_id

def get_all_orders(connection):
    cursor = connection.cursor()
    query = ("SELECT * FROM orders")
    cursor.execute(query)

    response = []
    for (order_id, customer_name, total, order_date) in cursor:
        response.append({
            'order_id': order_id,
            'customer_name': customer_name,
            'total': total,
            'date': order_date
        })
    return response

if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_all_orders(connection))

if __name__ == '__main__':
    connection = get_sql_connection()
    print(insert_order(connection, {
        'customer_name': 'Ironman',
        'total': '500',
        'order_details': [
            {
                'product_id': 1,
                'quantity': 2,
                'total_price': 50
            },
            {
                'product_id': 3,
                'quantity': 1,
                'total_price': 30
            }
        ]
    }))