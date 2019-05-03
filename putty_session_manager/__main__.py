import argparse
import sys

from . import operations as ops

def cmdline_main():
    """It is run when invoking the module via the commandline.
    """

    parser = argparse.ArgumentParser(
        description="Command Line utility to manage PuTTY sessions"
    )

    subparsers = parser.add_subparsers(
        description="Available commands"
    )

    parser_create = subparsers.add_parser(
        'create',
        help="Initialize empty session")

    parser_create.add_argument(
        'session',
        metavar="<session>",
        help="Session name")

    parser_create.set_defaults(func=ops.create)

    parser_list = subparsers.add_parser(
        'list',
        aliases=["ls"],
        help="Print PuTTY sessions")

    parser_list.set_defaults(func=ops.list)

    parser_get = subparsers.add_parser(
        'get',
        help="Print attributes of a given session"
    )

    parser_get.add_argument(
        'session',
        metavar="<session>",
        help="Session to work with"
    )

    parser_get.set_defaults(func=ops.get_operation('get'))

    parser_copy_attr = subparsers.add_parser(
        'copy-attr',
        help="Copy attributes from one session to another"
    )

    parser_copy_attr.add_argument(
        'from_session',
        metavar="<from_session>",
        help="Session to copy attributes from"
    )

    parser_copy_attr.add_argument(
        'to_session_pattern',
        metavar="<to_session_pattern>",
        help="Session(s) to copy attributes to. Supports regular expressions"
    )

    parser_copy_attr.add_argument(
        'attr_pattern',
        metavar="<attr_pattern>",
        help="Specify attributes to copy. Supports regular expressions"
    )

    parser_copy_attr.set_defaults(func=ops.get_operation('copy-attr'))

    parser_copy = subparsers.add_parser(
        'copy',
        aliases=["cp"],
        help="Create a new session by copying a given one"
    )

    parser_copy.add_argument(
        'source',
        metavar="<source>",
        help="Source session to copy"
    )

    parser_copy.add_argument(
        'dest',
        metavar="<dest>",
        help="Destination session. If it exists, it will be overwritten"
    )

    parser_copy.set_defaults(func=ops.get_operation('copy'))

    parser_delete = subparsers.add_parser(
        'delete',
        aliases=["rm"],
        help="Delete a session"
    )

    parser_delete.add_argument(
        'session',
        metavar="<session>",
        help="Session to delete"
    )

    parser_delete.set_defaults(func=ops.get_operation('delete'))

    if len(sys.argv)==1:
        input_args = [ops.get_default_operation()]
    else:
        input_args = sys.argv[1:]

    args = parser.parse_args(input_args)

    args.func(args)

if __name__ == "__main__":
    try:
        cmdline_main()
    except Exception as err:
        sys.exit("%s: %s" % (err.__class__.__name__, err))
