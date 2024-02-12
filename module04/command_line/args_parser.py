import argparse

parser = argparse.ArgumentParser(description='Todo APP')
parser.add_argument('--action', help='Command: create, update, list, remove', required=True)
parser.add_argument('--id')
parser.add_argument('--title')
parser.add_argument('--desc')
parser.add_argument('--login')

arguments = dict(parser.parse_args())
# print(arguments)
my_arg = vars(arguments)

{
    "action": "add",
    "id": "21"
}
# print(my_arg)

action = my_arg.get('action')
title = my_arg.get('title')
description = my_arg.get('desc')
_id = my_arg.get('id')
login = my_arg.get('login')

print(action, title)