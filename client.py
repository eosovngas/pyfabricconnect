from pyfabricconnect.connectors.jdbc import JDBCConnector
from pyfabricconnect.connectors.odbc import ODBCConnector
from pyfabricconnect.connectors.sqlalchemy import SQLAlchemyConnector


class FabricClient:
    def __init__(
        self,
        server: str,
        database: str,
        auth,
        spark=None,
    ):
        self.server = server
        self.database = database
        self.auth = auth
        self.spark = spark

    def __repr__(self):
        return f"FabricClient(server='{self.server}', " f"database='{self.database}')"

    def query_spark(self, sql: str):
        if self.spark is None:
            raise ValueError(
                "query_spark() requires an active SparkSession. "
                "Pass spark when creating FabricClient: "
                "FabricClient(..., spark=spark)"
            )

        connector = JDBCConnector(
            spark=self.spark,
            server=self.server,
            database=self.database,
            auth=self.auth,
        )

        return connector.query(sql)

    def query_pandas(self, sql: str):
        connector = ODBCConnector(
            server=self.server,
            database=self.database,
            auth=self.auth,
        )

        return connector.query(sql)

    def engine(self):
        connector = SQLAlchemyConnector(
            server=self.server,
            database=self.database,
            auth=self.auth,
        )

        return connector.create_engine()
