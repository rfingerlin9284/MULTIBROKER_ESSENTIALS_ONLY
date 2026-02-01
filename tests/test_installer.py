import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
INST = ROOT / 'tools' / 'installer.py'


def test_installer_verify_only():
    rv = subprocess.run([sys.executable, str(INST), '--verify-only'])
    assert rv.returncode == 0


def test_installer_dry_run():
    rv = subprocess.run([sys.executable, str(INST), '--dry-run'])
    assert rv.returncode == 0
