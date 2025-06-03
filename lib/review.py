from ..config import CONN, CURSOR

class Review:
    all = {}

    def __init__(self, year, summary, employee, id=None):
        self.id = id
        self.year = year
        self.summary = summary
        self.employee = employee

    def __repr__(self):
        return f"<Review {self.id}: {self.year}, {self.summary[:20]}...>"

    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY,
            year INTEGER,
            summary TEXT,
            employee_id INTEGER,
            FOREIGN KEY (employee_id) REFERENCES employees(id)
        )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        CURSOR.execute("DROP TABLE IF EXISTS reviews")
        CONN.commit()
