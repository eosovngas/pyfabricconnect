# PyFabricConnect

Unified Python connectivity toolkit for Microsoft Fabric Warehouses, Lakehouses, and SQL Analytics Endpoints.

PyFabricConnect simplifies secure connectivity to Microsoft Fabric using modern authentication methods and multiple connector backends including JDBC, ODBC, and SQLAlchemy.

---

# Features

- JDBC connectivity for Spark workloads
- ODBC connectivity using pyodbc
- SQLAlchemy integration
- Service Principal authentication
- OAuth Access Token authentication
- Pandas DataFrame support
- Spark DataFrame support
- Unified authentication abstraction
- Enterprise-ready architecture

---

# Supported Technologies

| Technology | Supported |
|---|---|
| Microsoft Fabric Warehouse | ✅ |
| Lakehouse SQL Endpoint | ✅ |
| Spark JDBC | ✅ |
| pyodbc | ✅ |
| SQLAlchemy | ✅ |
| Pandas | ✅ |
| PySpark | ✅ |

---

# Installation

```bash
pip install pyfabricconnect
```

---

# Quick Start

## Service Principal Authentication

```python
from pyfabricconnect import FabricClient
from pyfabricconnect.auth import ServicePrincipalAuth

auth = ServicePrincipalAuth(
    tenant_id="YOUR_TENANT_ID",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET"
)

client = FabricClient(
    server="YOUR_SERVER",
    database="WH_PYFABRICCONNECT",
    auth=auth
)

df = client.query_pandas("""
SELECT * FROM dbo.qlbacan
""")

print(df.head())
```

---

# Spark Example

```python
spark_df = client.query_spark("""
SELECT * FROM dbo.qlbacan
""")

spark_df.show()
```

---

# SQLAlchemy Example

```python
engine = client.engine()
```

---

# Project Structure

```text
pyfabricconnect/
│
├── pyfabricconnect/
│   ├── auth/
│   ├── connectors/
│   ├── core/
│   └── utils/
│
├── tests/
├── examples/
├── README.md
├── LICENSE
├── pyproject.toml
└── .gitignore
```

---

# Project Status

PyFabricConnect is currently under active development.

---

# Roadmap

## v0.1.0

- JDBC Connector
- ODBC Connector
- SQLAlchemy Connector
- Service Principal Authentication
- OAuth Token Authentication

## Future Releases

- Managed Identity
- Token Refresh
- Retry Policies
- Structured Logging
- Async Support
- Connection Pooling

---

# Contributing

Contributions, issues, and feature requests are welcome.

---

# Support the Project

If PyFabricConnect helps your projects or organization, consider supporting development in the future through:

- GitHub Sponsors
- PayPal
- Buy Me a Coffee

---

# Support the Project

If PyFabricConnect helps your projects or organization, consider supporting development.

Your support helps maintain:

- Fabric integrations
- Authentication improvements
- New connectors
- Documentation
- Community support

## Donations
- [PayPal Donations](https://paypal.me/eosovngas)
---

# License

Apache License 2.0

Copyright 2026 Eduardo Osorio Venegas - EOSOVNGAS