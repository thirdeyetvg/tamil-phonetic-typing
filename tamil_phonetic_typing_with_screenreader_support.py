import keyboard
from time import sleep
from transliterate import azhagi
import os


key_stack = []
key_handler_map = {}

backspace_stack = []


last_output = ''
key_table = azhagi.Transliteration.table
# Temporary correction until fixed in library
key_table["kO"] = u"கோ"

def handle_keys(key):
    global last_output
    key_stack.append(key)
    stack_str = ''.join(key_stack)
    backspaces = ''
    if(stack_str not in key_table):
        key_stack.clear()
        backspace_stack.clear()
        last_output = ''
        key_stack.append(key)
        stack_str = ''.join(key_stack)
    else:
        # keyboard.write('\b'*len(last_output))
        output_length = len(last_output)
        if(output_length > 0):
            print('Deleting ' + last_output)
            backspaces = '\b' * output_length
            for char in backspaces:
                backspace_stack.append(char)
    if(stack_str in key_table):
        output = key_table[stack_str]
        last_output = output
        # print('Writing backspaces')
        keyboard.write(backspaces)
        # sleep(1)
        print('Writing output')
        keyboard.write(output)
        output_length = len(last_output)
        print(stack_str + ' > ' + output)
    else:
        keyboard.write(stack_str)

def handle_space():
    global last_output
    print(''.join(key_stack))
    key_stack.clear()
    last_output = ''
    backspace_stack.clear()

def handle_backspace():
    global last_output
    print(backspace_stack)
    if(backspace_stack):
        backspace_stack.pop()
        keyboard.write('\b')
        if not backspace_stack:
            keyboard.write(last_output)
    else:
        keyboard.write('\b')
        key_stack.clear()
        last_output = ''

def handle_alphabet_key(key):
    print('Pressed ' + key )
    handle_keys(key)


def remove_char_mapping():
    print('Removing char mapping')
    for key_handler in key_handler_map:
        keyboard.remove_hotkey(key_handler)
    key_handler_map.clear()

def init_char_mapping():
    remove_char_mapping()
    print('Setting char mapping')
    for i in range(ord('a'), ord('z')+1):
        character = chr(i)
        caps_character = chr(i-32)
        listner = keyboard.add_hotkey(character, lambda character=character: handle_alphabet_key(character), suppress=True)
        key_handler_map[character] = listner
        keyboard.add_hotkey('shift+' + character, lambda caps_character=caps_character: handle_alphabet_key(caps_character), suppress=True)
        key_handler_map['shift+' + character] = listner

    listner = keyboard.add_hotkey(' ', lambda: handle_space())
    key_handler_map[' '] = listner
    listner = keyboard.add_hotkey('\b', lambda: handle_backspace(), suppress=True)
    key_handler_map['\b'] = listner


def close_app():
    print('Removing char mapping & closing application')
    keyboard.unhook_all_hotkeys()
    os._exit(0)

def init():
    keyboard.add_hotkey('ctrl+1', lambda: init_char_mapping())
    keyboard.add_hotkey('ctrl+0', lambda: remove_char_mapping())
    keyboard.add_hotkey('ctrl+q', lambda: close_app())
    keyboard.wait()

init()