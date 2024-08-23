// const input = document.querySelector('#id_content')
// const output = document.querySelector('#output')

// input.addEventListener('keypress', e => {
//     console.log(e)
//     if(e.code === 'Enter'){

//     }
// })

document.addEventListener('DOMContentLoaded', function() {
    // Supondo que você está passando `room_name_json` através de um objeto global ou similar
    var roomName = window.roomName;

    var chatSocket = new WebSocket(
        'ws://' + window.location.host +
        '/ws/chat/' + roomName + '/');

    chatSocket.onmessage = function(e) {
        var data = JSON.parse(e.data);
        var message = data['message'];
        document.querySelector('#form-control').value += (message + '\n');
    };

    chatSocket.onclose = function(e) {
        console.error('Chat fechado inesperadamente');
    };

    document.querySelector('#id_content').focus();
    document.querySelector('#id_content').onkeyup = function(e) {
        if (e.keyCode === 13) {  // enter, return
            document.querySelector('#chatMessageSend').click();
        }
    };

    document.querySelector('#chatMessageSend').onclick = function(e) {
        var messageInputDom = document.querySelector('#id_content');
        var message = messageInputDom.value;
        chatSocket.send(JSON.stringify({
            'message': message
        }));

        messageInputDom.value = '';
    };
});

