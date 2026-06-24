import json
from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class Query:
    id: int
    author: str
    last_modified: datetime
    text: str
    tags: List[str]

class QueryDashboard:
    def __init__(self):
        self.queries = []

    def add_query(self, query: Query):
        self.queries.append(query)

    def search(self, query_text: str, tags: List[str] = None) -> List[Query]:
        results = []
        for q in self.queries:
            if query_text.lower() in q.text.lower():
                if tags is None or any(tag.lower() in [t.lower() for t in q.tags] for tag in tags):
                    results.append(q)
        return results

    def get_query_metadata(self, query: Query) -> dict:
        return {
            'author': query.author,
            'last_modified': query.last_modified.isoformat()
        }
