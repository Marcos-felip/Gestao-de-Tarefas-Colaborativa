import json
from channels.generic.websocket import AsyncWebsocketConsumer
from tasks.models import Comment, Task
from channels.db import database_sync_to_async
from users.models import UserProfile

class CommentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Obtém o nome da sala a partir da URL
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'task_{self.room_name}'

        # Adiciona o consumidor ao grupo da sala
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Remove o consumidor do grupo da sala
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Recebe e processa os dados enviados pelo WebSocket
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        UserProfile = self.scope['user']  # Obtém o usuário autenticado
        username = UserProfile.username if UserProfile.is_authenticated else 'Anonymous'

        # Salva a mensagem no banco de dados
        await self.save_comment(message, username)

        # Envia a mensagem para o grupo da sala
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )

    async def chat_message(self, event):
        # Envia a mensagem recebida para o WebSocket
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))

    @database_sync_to_async
    def save_comment(self, message, username):
        # Salva o comentário no banco de dados
        task = Task.objects.get(id=self.room_name)  # Obtém a tarefa baseada no room_name
        user = UserProfile.objects.get(username=username)  # Obtém o usuário baseado no nome de usuário
        Comment.objects.create(task=task, user=user, content=message)
