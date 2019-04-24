from ..registry import utils as reg_utils
from ..format import utils as format_utils

from ..error import InputParameterError

def list(args):
    """
    Displays current PuTTY sessions
    """

    print(format_utils.list_to_table(
        column_names=['Session'], 
        values=reg_utils.get_sessions()))
