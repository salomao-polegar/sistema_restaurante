from common.interfaces import MercadoPagoInterface
import requests, uuid

class MercadoPagoConnection (MercadoPagoInterface):
    
    def enviar_pagamento(self, payment_data):
        try:
            response = requests.post("urlmercadolivre", json=payment_data)
            
            if response.status_code == 200: 
                return response.json()
        except:
            return {"id_pagamento":str(uuid.uuid4())}