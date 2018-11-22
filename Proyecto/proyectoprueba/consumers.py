import json
import logging
from channels.sessions import channel_session
from testcore.models import TestExecution

log = logging.getLogger(__name__)

# In consumers.py
from channels import Group

# Connected to websocket.connect
@channel_session
def ws_add(message):
    prefix, testHash = message['path'].strip('/').split('/')
    # testExe = TestExecution.objects.get(executionhash=testHash)

    # Accept the connection
    message.reply_channel.send({"accept": True})
    # Add to the chat group
    Group('terminal-' + testHash).add(message.reply_channel)


# Connected to websocket.receive
def ws_message(message, testHash):
    # Look up the room from the channel session, bailing if it doesn't exist
    # See above for the note about Group
    Group('terminal-' + testHash).send(
        {'text': message})


# Connected to websocket.disconnect
@channel_session
def ws_disconnectNew(message):
    Group("chat").discard(message.reply_channel)


# inmmemory
@channel_session
def ws_echo(message):
    message.reply_channel.send({
        'text': message.content['text'],
    })


@channel_session
def ws_connect1(message):
    log.debug('Se trata de conectar a el socket')
    # message.channel_session['room'] = u'343'
    # Add to reader group
    Group("liveblog").add(message.reply_channel)
    # Accept the connection request
    message.reply_channel.send({"accept": True})


@channel_session
# Connected to websocket.disconnect
def ws_disconnect1(message):
    # Remove from reader group on clean disconnect
    Group("liveblog").discard(message.reply_channel)


# redis


@channel_session
def ws_connect(message):
    # Extract the room from the message. This expects message.path to be of the
    # form /chat/{label}/, and finds a Room if the message path is applicable,
    # and if the Room exists. Otherwise, bails (meaning this is a some othersort
    # of websocket). So, this is effectively a version of _get_object_or_404.
    try:
        prefix, label = message['path'].decode('ascii').strip('/').split('/')
        if prefix != 'organico_cooperativas':
            log.debug('invalid ws path=%s', message['path'])
            return
        room = Room.objects.get(label=label)
    except ValueError:
        log.debug('invalid ws path=%s', message['path'])
        return
    except Room.DoesNotExist:
        log.debug('ws room does not exist label=%s', label)
        return

    log.debug('chat connect room=%s client=%s:%s',
              room.label, message['client'][0], message['client'][1])

    # Need to be explicit about the channel layer so that testability works
    # This may be a FIXME?
    Group('organico_cooperativas-' + label, channel_layer=message.channel_layer).add(message.reply_channel)

    message.channel_session['room'] = room.label

    # Accept the connection request
    message.reply_channel.send({"accept": True})


def ws_receive(message):
    # Look up the room from the channel session, bailing if it doesn't exist
    try:
        label = message.channel_session['room']
        room = Room.objects.get(label=label)
    except KeyError:
        log.debug('no room in channel_session')
        return
    except Room.DoesNotExist:
        log.debug('recieved message, buy room does not exist label=%s', label)
        return

    # Parse out a chat message from the content text, bailing if it doesn't
    # conform to the expected message format.
    try:
        data = json.loads(message['text'])
    except ValueError:
        log.debug("ws message isn't json text=%s", message['text'])
        return

    if set(data.keys()) != set(('handle', 'message')):
        log.debug("ws message unexpected format data=%s", data)
        return

    if data:
        log.debug('chat message room=%s handle=%s message=%s',
                  room.label, data['handle'], data['message'])
        m = room.messages.create(**data)

        # See above for the note about Group
        Group('organico_cooperativas-' + label, channel_layer=message.channel_layer).send(
            {'text': json.dumps(m.as_dict())})


@channel_session
def ws_disconnect(message):
    try:
        label = message.channel_session['room']
        room = Room.objects.get(label=label)
        Group('organico_cooperativas-' + label, channel_layer=message.channel_layer).discard(message.reply_channel)
    except (KeyError, Room.DoesNotExist):
        pass
