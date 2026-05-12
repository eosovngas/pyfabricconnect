from pyfabricconnect.core.exceptions import QueryExecutionError


class JDBCConnector:

    def __init__(self, spark, server: str, database: str, auth):
        self.spark = spark
        self.server = server
        self.database = database
        self.auth = auth

    @property
    def jdbc_url(self) -> str:
        return (
            f"jdbc:sqlserver://{self.server}:1433;"
            f"database={self.database};"
            "encrypt=true;"
            "trustServerCertificate=false;"
            "hostNameInCertificate=*.datawarehouse.fabric.microsoft.com;"
            "authentication=ActiveDirectoryServicePrincipal;"
        )

    def query(self, sql: str):
        try:
            return (
                self.spark.read.format("jdbc")
                .option("url", self.jdbc_url)
                .option("query", sql)
                .option("user", self.auth.client_id)
                .option("password", self.auth.client_secret)
                .option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver")
                .load()
            )

        except Exception as e:
            raise QueryExecutionError(f"Spark JDBC query failed: {str(e)}") from e
