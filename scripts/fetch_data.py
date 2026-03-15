#!/usr/bin/env python3
import os
import csv
import mysql.connector

# === CONFIGURE THESE ===
DB_HOST = os.environ.get("DB_HOST", "db")
DB_USER = os.environ.get("DB_USER", "root")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "")
DB_NAME = os.environ.get("DB_NAME", "coopmart")
OUTPUT_FILE = "data.csv"

def fetch_users(batch_size=10_000):
    """Generator to fetch users from MySQL in batches for memory efficiency."""
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT 
                entity_id,
                sku,
                name,
                price
            FROM catalog_product_flat_1
            ORDER BY entity_id;
        """)

        while True:
            rows = cursor.fetchmany(batch_size)
            if not rows:
                break
            for row in rows:
                yield row
    finally:
        cursor.close()
        connection.close()

def export_to_csv(users_generator):
    """Export users to CSV in a memory-efficient way using a generator."""
    try:
        first_row = next(users_generator)
    except StopIteration:
        print("No users found.")
        return

    keys = first_row.keys()
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerow(first_row)

        count = 1
        for row in users_generator:
            writer.writerow(row)
            count += 1
            if count % 100_000 == 0:
                print(f"Exported {count} users...")

    print(f"Finished exporting {count} users to {OUTPUT_FILE}")

if __name__ == "__main__":
    try:
        print("Fetching users from database...")
        users = fetch_users()
        export_to_csv(users)
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    except Exception as e:
        print(f"Error: {e}")
