from pyfabricconnect import FabricClient
from pyfabricconnect.auth import ServicePrincipalAuth

auth = ServicePrincipalAuth(
    tenant_id="YOUR_TENANT_ID",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)

client = FabricClient(server="YOUR_SERVER", database="WH_PYFABRICCONNECT", auth=auth)

df = client.query_pandas("SELECT TOP 10 * FROM dbo.certificadosmaterial")

print(df.head())
