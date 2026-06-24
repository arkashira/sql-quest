import json
from dataclasses import dataclass
from enum import Enum
from typing import Dict

class DataWarehouse(Enum):
    SNOWFLAKE = "snowflake"
    BIGQUERY = "bigquery"
    REDSHIFT = "redshift"
    POSTGRES = "postgres"

@dataclass
class QueryAdapter:
    data_warehouse: DataWarehouse
    config: Dict[str, str]

    def integrate(self):
        # Simulate integration with the data warehouse
        return f"Integrated with {self.data_warehouse.value}"

    def use_query_template(self, query_template: str):
        # Simulate using a query template with the data warehouse
        return f"Used query template '{query_template}' with {self.data_warehouse.value}"

class QueryVault:
    def __init__(self):
        self.adapters = {}

    def add_adapter(self, data_warehouse: DataWarehouse, config: Dict[str, str]):
        self.adapters[data_warehouse] = QueryAdapter(data_warehouse, config)

    def get_adapter(self, data_warehouse: DataWarehouse):
        return self.adapters.get(data_warehouse)

    def integrate(self, data_warehouse: DataWarehouse):
        adapter = self.get_adapter(data_warehouse)
        if adapter:
            return adapter.integrate()
        else:
            raise ValueError(f"No adapter found for {data_warehouse.value}")

    def use_query_template(self, data_warehouse: DataWarehouse, query_template: str):
        adapter = self.get_adapter(data_warehouse)
        if adapter:
            return adapter.use_query_template(query_template)
        else:
            raise ValueError(f"No adapter found for {data_warehouse.value}")
