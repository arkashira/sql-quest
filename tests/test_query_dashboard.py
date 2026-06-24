import pytest
from datetime import datetime
from query_dashboard import Query, QueryDashboard

@pytest.fixture
def dashboard():
    return QueryDashboard()

def test_add_query(dashboard):
    query = Query(1, 'author1', datetime(2022, 1, 1), 'select * from table', ['tag1'])
    dashboard.add_query(query)
    assert len(dashboard.queries) == 1

def test_search_full_text(dashboard):
    query1 = Query(1, 'author1', datetime(2022, 1, 1), 'select * from table', ['tag1'])
    query2 = Query(2, 'author2', datetime(2022, 1, 2), 'insert into table', ['tag2'])
    dashboard.add_query(query1)
    dashboard.add_query(query2)
    results = dashboard.search('select')
    assert len(results) == 1
    assert results[0].id == 1

def test_search_tags(dashboard):
    query1 = Query(1, 'author1', datetime(2022, 1, 1), 'select * from table', ['tag1'])
    query2 = Query(2, 'author2', datetime(2022, 1, 2), 'insert into table', ['tag2'])
    dashboard.add_query(query1)
    dashboard.add_query(query2)
    results = dashboard.search('', ['tag1'])
    assert len(results) == 1
    assert results[0].id == 1

def test_get_query_metadata(dashboard):
    query = Query(1, 'author1', datetime(2022, 1, 1), 'select * from table', ['tag1'])
    metadata = dashboard.get_query_metadata(query)
    assert metadata['author'] == 'author1'
    assert metadata['last_modified'] == '2022-01-01T00:00:00'
