from pyfabricconnect import FabricClient


def test_client_creation():

    client = FabricClient(
        server="test.fabric.microsoft.com", database="WH_PYFABRICCONNECT", auth=None
    )

    assert client.server == "test.fabric.microsoft.com"
    assert client.database == "WH_PYFABRICCONNECT"
