#!/usr/bin/env python3
"""
A simple command-line tool to install Python libraries easily.

Usage examples:
---------------
1️⃣  Interactive mode:
    python cmd_installer.py

2️⃣  Command-line mode:
    python cmd_installer.py numpy pandas matplotlib

3️⃣  Help:
    python cmd_installer.py --help
"""

import subprocess
import sys
import argparse
from importlib import util

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    # Colorama not installed? Fall back to no color
    class ColorFallback:
        def __getattr__(self, _):
            return ""
    Fore = Style = ColorFallback()

def is_installed(package_name: str) -> bool:
    """Check if a package is already installed."""
    return util.find_spec(package_name) is not None

def install_package(package_name: str):
    """Install a single Python package using pip."""
    if is_installed(package_name):
        print(f"{Fore.YELLOW}⚠️  {package_name} is already installed.")
        return

    try:
        print(f"{Fore.CYAN}🔍 Installing {package_name} ...{Style.RESET_ALL}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"{Fore.GREEN}✅ Successfully installed {package_name}{Style.RESET_ALL}\n")
    except subprocess.CalledProcessError:
        print(f"{Fore.RED}❌ Failed to install {package_name}{Style.RESET_ALL}\n")

def install_packages(packages: list[str]):
    """Install multiple packages."""
    for pkg in packages:
        install_package(pkg)

def main():
    parser = argparse.ArgumentParser(
        description="💻 Simple CMD-based Python library installer"
    )
    parser.add_argument(
        "packages",
        nargs="*",
        help="Name(s) of the package(s) to install (space-separated). Leave empty for interactive mode."
    )
    args = parser.parse_args()

    if args.packages:
        install_packages(args.packages)
    else:
        print(f"{Fore.CYAN}🔧 Welcome to the Python CMD Installer!{Style.RESET_ALL}")
        while True:
            user_input = input("\nEnter library names (or 'exit' to quit): ").strip()
            if user_input.lower() in ["exit", "quit"]:
                print(f"{Fore.GREEN}👋 Goodbye!{Style.RESET_ALL}")
                break
            if not user_input:
                continue
            packages = user_input.split()
            install_packages(packages)

if __name__ == "__main__":
    main()
