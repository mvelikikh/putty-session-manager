from ..registry import utils as reg_utils
from ..format import utils as format_utils

def copy(args):
    """
    Copy one session to another
    """

    reg_utils.copy(
        source=args.source,
        dest=args.dest
    )
