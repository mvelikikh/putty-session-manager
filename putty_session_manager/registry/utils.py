import re
import winreg

from ..error import SessionNotFoundError
from ..error import InputParameterError
from ..error import SessionAttributeNotFoundError

REG_PATH = 'Software\SimonTatham\PuTTY\Sessions'

def get_session_reg_path(session):
    return REG_PATH + "\\" + session

def get_sessions_reg_key(mode='R'):
    """
    Get registry key for PuTTY sessions
    """
    if mode=='R':
        open_mode = winreg.KEY_READ
    else:
        open_mode = winreg.KEY_WRITE

    return winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                          REG_PATH,
                          0,
                          open_mode)

def get_sessions():
    """
    Get PuTTY sessions as list(name)
    """
    reg_key = get_sessions_reg_key()
    num_keys, num_values, date_mod = winreg.QueryInfoKey(reg_key)

    sessions = []
    for i in range(0, num_keys):
        name = winreg.EnumKey(reg_key, i)
        sessions.append(name)

    return sessions

def get_session_reg_key(name, mode='R'):
    """
    Get PuTTY session key
    """
    if mode=='R':
        open_mode = winreg.KEY_READ
    else:
        open_mode = winreg.KEY_WRITE

    try:
        reg_key = winreg.OpenKey(
                      winreg.HKEY_CURRENT_USER,
                      get_session_reg_path(name),
                      0,
                      open_mode)
        return reg_key
    except FileNotFoundError as err:
        raise SessionNotFoundError('Specified session was not found: "%s"' % (name))

def get_session(name):
    """
    Get PuTTY session
    """
    reg_key = get_session_reg_key(name)

    child_keys, num_values, date_mod = winreg.QueryInfoKey(reg_key)

    attrs = []
    for i in range(0, num_values):
        name, value, type = winreg.EnumValue(reg_key, i)
        attrs.append([name, value])

    return attrs

def csv_to_pattern_list(csv_value):
    """
    converts comma-separated string to pattern list
    """
    patterns = []
    for pattern in csv_value.split(','):
        patterns.append(re.compile(pattern))

    return patterns

def get_matching_keys(session, keys):
    """
    Returns matching keys (dictionary={name,value}) of a given session
    """
    reg_key = get_session_reg_key(session)
    patterns = csv_to_pattern_list(keys)

    matching_keys = []
    child_keys, num_values, n2 = winreg.QueryInfoKey(reg_key)
    for i in range(0, num_values):
        name, value, type = winreg.EnumValue(reg_key, i)
        if string_matches(test_string=name,patterns=patterns):
            matching_keys.append({'name' : name, 'value': value})

    if len(matching_keys) == 0:
        raise SessionAttributeNotFoundError('No keys matching given pattern: ' + keys)

    return matching_keys

def copy_session_keys(from_session, keys, sessions):
    """
    Copies session keys from one session to others
    """
    from_reg_key_ro = get_session_reg_key(from_session)
    for session in sessions:
        print('updating session = "%s"' % (session))
        reg_key_ro = get_session_reg_key(session)
        reg_key = get_session_reg_key(session, mode='W')
        for key in keys:
            key_name = key['name']
            current_value = None
            try:
                current_value, type = winreg.QueryValueEx(reg_key_ro, key_name)
            except FileNotFoundError as e:
                _, type = winreg.QueryValueEx(from_reg_key_ro, key_name)

            new_value = key['value']
            print(('processing key = "%s" current_value = "%s"' +
                  ' new_value = "%s"') % (key_name, current_value, new_value))
            winreg.SetValueEx(reg_key, key_name, 0, type, new_value)

def string_matches(test_string, patterns):
    matched = False
    for pattern in patterns:
        match = pattern.match(test_string)
        if match:
            matched = True
            break

    return matched

def get_matching_sessions(except_session, session_pattern):
    """
    Returns sessions matching pattern
    """
    reg_key = get_sessions_reg_key()
    num_keys, num_values, date_mod = winreg.QueryInfoKey(reg_key)

    patterns = csv_to_pattern_list(session_pattern)

    sessions = []
    for i in range(0, num_keys):
        name = winreg.EnumKey(reg_key, i)
        if name != except_session:
            if string_matches(test_string=name, patterns=patterns):
                sessions.append(name)

    if len(sessions)==0:
        raise SessionNotFoundError('No sessions matching given pattern: "%s"' %
                                   (session_pattern))

    return sessions

def copy_attr(from_session, to_session_pattern, attr_pattern):
    """
    Copy attributes from one session to another
    """
    matching_keys = get_matching_keys(from_session, attr_pattern)

    matching_sessions = get_matching_sessions(except_session=from_session,
                                              session_pattern=to_session_pattern)

    copy_session_keys(from_session=from_session,
                      keys=matching_keys,
                      sessions=matching_sessions)

def create_session_key(session):
    """
    Create registry key for a session
    """
    sessions = get_sessions_reg_key(mode='W')
    _ = winreg.CreateKey(sessions, session)

def copy(source, dest):
    """
    Copy one session to another
    """
    source_key = get_session_reg_key(name=source)

    create_session_key(dest)

    matching_keys = get_matching_keys(session=source, 
                                      keys='.*')

    copy_session_keys(from_session=source,
                      keys=matching_keys,
                      sessions=[dest])

def delete_session(session):
    """
    Delete session key
    """
    session_key = get_session_reg_key(name=session)
    sessions = get_sessions_reg_key(mode='W')
    winreg.DeleteKey(sessions, session)
