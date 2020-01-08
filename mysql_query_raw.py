def mysql_query(query, db, host='localhost', user='root', password=''):
    """
    Run query against database db, with the supplied config.

    Insecure - does not paramaterize queries
    """
    import _mysql
    db = _mysql.connect(host, user, password, db)
    db.query(query)
    results = []
    raw_results = db.store_result()
    while True:
        result = raw_results.fetch_row(how=1)
        if not result:
            break
        result = result[0]
        results.append(result)
    return(results)


query_txt = 'select * from some_table'
try:
    db_result = mysql_query(query_txt)
    print(db_result.__repr__())
except Exception:
    print(
        'Example works on a local mysql db, user root, no password, '
        'table some_table.')
