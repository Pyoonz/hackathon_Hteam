from Coffee_App.database import get_db


class User:
    def __init__(
        self,
        id,
        username,
        email,
        password_hash,
        created_at=None,
        updated_at=None,
        deleted_at=None,
        profile_image_url=None,
        profile_text=None,
        beans_color=1
    ):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at
        self.profile_image_url = profile_image_url
        self.profile_text = profile_text
        self.beans_color = beans_color

    @staticmethod
    def find_by_email(email):
        connection = get_db()

        with connection.cursor() as cursor:
            sql = """
                SELECT *
                FROM users
                WHERE email = %s
            """

            cursor.execute(sql, (email,))
            return cursor.fetchone()

    @staticmethod
    def create(username, email, password_hash):
        connection = get_db()

        try:
            with connection.cursor() as cursor:
                sql = """
                    INSERT INTO users (
                        username,
                        email,
                        password_hash
                    )
                    VALUES (
                        %s,
                        %s,
                        %s
                    )
                """

                cursor.execute(
                    sql,
                    (username, email, password_hash)
                )

            connection.commit()

        except Exception:
            connection.rollback()
            raise

    @staticmethod
    def find_by_id(user_id):
        connection = get_db()

        with connection.cursor() as cursor:
            sql = """
                SELECT *
                FROM users
                WHERE id = %s
                    AND deleted_at IS NULL
            """

            cursor.execute(sql, (user_id,))
            return cursor.fetchone()

    @staticmethod
    def update(user_id, username, profile_text):
        connection = get_db()

        try:
            with connection.cursor() as cursor:
                sql = """
                    UPDATE users
                    SET
                        username = %s,
                        profile_text = %s,
                        updated_at = CURRENT_TIMESTAMP
                    WHERE id = %s
                """

                cursor.execute(
                    sql,
                    (username, profile_text, user_id)
                )

            connection.commit()

        except Exception:
            connection.rollback()
            raise


    @staticmethod
    def delete(user_id):
        connection = get_db()

        try:
            with connection.cursor() as cursor:
                sql = """
                    UPDATE users
                    SET
                        deleted_at = CURRENT_TIMESTAMP,
                        updated_at = CURRENT_TIMESTAMP
                    WHERE id = %s
                """

                cursor.execute(
                    sql,
                    (user_id,)
                )

            connection.commit()

        except Exception:
            connection.rollback()
            raise


    @staticmethod
    def find_active_by_email(email):
        connection = get_db()

        with connection.cursor() as cursor:
            sql = """
                SELECT *
                FROM users
                WHERE email = %s
                AND deleted_at IS NULL
            """

            cursor.execute(sql, (email,))
            return cursor.fetchone()
