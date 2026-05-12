from sqlalchemy import create_engine
from sqlalchemy.engine import Engine, URL
from sqlalchemy.exc import SQLAlchemyError

from pyfabricconnect.core.exceptions import ConnectionError


class SQLAlchemyConnector:

    def __init__(
        self,
        server: str,
        database: str,
        auth,
        driver: str = "ODBC Driver 18 for SQL Server"
    ):
        self.server = server
        self.database = database
        self.auth = auth
        self.driver = driver

    def create_engine(self) -> Engine:
        try:
            connection_url = URL.create(
                "mssql+pyodbc",
                username=self.auth.client_id,
                password=self.auth.client_secret,
                host=self.server,
                database=self.database,
                query={
                    "driver": self.driver,
                    "Authentication": "ActiveDirectoryServicePrincipal",
                    "Encrypt": "yes",
                    "TrustServerCertificate": "no"
                }
            )

            return create_engine(connection_url)

        except SQLAlchemyError as e:
            raise ConnectionError(
                f"SQLAlchemy engine creation failed: {str(e)}"
            ) from e

        except Exception as e:
            raise ConnectionError(
                f"Unexpected SQLAlchemy connector error: {str(e)}"
            ) from e