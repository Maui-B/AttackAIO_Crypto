# AttackAIO Crypto - Unified Command-Line Interface

"""
AttackAIO Crypto - All-in-One Cryptocurrency Private Key Recovery Tool

⚠️  LEGAL WARNING ⚠️
This tool is for EDUCATIONAL purposes and recovering YOUR OWN lost passphrases ONLY.
Using this tool to access wallets you don't own is ILLEGAL and constitutes theft.

Author: PyMmdrza
Telegram: @MrPyMmdrza
Website: mmdrza.com
"""

import argparse
import sys
import os
from pathlib import Path


def print_banner():
    """Display the tool banner."""
    banner = """
    ╔═══════════════════════════════════════════════════════════╗
    ║           AttackAIO Crypto - Private Key Recovery         ║
    ║                    All-in-One Tool                        ║
    ╠═══════════════════════════════════════════════════════════╣
    ║  ⚠️  LEGITIMATE USE ONLY - YOUR WALLETS ONLY  ⚠️          ║
    ╚═══════════════════════════════════════════════════════════╝
    """
    print(banner)


def check_dependencies():
    """Check if required dependencies are installed."""
    missing = []
    
    try:
        import hdwallet
    except ImportError:
        missing.append('hdwallet')
    
    try:
        import ecdsa
    except ImportError:
        missing.append('ecdsa')
    
    try:
        import requests
    except ImportError:
        missing.append('requests')
    
    try:
        import requests_html
    except ImportError:
        missing.append('requests-html')
    
    try:
        import rich
    except ImportError:
        missing.append('rich')
    
    try:
        import colorama
    except ImportError:
        missing.append('colorama')
    
    if missing:
        print("❌ Missing dependencies:")
        for dep in missing:
            print(f"   - {dep}")
        print("\n📦 Install them with: pip install -r requirements.txt")
        return False
    
    print("✅ All dependencies are installed.")
    return True


def list_supported_coins():
    """List all supported cryptocurrencies."""
    coins = {
        'btc': 'Bitcoin (BTC)',
        'eth': 'Ethereum (ETH)',
        'doge': 'Dogecoin (DOGE)',
        'ltc': 'Litecoin (LTC)',
        'dash': 'Dash (DASH)',
        'bch': 'Bitcoin Cash (BCH)',
        'btg': 'Bitcoin Gold (BTG)',
        'zec': 'Zcash (ZEC)',
        'qtum': 'Qtum (QTUM)',
        'trx': 'Tron (TRX)',
        'dgb': 'Digibyte (DGB)'
    }
    
    print("\n📊 Supported Cryptocurrencies:")
    print("=" * 40)
    for code, name in coins.items():
        print(f"  {code:8} - {name}")
    print("=" * 40)


def validate_wordlist(filepath):
    """Validate that the wordlist file exists and is readable."""
    path = Path(filepath)
    
    if not path.exists():
        print(f"❌ Error: Wordlist file '{filepath}' not found.")
        return False
    
    if not path.is_file():
        print(f"❌ Error: '{filepath}' is not a file.")
        return False
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = sum(1 for _ in f)
        print(f"✅ Wordlist loaded: {lines} passphrases found.")
        return True
    except Exception as e:
        print(f"❌ Error reading wordlist: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description='AttackAIO Crypto - Cryptocurrency Private Key Recovery Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
⚠️  LEGAL WARNING ⚠️
This tool is for EDUCATIONAL purposes and recovering YOUR OWN lost passphrases ONLY.
Using this tool to access wallets you don't own is ILLEGAL and constitutes theft.

Examples:
  python aio.py --check-deps
  python aio.py --list-coins
  python aio.py --coin btc --wordlist mywords.txt
  python aio.py -c eth -w passwords.txt
        """
    )
    
    parser.add_argument(
        '-c', '--coin',
        type=str,
        help='Cryptocurrency to attack (e.g., btc, eth, doge)'
    )
    
    parser.add_argument(
        '-w', '--wordlist',
        type=str,
        help='Path to wordlist file (without .txt extension)'
    )
    
    parser.add_argument(
        '--check-deps',
        action='store_true',
        help='Check if all dependencies are installed'
    )
    
    parser.add_argument(
        '--list-coins',
        action='store_true',
        help='List all supported cryptocurrencies'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='AttackAIO Crypto v2.0'
    )
    
    args = parser.parse_args()
    
    print_banner()
    
    # If no arguments provided, show help
    if len(sys.argv) == 1:
        parser.print_help()
        print("\n⚠️  Remember: Only use this tool on wallets YOU OWN!")
        sys.exit(0)
    
    # Check dependencies
    if args.check_deps:
        check_dependencies()
        sys.exit(0)
    
    # List supported coins
    if args.list_coins:
        list_supported_coins()
        sys.exit(0)
    
    # Validate coin and wordlist for actual attack
    if args.coin and not args.wordlist:
        print("❌ Error: You must specify both --coin and --wordlist")
        parser.print_help()
        sys.exit(1)
    
    if args.wordlist and not args.coin:
        print("❌ Error: You must specify both --coin and --wordlist")
        parser.print_help()
        sys.exit(1)
    
    if args.coin and args.wordlist:
        # Validate inputs
        if not check_dependencies():
            sys.exit(1)
        
        if not validate_wordlist(args.wordlist + '.txt'):
            sys.exit(1)
        
        # Map coin codes to script files
        coin_scripts = {
            'btc': 'bitcoin.py',
            'eth': 'ethereum.py',
            'doge': 'doge.py',
            'ltc': 'litecoin.py',
            'dash': 'dash.py',
            'bch': 'bitcoincash.py',
            'btg': 'bitcoingold.py',
            'zec': 'zcash.py',
            'qtum': 'qtum.py',
            'trx': 'tron.py',
            'dgb': 'digibyte.py'
        }
        
        coin_lower = args.coin.lower()
        if coin_lower not in coin_scripts:
            print(f"❌ Error: Unsupported cryptocurrency '{args.coin}'")
            print("Use --list-coins to see supported cryptocurrencies.")
            sys.exit(1)
        
        script = coin_scripts[coin_lower]
        
        if not os.path.exists(script):
            print(f"❌ Error: Script '{script}' not found.")
            sys.exit(1)
        
        print(f"\n🚀 Starting attack on {coin_upper}...")
        print(f"📁 Wordlist: {args.wordlist}.txt")
        print(f"📜 Script: {script}")
        print("\n⚠️  This may take a long time depending on wordlist size.")
        print("⚠️  Remember: Only use on wallets YOU OWN!\n")
        
        # Execute the script
        os.system(f"python {script}")
    
    print("\n✅ Operation completed.")


if __name__ == "__main__":
    main()
