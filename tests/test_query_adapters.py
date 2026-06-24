import pytest
from query_adapters import DataWarehouse, QueryVault

def test_add_adapter():
    query_vault = QueryVault()
    config = {"username": "user", "password": "pass"}
    query_vault.add_adapter(DataWarehouse.SNOWFLAKE, config)
    assert query_vault.get_adapter(DataWarehouse.SNOWFLAKE).config == config

def test_integrate():
    query_vault = QueryVault()
    config = {"username": "user", "password": "pass"}
    query_vault.add_adapter(DataWarehouse.SNOWFLAKE, config)
    assert query_vault.integrate(DataWarehouse.SNOWFLAKE) == "Integrated with snowflake"

def test_use_query_template():
    query_vault = QueryVault()
    config = {"username": "user", "password": "pass"}
    query_vault.add_adapter(DataWarehouse.SNOWFLAKE, config)
    assert query_vault.use_query_template(DataWarehouse.SNOWFLAKE, "SELECT * FROM table") == "Used query template 'SELECT * FROM table' with snowflake"

def test_integrate_no_adapter():
    query_vault = QueryVault()
    with pytest.raises(ValueError):
        query_vault.integrate(DataWarehouse.SNOWFLAKE)

def test_use_query_template_no_adapter():
    query_vault = QueryVault()
    with pytest.raises(ValueError):
        query_vault.use_query_template(DataWarehouse.SNOWFLAKE, "SELECT * FROM table")
