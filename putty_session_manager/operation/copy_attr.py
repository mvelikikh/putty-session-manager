from ..registry import utils as reg_utils
from ..format import utils as format_utils

def copy_attr(args):
    """
    Copy attributes from one session to another
    """

    reg_utils.copy_attr(from_session=args.from_session,
                        to_session_pattern=args.to_session_pattern,
                        attr_pattern=args.attr_pattern)
