def reviews(self):
    from .review import Review  # import inside to avoid circular import
    sql = "SELECT * FROM reviews WHERE employee_id = ?"
    CURSOR.execute(sql, (self.id,))
    rows = CURSOR.fetchall()
    return [Review.instance_from_db(row) for row in rows]


       