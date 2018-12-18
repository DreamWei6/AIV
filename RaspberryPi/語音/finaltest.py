#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Run a recognizer using the Google Assistant Library.

The Google Assistant Library has direct access to the audio API, so this Python
code doesn't need to record audio. Hot word detection "OK, Google" is supported.

The Google Assistant Library can be installed with:
    env/bin/pip install google-assistant-library==0.0.2

It is available for Raspberry Pi 2/3 only; Pi Zero is not supported.
"""

import logging
import subprocess
import sys

import aiy.assistant.auth_helpers
import aiy.audio
import aiy.voicehat
from google.assistant.library import Assistant
from google.assistant.library.event import EventType
import serial

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
)
port = serial.Serial('/dev/ttyACM0', 9600, timeout = 3.0)

command = 'stop'

#各個狀況呼叫的方法
def power_off_pi():
    aiy.audio.say('Good bye!')
    subprocess.call('sudo shutdown now', shell=True)


def reboot_pi():
    aiy.audio.say('See you in a bit!')
    subprocess.call('sudo reboot', shell=True)


def say_ip():
    ip_address = subprocess.check_output("hostname -I | cut -d' ' -f1", shell=True)
    aiy.audio.say('My IP address is %s' % ip_address.decode('utf-8'))

#控制移動
def aiv(command_string):
    if command_string == 'go':
        aiy.audio.say('Go')
        port.write(bytes('F', 'UTF-8'))
    elif command_string == 'stop':
        aiy.audio.say('Stop')
        port.write(bytes('Q', 'UTF-8'))
    elif command_string == 'back':
        aiy.audio.say('Back')
        port.write(bytes('B', 'UTF-8'))
    elif command_string == 'right':
        aiy.audio.say('Right')
        port.write(bytes('R', 'UTF-8'))
    elif command_string == 'left':
        aiy.audio.say('Left')
        port.write(bytes('L', 'UTF-8'))


def process_event(assistant, event):
    status_ui = aiy.voicehat.get_status_ui()           #判斷目前assistant狀態
    if event.type == EventType.ON_START_FINISHED:
        status_ui.status('ready')
        if sys.stdout.isatty():
            print('Say "OK, Google" then speak, or press Ctrl+C to quit...')

    elif event.type == EventType.ON_CONVERSATION_TURN_STARTED:
        status_ui.status('listening')

    elif event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED and event.args:
        print('You said:', event.args['text'])
        text = event.args['text'].lower()
        if text == 'power off':
            assistant.stop_conversation()
            power_off_pi()
        elif text == 'reboot':
            assistant.stop_conversation()
            reboot_pi()
        elif text == 'ip address':
            assistant.stop_conversation()
            say_ip()
        elif 'stop' in text:
            assistant.stop_conversation()
            command = 'stop'
            aiv(command)
        elif 'fuck' in text:
            assistant.stop_conversation()
            command = 'stop'
            aiv(command)
        elif "don't" in text:
            assistant.stop_conversation()
            command = 'stop'
            aiv(command)
        elif 'forward' in text:
            assistant.stop_conversation()
            command = 'go'
            aiv(command)
        elif 'ahead' in text:
            assistant.stop_conversation()
            command = 'go'
            aiv(command)
        elif 'straight' in text:
            assistant.stop_conversation()
            command = 'go'
            aiv(command)
        elif 'run' in text:
            assistant.stop_conversation()
            command = 'go'
            aiv(command)
        elif 'left' in text:
            assistant.stop_conversation()
            command = 'left'
            aiv(command)
        elif 'right' in text:
            assistant.stop_conversation()
            command = 'right'
            aiv(command)
        elif 'back' in text:
            assistant.stop_conversation()
            command = 'back'
            aiv(command)


    elif event.type == EventType.ON_END_OF_UTTERANCE:
        status_ui.status('thinking')

    elif event.type == EventType.ON_CONVERSATION_TURN_FINISHED:
        status_ui.status('ready')

    elif event.type == EventType.ON_ASSISTANT_ERROR and event.args and event.args['is_fatal']:
        sys.exit(1)


def main():
    credentials = aiy.assistant.auth_helpers.get_assistant_credentials()
    with Assistant(credentials) as assistant:
        for event in assistant.start():
            process_event(assistant, event)


if __name__ == '__main__':
    main()
