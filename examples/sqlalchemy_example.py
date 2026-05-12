import pandas as pd

from pyfabricconnect import FabricClient
from pyfabricconnect.auth import ServicePrincipalAuth

auth = ServicePrincipalAuth(
    tenant_id="YOUR_TENANT_ID",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)

client = FabricClient(server="YOUR_SERVER", database="WH_PYFABRICCONNECT", auth=auth)

engine = client.engine()

with engine.connect() as conn:

    df = pd.read_sql("SELECT TOP 10 * FROM dbo.certificadosmaterial", conn)

print(df.head())
