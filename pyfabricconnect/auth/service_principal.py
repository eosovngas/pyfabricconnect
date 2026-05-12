from azure.identity import ClientSecretCredential

from pyfabricconnect.core.exceptions import AuthenticationError


class ServicePrincipalAuth:

    def __init__(self, tenant_id: str, client_id: str, client_secret: str):
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret

    def get_token(self) -> str:

        try:

            credential = ClientSecretCredential(
                tenant_id=self.tenant_id,
                client_id=self.client_id,
                client_secret=self.client_secret,
            )

            token = credential.get_token("https://database.windows.net/.default")

            return token.token

        except Exception as e:
            raise AuthenticationError(f"Failed to acquire token: {str(e)}") from e
