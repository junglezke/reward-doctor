"""reward-doctor -- find out what your reward function actually accepts.

    from reward_doctor import audit
    from my_project import my_reward_fn

    audit(my_reward_fn).print()
"""

from .audit import Audit, Outcome, audit
from .case import Case
from .corpus import ALL_CASES, load
from .reference import REFERENCE_VERIFIERS

__version__ = "0.2.0"

__all__ = [
    "ALL_CASES",
    "Audit",
    "Case",
    "Outcome",
    "REFERENCE_VERIFIERS",
    "__version__",
    "audit",
    "load",
]
