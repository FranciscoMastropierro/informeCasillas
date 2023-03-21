from exchangelib import (
    Account,
    Identity,
    Configuration,
    OAuth2Credentials,
    DELEGATE,
    OAUTH2,
)
from dotenv import dotenv_values

__name__ == '__main__' 

config = dotenv_values(".env") 

def Cuenta(mail):
        """
        Devuelve la conexión con la cuenta de correo pasada por parametro.

        :param mail: Debe ser un correo.
        :return: Account
        :rtype: exchangelib.Account
        """
        client_id = list(config.items())[0][1]
        tenant_id = list(config.items())[1][1]
        secret_value = list(config.items())[2][1]
        cuenta_destino = mail

        credentials = OAuth2Credentials(
            client_id=client_id,
            tenant_id=tenant_id,
            client_secret=secret_value,
            identity=Identity(primary_smtp_address=cuenta_destino)
        )
        conf = Configuration(
            credentials=credentials,
            server= list(config.items())[3][1],
            auth_type=OAUTH2
        )
        account = Account(
            primary_smtp_address=cuenta_destino,
            autodiscover=False,
            config=conf,
            access_type=DELEGATE,
        )
        print(account)
        return account
