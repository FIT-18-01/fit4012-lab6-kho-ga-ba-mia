import sys
from pathlib import Path

# Ensure the repository root is on sys.path so tests can import top-level modules
# like aes_socket_utils, even when pytest runs from a different working directory.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
