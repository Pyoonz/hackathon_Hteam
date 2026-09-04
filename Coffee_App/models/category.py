from Coffee_App.models.database import get_db_connection


# カテゴリ一覧を取得
def get_categories():
    conn = get_db_connection()
    cr = conn.cursor()

    try:
        sql = """
            SELECT 
            categories.id, categories.category_name
            FROM categories;
        """
        cr.execute(sql)
        categories = cr.fetchall()

        return categories
    finally:
        cr.close()
        conn.close()


# 特定のカテゴリを取得
def get_category(category_id):
    conn = get_db_connection()
    cr = conn.cursor()

    try:
        sql = """
            SELECT 
            id, category_name 
            FROM categories WHERE id=%s;
            """
        cr.execute(sql, (category_id,))
        category_name = cr.fetchone()

        return category_name
    finally:
        cr.close()
        conn.close()
