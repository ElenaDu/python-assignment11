#Task 2: A Line Plot with Pandas
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Define the SQL query
query = """
SELECT o.order_id, SUM(p.price * l.quantity) AS total_price
FROM orders o
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id;
"""

try:
    
    with sqlite3.connect('../db/lesson.db') as conn:
         # Load the results into a DataFrame
        df = pd.read_sql_query(query, conn)
        #Add a "cumulative" column to the DataFrame
        df['cumulative'] = df['total_price'].cumsum()

        # Plot the cumulative revenue
        df.plot(x = 'order_id', y = 'cumulative', kind='line', color='green', title='Cumulative Revenue By Order')
        plt.xlabel('Order ID')
        plt.ylabel('Cumulative Revenue ($)')  
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('task2_cumulative_revenue')
        # Show the plot
        plt.show()

except sqlite3.Error as e:
    print(f"Database error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")