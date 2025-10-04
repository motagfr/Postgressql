

# Update these with your actual database connection details
DB_HOST = 'localhost'
DB_PORT = 5432
DB_NAME = 'dvdrental'
DB_USER = 'postgres'
DB_PASS = '1234'

# SQLAlchemy connection string
conn_str = f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# SQL query for monthly sales
db_query = '''
SELECT TO_CHAR(payment_date, 'YYYY-MM') AS month, SUM(amount) AS total_sales
FROM payment
GROUP BY month
ORDER BY month;
'''


def fetch_data(query):
    engine = create_engine(conn_str)
    df = pd.read_sql_query(query, engine)
    engine.dispose()
    return df

# 1. Top Film Categories (Bar Chart)


def plot_top_categories():
    query = '''
    SELECT name AS category, COUNT(*) AS film_count
    FROM category
    JOIN film_category USING (category_id)
    GROUP BY name
    ORDER BY film_count DESC
    LIMIT 10;
    '''
    df = fetch_data(query)
    plt.figure(figsize=(10, 6))
    plt.bar(df['category'], df['film_count'], color='skyblue')
    plt.title('Top 10 Film Categories by Number of Films')
    plt.xlabel('Category')
    plt.ylabel('Number of Films')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# 2. Film Ratings Distribution (Pie Chart)


def plot_ratings_distribution():
    query = '''
    SELECT rating, COUNT(*) AS film_count
    FROM film
    GROUP BY rating
    ORDER BY film_count DESC;
    '''
    df = fetch_data(query)
    plt.figure(figsize=(8, 8))
    plt.pie(df['film_count'], labels=df['rating'],
            autopct='%1.1f%%', startangle=140)
    plt.title('Film Ratings Distribution')
    plt.tight_layout()
    plt.show()

# 3. Top Categories by Sales (Bar Chart)


def plot_top_categories_by_sales():
    query = '''
    SELECT c.name AS category, SUM(p.amount) AS total_sales
    FROM payment p
    JOIN rental r ON p.rental_id = r.rental_id
    JOIN inventory i ON r.inventory_id = i.inventory_id
    JOIN film f ON i.film_id = f.film_id
    JOIN film_category fc ON f.film_id = fc.film_id
    JOIN category c ON fc.category_id = c.category_id
    GROUP BY c.name
    ORDER BY total_sales DESC
    LIMIT 10;
    '''
    df = fetch_data(query)
    plt.figure(figsize=(10, 6))
    plt.bar(df['category'], df['total_sales'], color='orange')
    plt.title('Top 10 Film Categories by Sales')
    plt.xlabel('Category')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_monthly_sales():
    df = fetch_data(db_query)
    plt.figure(figsize=(10, 6))
    plt.plot(df['month'], df['total_sales'], marker='o')
    plt.title('Monthly Total Sales')
    plt.xlabel('Month')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    print('Monthly Sales Trend:')
    plot_monthly_sales()
    print('Top Film Categories:')
    plot_top_categories()
    print('Film Ratings Distribution:')
    plot_ratings_distribution()
    print('Top Categories by Sales:')
    plot_top_categories_by_sales()
