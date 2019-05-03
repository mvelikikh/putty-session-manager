from ..registry import utils as reg_utils

def create(args):
    """
    Create session
    """

    reg_utils.create_session_key(
        session=args.session
    )
