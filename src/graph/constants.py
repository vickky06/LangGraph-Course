"""Constants used in graph definitions."""
from enum import Enum, auto

class GraphNodes(str, Enum):
    """Enum for graph node names."""
    AGENT_REASON = "agent_reason"
    ACT = "act"
    END = "end"

# Index constants
LAST = -1
