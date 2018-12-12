$(function () {
    // When we're using HTTPS, use WSS too.
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var chatsock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/ws/terminal/" + executionId);

    chatsock.onmessage = function (message) {
        var data = JSON.parse(message.data);
        var chat = $("#terminal-area")
        chat.append(data.message)
        document.getElementById("terminal-area").scrollTop = document.getElementById("terminal-area").scrollHeight;
    };

    document.getElementById("terminal-area").scrollTop = document.getElementById("terminal-area").scrollHeight;
});