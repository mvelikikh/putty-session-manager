from ..registry import utils as reg_utils

def delete(args):
    """
    Delete session
    """

    reg_utils.delete_session(
        session=args.session
    )
