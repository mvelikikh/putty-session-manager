# putty-session-manager
Python library and command line utility for basic management of PuTTY sessions on Windows
# Dependencies
- PrettyTable

You can install PrettyTable with the following command:

`pip install PrettyTable`
# Build & Install
Build:

`python setup.py build`

Install:

`python setup.py install`

# Run tests

`python test_putty_session_manager.py -v -b`

# Command line usage

You can invoke putty-session-manager from the commandline after installation as follows:

`python -m putty_session_manager`

Listing PuTTY sessions:

`python -m putty_session_manager list`

Getting attributes of a given session:

`python -m putty_session_manager get my_session`

Copying a session:

`python -m putty_session_manager copy source_session dest_session`

Copying attributes from one session to another:

`python -m putty_session_manager copy-attr source_session dest_session_pattern attribute_pattern`

Example:

`python -m putty_session_manager copy-attr src_session dst_sess_a.*,dst_sess_b.* Colour*`

Deleting a session:

`python -m putty_session_manager delete my_session`

You can get help by running

`python -m putty_session_manager --help`

# Prerequisites

Operating System: Microsoft Windows.

I have written it to automate common tasks of managing PuTTY sessions on Windows.
