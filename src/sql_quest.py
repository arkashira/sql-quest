import json
from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class QueryResult:
    rows: List[List[str]] = None
    error: str = None

class SQLQuest:
    def __init__(self):
        self.data_sources = {
            'Snowflake': self.snowflake_executor,
            'BigQuery': self.bigquery_executor,
            'Redshift': self.redshift_executor
        }
        self.query_log = []

    def execute_query(self, query_id: str, user_id: str, data_source: str, query: str) -> QueryResult:
        if data_source not in self.data_sources:
            return QueryResult(error='Invalid data source')
        try:
            result = self.data_sources[data_source](query)
            self.query_log.append({
                'query_id': query_id,
                'user_id': user_id,
                'data_source': data_source,
                'timestamp': datetime.now().isoformat()
            })
            return result
        except Exception as e:
            return QueryResult(error=str(e))

    def snowflake_executor(self, query: str) -> QueryResult:
        # Simulate Snowflake execution
        return QueryResult(rows=[['row1'], ['row2']])

    def bigquery_executor(self, query: str) -> QueryResult:
        # Simulate BigQuery execution
        return QueryResult(rows=[['row3'], ['row4']])

    def redshift_executor(self, query: str) -> QueryResult:
        # Simulate Redshift execution
        return QueryResult(rows=[['row5'], ['row6']])

    def get_query_log(self) -> List[dict]:
        return self.query_log
