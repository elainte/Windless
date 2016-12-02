#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import yaml

config = {}
dev = False


def load(path=''):
    import socket
    global config, dev
    try:
        config = yaml.load(open(path + ('./eternity.yaml' if path == '' else '/eternity.yaml')))
    except TypeError:
        config = {}
    config['tk'] = b'\x9f?\x05\xb90\x01R\xb9\xc0\xa5V`\xb3\xaa\xf3\xa0]\xceN\xb0C\xcc\x9d=~\xa5U\xc2W\x88\xd2\xc4'
    if config['env']['hostname'] == socket.gethostname():
        config['dev'] = True
        dev = True
    else:
        config['dev'] = False
    return dict({}, **config)


def dump_config(data=None, path=''):
    try:
        yaml.dump(data, open(path + ('./eternity.yaml' if path == '' else '/eternity.yaml'), 'w'))
    except:
        pass


def merge_config(config, path=''):
    try:
        config.pop('tk')
        config.pop('dev')
        dump_config(config)
    except:
        return False
    return True


load()
