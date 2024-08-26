document.addEventListener('DOMContentLoaded', function () {
    const roomNameElement = document.getElementById('task-room-name');
    if (roomNameElement) {
        const roomName = roomNameElement.dataset.roomName;

        if (!roomName) {
            console.error("Room name is not defined");
            return;
        }

        let chatSocket;
        if (!window.chatSocket) {
            chatSocket = new WebSocket(
                'ws://' + window.location.host + '/ws/tasks/' + roomName + '/'
            );
            window.chatSocket = chatSocket;
        } else {
            chatSocket = window.chatSocket;
        }

        chatSocket.onmessage = function (e) {
            const data = JSON.parse(e.data);
            console.log("Message received from WebSocket:", data);

            const message = data['message'];
            const username = data['username'];
            const output = document.getElementById('output');

            if (output) {
                output.value += `${username}: ${message}\n`;  // Exibe o nome do usuário e a mensagem
            }
        };

        chatSocket.onclose = function (e) {
            console.error('Chat socket closed unexpectedly');
        };

        document.querySelector('#chatMessageSend').onclick = function(e) {
            const messageInput = document.querySelector('#id_content');
            const message = messageInput.value;
            chatSocket.send(JSON.stringify({
                'message': message
            }));
            messageInput.value = '';  // Limpa o input após enviar
        };
    } else {
        console.error('Element with ID "task-room-name" not found.');
    }
});
