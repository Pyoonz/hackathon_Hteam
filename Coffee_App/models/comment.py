from Coffee_App.models.database import get_db_connection


# コメント一覧の取得
def get_comments(post_id):

    conn = get_db_connection()
    cr = conn.cursor()

    try:
        sql = """
            SELECT 
            comments.content, users.username, comments.created_at, comments.id
            FROM comments 
            JOIN users 
            ON comments.user_id = users.id  
            WHERE post_id=%s;
        """
        cr.execute(sql, (post_id,))
        comments = cr.fetchall()
        return comments

    finally:
        cr.close()
        conn.close()


# コメントの削除
def delete_comments(comment_id):
    conn = get_db_connection()
    cr = conn.cursor()

    try:
        sql = """
            DELETE FROM comments 
            WHERE id=%s;
        """
        cr.execute(sql, (comment_id,))
        conn.commit()

    except Exception:
        conn.rollback()
        raise

    finally:
        cr.close()
        conn.close()


# コメントの投稿
def post_comments(content, user_id, post_id):
    conn = get_db_connection()
    cr = conn.cursor()

    try:
        sql = """
        INSERT INTO comments (content, user_id, post_id) 
        VALUES (%s, %s, %s);
    """
        cr.execute(sql, (content, user_id, post_id))
        conn.commit()

    except Exception:
        conn.rollback()
        raise

    finally:
        cr.close()
        conn.close()
