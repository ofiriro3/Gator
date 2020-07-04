from enum import Enum


# probably we will need to share it with all projects
class CustomerError(Enum):
    InvalidRequest = 1,
    PermissionDenied = 2
