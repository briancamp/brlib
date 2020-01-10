def mysql_query(query, db, host='localhost', user='root', password=''):
    """
    Run query against database db, with the supplied config.

    Insecure - does not paramaterize queries
    """
    import pymysql
    try:
        db = pymysql.connect(
            host=host, user=user, password=password, db=db,
            cursorclass=pymysql.cursors.DictCursor
        )
    except pymysql.err.OperationalError:
        raise Exception("Couldn't connect to Mysql server %s." % host)

    with db.cursor() as cursor:
        cursor.execute(query)
        results = cursor.fetchall()
        db.commit()

    return(results)


query_txt = 'select * from some_table'
try:
    db_result = mysql_query(query_txt)
    print(db_result.__repr__())
except Exception:
    print(
        'Example works on a local mysql db, user root, no password, '
        'table some_table.')
