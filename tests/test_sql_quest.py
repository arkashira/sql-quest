import pytest
from sql_quest import SQLQuest, QueryResult

def test_execute_query_snowflake():
    sql_quest = SQLQuest()
    result = sql_quest.execute_query('query1', 'user1', 'Snowflake', 'SELECT * FROM table')
    assert result.rows == [['row1'], ['row2']]
    assert result.error is None

def test_execute_query_bigquery():
    sql_quest = SQLQuest()
    result = sql_quest.execute_query('query2', 'user2', 'BigQuery', 'SELECT * FROM table')
    assert result.rows == [['row3'], ['row4']]
    assert result.error is None

def test_execute_query_redshift():
    sql_quest = SQLQuest()
    result = sql_quest.execute_query('query3', 'user3', 'Redshift', 'SELECT * FROM table')
    assert result.rows == [['row5'], ['row6']]
    assert result.error is None

def test_execute_query_invalid_data_source():
    sql_quest = SQLQuest()
    result = sql_quest.execute_query('query4', 'user4', 'Invalid', 'SELECT * FROM table')
    assert result.error == 'Invalid data source'
    assert result.rows is None

def test_get_query_log():
    sql_quest = SQLQuest()
    sql_quest.execute_query('query5', 'user5', 'Snowflake', 'SELECT * FROM table')
    log = sql_quest.get_query_log()
    assert len(log) == 1
    assert log[0]['query_id'] == 'query5'
    assert log[0]['user_id'] == 'user5'
    assert log[0]['data_source'] == 'Snowflake'
