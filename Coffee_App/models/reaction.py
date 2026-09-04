from Coffee_App.models.database import get_db_connection


# 投稿へリアクション
def add_reaction(reaction_type, user_id, post_id):

    conn = get_db_connection()
    cr = conn.cursor()

    try:
        sql = """
            INSERT INTO reactions(reaction_type, user_id, post_id)
            VALUES (%s, %s, %s)
            """

        cr.execute(sql, (reaction_type, user_id, post_id))
        conn.commit()

    except Exception:
        conn.rollback()
        raise

    finally:
        cr.close()
        conn.close()


# リアクションを削除
def delete_reaction(reaction_id):
    conn = get_db_connection()
    cr = conn.cursor()

    try:
        sql = """
            DELETE FROM reactions
            WHERE id = %s
            """

        cr.execute(sql, (reaction_id,))
        conn.commit()

    except Exception:
        conn.rollback()
        raise

    finally:
        cr.close()
        conn.close()


# リアクションの数をカウント


def get_reaction_count(post_id):

    conn = get_db_connection()
    cr = conn.cursor()

    try:
        sql = """
            SELECT COUNT(*) AS reaction_count FROM reactions
            WHERE post_id = %s
        """

        cr.execute(sql, (post_id,))
        result = cr.fetchone()

        return result["reaction_count"]

    finally:
        cr.close()
        conn.close()
