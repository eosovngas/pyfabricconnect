import pandas as pd
import pyodbc

from pyfabricconnect.core.exceptions import ConnectionError, QueryExecutionError


class ODBCConnector:

    def __init__(
        self,
        server: str,
        database: str,
        auth,
        driver: str = "ODBC Driver 18 for SQL Server",
    ):
        self.server = server
        self.database = database
        self.auth = auth
        self.driver = driver

    @property
    def connection_string(self) -> str:
        return (
            f"DRIVER={{{self.driver}}};"
            f"SERVER={self.server};"
            f"DATABASE={self.database};"
            f"UID={self.auth.client_id};"
            f"PWD={self.auth.client_secret};"
            "Authentication=ActiveDirectoryServicePrincipal;"
            "Encrypt=yes;"
            "TrustServerCertificate=no;"
        )

    def query(self, sql: str) -> pd.DataFrame:
        try:
            with pyodbc.connect(self.connection_string) as conn:
                return pd.read_sql(sql, conn)

        except pyodbc.Error as e:
            raise ConnectionError(f"ODBC connection or query failed: {str(e)}") from e

        except Exception as e:
            raise QueryExecutionError(f"Pandas query execution failed: {str(e)}") from e
