#Task 1: Plotting with Pandas
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Define the SQL query
query = """
SELECT last_name, SUM(price * quantity) AS revenue
FROM employees e
JOIN orders o ON e.employee_id = o.employee_id
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY e.employee_id;
"""

# Connect to the database
try:
    with sqlite3.connect('../db/lesson.db') as conn:
        # Load the results into a DataFrame
        df = pd.read_sql_query(query, conn)
        df = df.sort_values(by='revenue', ascending=False)

        #Create a bar chart where the x axis is the employee last name and the y axis is the revenue
        df.plot(x = 'last_name', y = 'revenue', kind="bar", color="skyblue", title='Employee Revenue')
        plt.xlabel('Employee Last Name')
        plt.ylabel('Revenue ($)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        plt.savefig('task1_employee_revenue')
        # Show the plot
        plt.show()
        
except sqlite3.Error as e:
    print(f"Database error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")