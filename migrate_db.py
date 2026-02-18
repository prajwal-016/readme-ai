import sqlite3
import os

def migrate():
    try:
        # Ensure the directory for the database exists
        if not os.path.exists('instance'):
            os.makedirs('instance')
            
        conn = sqlite3.connect('instance/database.db')
        cursor = conn.cursor()
        
        # New columns to add
        columns = [
            ('features', 'TEXT'),
            ('installation', 'TEXT'),
            ('usage', 'TEXT'),
            ('tech_stack', 'TEXT'),
            ('author', 'VARCHAR(200)'),
            ('github_link', 'VARCHAR(500)')
        ]
        
        for col_name, col_type in columns:
            try:
                cursor.execute(f"ALTER TABLE readme_record ADD COLUMN {col_name} {col_type}")
                print(f"Added column: {col_name}")
            except sqlite3.OperationalError as e:
                # Column might already exist
                print(f"Notice: {e}")
        
        conn.commit()
        conn.close()
        print("Migration completed successfully.")
    except Exception as e:
        print(f"Migration failed: {e}")

if __name__ == "__main__":
    migrate()
