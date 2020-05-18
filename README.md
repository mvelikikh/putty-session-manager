# PuTTY Session Manager
Python command line utility for basic management of PuTTY sessions on Windows

# Installation

## From PyPI

You can install `putty-session-manager` using pip:

`pip install putty-session-manager`

## From source

You can also clone the project's repository and install from source:

```
git clone https://github.com/mvelikikh/putty-session-manager
cd putty-session-manager
pip install .
```

# Usage

You can invoke putty-session-manager from the commandline after installation as follows:

`psm`
or
`python -m putty_session_manager`

Listing PuTTY sessions:

`psm list`

Getting attributes of a given session:

`psm get my_session`

Copying a session:

`psm copy source_session dest_session`

Copying attributes from one session to another:

`psm copy-attr source_session dest_session_pattern attribute_pattern`

Example:

`psm copy-attr src_session dst_sess_a.*,dst_sess_b.* Colour*`

Deleting a session:

`psm delete my_session`

You can get help by running

`psm --help`

# Prerequisites

Operating System: Microsoft Windows.

[PuTTY SSH Client](https://www.putty.org/)

I have written it to automate common tasks of managing PuTTY sessions on Windows.
