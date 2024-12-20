class Mensagem:

    def __init__(self):
        pass
    def enviar_mensagem(self):
        pass
    
class Email(Mensagem):
    def __init__(self, destinatario, assunto, corpo):
        self.destinatario = destinatario
        self.assunto = assunto
        self.corpo = corpo
        super().__init__()
    
    def enviar_mensagem(self):
        print(f"Email({self.destinatario}). Assunto: {self.assunto}")

class SMS(Mensagem):
    def __init__(self, numero, mensagem):
        self.numero = numero
        self.mensagem = mensagem
        super().__init__()
    
    def enviar_mensagem(self):
        print(f"SMS({self.numero}). {self.mensagem}")

class NotificacaoPush(Mensagem):
    def __init__(self, mensagem, dispositivo_id):
        self.mensagem = mensagem
        self.dispositivo_id = dispositivo_id
        super().__init__()
    
    def enviar_mensagem(self):
        print(f"Notificação Push({self.dispositivo_id}). {self.mensagem}")

def realizar_envio(objeto):
    objeto.enviar_mensagem()

email = Email(destinatario="joao.silva@email.com", assunto="Reunião", corpo="Reunião marcada para as 10h.")
sms = SMS(numero="912345678", mensagem="A sua Encomenda Chegou!")
notificacao = NotificacaoPush(dispositivo_id="abc123", mensagem="Tem uma Nova Mensagem.")

realizar_envio(email)
realizar_envio(sms)
realizar_envio(notificacao)