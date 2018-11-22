$(function () {
    // When we're using HTTPS, use WSS too.
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var chatsock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/terminal/" + executionId);

    chatsock.onmessage = function (message) {
        debugger;
        var data = JSON.parse(message.data);
        var chat = $("#conversation")
        var ele = $('<div class="row message-body"></div>')

        if (data.productorid == _productorid) {

            ele.append('<div class="col-sm-12 message-main-sender">' +
                '                        <div class="sender">' +
                '                           <div class="message-text">' +
                '                               <b>' + data.productor + '</b><br>' + data.message +
                '                           </div>' +
                '                        <span class="message-time pull-right">' + data.timestamp + '</span>' +
                '                        </div>' +
                '                   </div>')
        } else {
            ele.append('<div class="row message-body">' +
                '                            <div class="col-sm-12 message-main-receiver">' +
                '                                <div class="receiver">' +
                '                                    <div class="message-text">\n' +
                '                                        <b>'+ data.productor  + '</b><br>' + data.message +
                '                                    </div>' +
                '                                    <span class="message-time pull-right">' +
                '                   <span class="message-time pull-right">' + data.timestamp + '</span>' +
                '                </span>' +
                '                                </div>' +
                '                            </div>' +
                '                        </div>')

        }

        chat.append(ele)
        document.getElementById("terminal-area").scrollTop = document.getElementById("terminal-area").scrollHeight;
    };

    document.getElementById("terminal-area").scrollTop = document.getElementById("terminal-area").scrollHeight;
});