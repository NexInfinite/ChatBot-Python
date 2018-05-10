from collections import namedtuple
from config import oauth, nickname, channel_name
from socket import socket
from typing import List
from shlex import split
import re
import traceback
import time
import asyncio
import asynctwitch

from asynctwitch import CommandBot
from config import channel_name, nickname, oauth
from datetime import datetime, timedelta

Message = namedtuple('Message', 'user channel content')

answerq = 'anything'
youranswer = 'anything'

def question(question, a, b, c, d, answer):
    send_message(f'' + question)
    time.sleep(1)
    send_message(f'' + a)
    time.sleep(0.5)
    send_message(f'' + b)
    time.sleep(0.5)
    send_message(f'' + c)
    time.sleep(0.5)
    send_message(f'' + d)
    time.sleep(0.5)
    send_message(f'' + answer)

class Command:
    def __init__(self, name, func):
        self.func = func
        self.name = name

    def __call__(self, *args, **kwargs):
        self.func(*args, **kwargs)


def encode(text):
    return (text + '\r\n').encode('utf-8')


def decode(data):
    return data.decode('utf-8')


def send_message(data):
    send(f'PRIVMSG #{channel_name} :{data}')

def send_message_all(*messages):
    for msg in messages:
        send_message(msg)


def send(msg):
    sock.send(encode(msg))


def send_all(*messages):
    for msg in messages:
        send(msg)

def login(channel_login):
    sock.connect(('irc.chat.twitch.tv', 6667))
    send_all(f'PASS {oauth}', f'NICK {nickname}', f'JOIN #{channel_login}')

def iter_message_loop():
    while True:
        data = decode(sock.recv(1024))
        match = RE_CHANNEL_MESSAGE.match(data)

        if match is not None:
            yield Message(*match.groups())

def is_cmd(msg):
    return msg.content.startswith(COMMAND_PREFIX)


def format_message(msg):
    return f'{msg.user}({msg.channel}): {msg.content}'


def command(name=None, help=None):
    def _command(func):
        nonlocal name, help

        if name is None:
            name = func.__name__

        if help is None:
            help = f'no help is available for {name}'

        commands.append(Command(name, func))

    return _command


def handle_command(msg: Message):
    if not is_cmd(msg):
        return

    cmd_name, *args = split(msg.content)
    cmd_name = cmd_name.lower().strip()

    try:
        for c in commands:
            if c.name == cmd_name[1:]:
                print(f'{msg.user} executed command: "{c.name}" with args: {args}')
                yield c.func(msg.user, *args)
                return

    except:
        print(f'error occured while trying to execute command {cmd_name[1:]}')
        traceback.print_exc()


commands: List[Command] = []
# :userman2!userman2@userman2.tmi.twitch.tv PRIVMSG #userman2 :hello world!
RE_CHANNEL_MESSAGE = re.compile(
    r':(?P<user>[\w\d]+)!(?P=user)@(?P=user)\.tmi\.twitch\.tv PRIVMSG #(?P<channel>[\w\d]+) :(?P<content>.+)')
COMMAND_PREFIX = '!'

sock = socket()
