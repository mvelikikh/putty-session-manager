from ..registry import utils as reg_utils
from ..format import utils as format_utils

from ..error import InputParameterError

def get(args):
    """
    Return a single session
    """
    if args.session is None:
         raise InputParameterError('Session name must be specified')

    print(format_utils.list_to_table(
        column_names=['Name', 'Value'], 
        values=reg_utils.get_session(name=args.session)))
