from enum import Enum

# Define an enumeration for Share Permission
class Permission(int, Enum):
    READ   = 0    # Read Only
    SHARE  = 1    # Share
    UPDATE = 2    # Update
    DELETE = 3    # Delete
    ADMIN  = 4    # Admin

# Define an enumeration for Task State
class State(int, Enum):
    PENDING = 0  # Task is pending
    DONE    = 1  # Task is done
    CANCEL  = 2  # Task is cancelled
    DELETE  = 3  # Task is deleted

# End of File