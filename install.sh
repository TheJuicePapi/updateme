#!/usr/bin/env bash
set -euo pipefail

if [[ "${EUID}" -ne 0 ]]; then
    echo "Please run as root (for example: sudo ./install.sh)" >&2
    exit 1
fi

if ! command -v apt-get >/dev/null 2>&1; then
    echo "apt-get is required. This installer is intended for Debian-based systems." >&2
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET="/usr/local/bin/updateme"

apt-get update
apt-get install -y python3
chmod +x "${SCRIPT_DIR}/updateme.py"
ln -sfn "${SCRIPT_DIR}/updateme.py" "${TARGET}"

clear
echo "Installation complete! Run 'updateme' from any directory."
