from .operation import *

LIST_OPERATION = 'list'
GET_OPERATION = 'get'
COPY_ATTR_OPERATION = 'copy-attr'
COPY_OPERATION = 'copy'
DELETE_OPERATION = 'delete'

DEFAULT_OPERATION = LIST_OPERATION

_OPERATION_FUNCS = {
    LIST_OPERATION: list,
    GET_OPERATION: get,
    COPY_ATTR_OPERATION: copy_attr,
    COPY_OPERATION: copy,
    DELETE_OPERATION: delete
}

def get_operation(specified_operation):
    return _OPERATION_FUNCS[specified_operation]

def get_default_operation():
    return DEFAULT_OPERATION
