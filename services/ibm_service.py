from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from config.config import Config

class IbmService:

    def __init__(self):
        config = Config()
        ibm_credentials = config.get_ibmcredentials()
        self.version = ibm_credentials.get("version")
        self.api_key = ibm_credentials.get("ibm_key")
        self.service_url = ibm_credentials.get("url")
        self.assistant_id = ibm_credentials.get("assistant_id")
        self.assistant = None
        self.session_id = None
        self._connect_ibm()
        self._create_session()


    def _create_session(self):
        response = self.assistant.create_session(
                    assistant_id=self.assistant_id
                    ).get_result()
        self.session_id = response.get('session_id')
    
    def get_intent(self, message: str):
        response = self.assistant.message(

            assistant_id=self.assistant_id,
            session_id=self.session_id,
            input={
                "message_type":"text",
                "text":message
            }
        ).get_result()
        result = response.get("output")
        intents = result.get("intents")

        if len(intents) > 0:
            return intents[0]

        return None

    def _connect_ibm(self):
        authenticator = IAMAuthenticator(self.api_key)
        self.assistant = AssistantV2(
            version=self.version,
            authenticator=authenticator,
        )
        self.assistant.set_service_url(self.service_url)