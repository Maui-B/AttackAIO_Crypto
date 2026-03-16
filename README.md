# Attack AIO Crypto

![Attack AIO Crypto](https://github.com/Pymmdrza/AttackAIO_Crypto/raw/mainx/aioattack2.jpg 'Attack AIO Crypto')

---

## ⚠️ IMPORTANT LEGAL WARNING ⚠️

**This tool is for EDUCATIONAL purposes and recovering YOUR OWN lost passphrases ONLY.**

- ✅ **Legitimate Use**: Recovering your own lost cryptocurrency wallet passphrases
- ✅ **Educational**: Learning about cryptographic key derivation and brain wallet vulnerabilities
- ❌ **ILLEGAL**: Attempting to access wallets you do not own
- ❌ **THEFT**: Using this tool on addresses without explicit ownership authorization

**Using this software to access wallets without authorization is ILLEGAL and constitutes THEFT under criminal law in most jurisdictions. Violators may face severe legal consequences including imprisonment and fines.**

By using this software, you acknowledge that:
1. You will only use it on wallets **YOU OWN**
2. You understand the legal implications of unauthorized access
3. You accept full responsibility for your actions

---

## Overview

**Attack AIO Crypto** (All-In-One) is a cryptocurrency private key recovery tool that attempts to recover wallet private keys from passphrase/word lists (brain wallets).

### Author
- **Developer**: PyMmdrza
- **Telegram**: [@MrPyMmdrza](https://t.me/MrPyMmdrza)
- **Website**: [mmdrza.com](https://mmdrza.com)
- **Channel**: [@Cryptoixer](https://t.me/Cryptoixer)

---

## 🚀 Quick Start

### Installation

#### Option 1: Automated Installer (Recommended)

**Linux/Mac:**
```bash
chmod +x install.sh
./install.sh
```

**Windows:**
```batch
install.bat
```

#### Option 2: Manual Installation

1. **Update pip:**
   ```bash
   # Windows
   python -m pip install --upgrade pip
   
   # Linux/Mac
   python3 -m pip install --upgrade pip
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Usage

#### New Unified CLI (Recommended)

```bash
# Check dependencies
python aio.py --check-deps

# List supported cryptocurrencies
python aio.py --list-coins

# Run attack on Bitcoin with wordlist
python aio.py --coin btc --wordlist words

# Run attack on Ethereum
python aio.py -c eth -w passwords
```

#### Traditional Method

Run individual scripts directly:

```bash
# Bitcoin
python bitcoin.py

# Ethereum
python ethereum.py

# Dogecoin
python doge.py

# And more...
```

---

## Supported Cryptocurrencies

| Code | Cryptocurrency | Script |
|------|---------------|--------|
| BTC | Bitcoin | `bitcoin.py` |
| ETH | Ethereum | `ethereum.py` |
| DOGE | Dogecoin | `doge.py` |
| LTC | Litecoin | `litecoin.py` |
| DASH | Dash | `dash.py` |
| BCH | Bitcoin Cash | `bitcoincash.py` |
| BTG | Bitcoin Gold | `bitcoingold.py` |
| ZEC | Zcash | `zcash.py` |
| QTUM | Qtum | `qtum.py` |
| TRX | Tron | `tron.py` |
| DGB | Digibyte | `digibyte.py` |

### Bitcoin Address Types Supported

- P2PKH (Pay-to-Public-Key-Hash)
- P2SH (Pay-to-Script-Hash)
- P2WPKH (Pay-to-Witness-Public-Key-Hash)
- P2WSH (Pay-to-Witness-Script-Hash)
- P2WSH-in-P2SH
- P2WPKH-in-P2SH

---

## How It Works

1. **Input**: User provides a text file containing word lists/passphrases to test
2. **Key Generation**: Each passphrase is hashed (SHA-256) to generate a private key
3. **Address Derivation**: Private keys are converted to public keys and then to wallet addresses
4. **Balance Checking**: The tool queries blockchain explorers (e.g., trezor.io APIs) to check if any generated address has a balance
5. **Output**: If a balance is found, the passphrase, private key, and address are saved to a file

---

## Requirements

- Python 3.8 or higher
- Required packages (see `requirements.txt`):
  - `hdwallet` - Hierarchical Deterministic wallet operations
  - `ecdsa` - Elliptic Curve Digital Signature Algorithm
  - `requests` & `requests-html` - HTTP requests and web scraping
  - `rich` - Terminal formatting
  - `colorama` - Cross-platform colored terminal output
  - `bit` - Bitcoin library

---

## File Structure

```
AttackAIO_Crypto/
├── aio.py                 # Unified command-line interface (NEW!)
├── requirements.txt       # Python dependencies
├── install.sh            # Linux/Mac installer
├── install.bat           # Windows installer
├── LICENSE               # MIT License with legal notice
├── README.md             # This file
├── words.txt.example     # Example wordlist template
├── *.py                  # Individual coin scripts
├── *.cmd                 # Windows batch launchers
├── Bitcoin/              # Dedicated Bitcoin scripts
├── BatchAttack/          # Batch execution scripts
└── media/                # Screenshots and demos
```

---

## Examples

### Running Bitcoin Attack

```bash
# Create your wordlist
echo "my_secret_passphrase" > words.txt
echo "another_password" >> words.txt

# Run the attack
python bitcoin.py
# When prompted, enter: words
```

### Using the Unified CLI

```bash
# Check if everything is set up correctly
python aio.py --check-deps

# Run Bitcoin attack
python aio.py -c btc -w words

# Run Ethereum attack  
python aio.py --coin eth --wordlist mypasswords
```

### Batch Processing (Windows)

```batch
00BatchAttack.bat
```

---

## Demos

### Bitcoin Attack Demo
[![asciicast](https://asciinema.org/a/548828.svg)](https://asciinema.org/a/548828)

### Bitcoin Gold Demo
[![Bitcoin Gold screen recorder](https://asciinema.org/a/548836.svg)](https://asciinema.org/a/548836)

### Dash Demo
[![asciicast](https://asciinema.org/a/548835.svg)](https://asciinema.org/a/548835)

### Dogecoin Demo
[![asciicast](https://asciinema.org/a/548830.svg)](https://asciinema.org/a/548830)

---

## ⚠️ Security Warnings

### Beware of Scammers

> Unfortunately, due to the ignorance of some users, we have been informed that some profiteers are selling fake versions of these scripts at lower prices. Users do not receive anything after payment, and some receive malicious/viral files instead.

**The only official sources are:**
- Website: [mmdrza.com](https://mmdrza.com)
- Telegram ID: [@MrPyMmdrza](https://t.me/MrPyMmdrza)
- Telegram Channel: [@Cryptoixer](https://t.me/Cryptoixer)

### Important Considerations

1. **Low Success Rate**: Brain wallet attacks have extremely low success rates against properly generated random passphrases
2. **Time Consuming**: Large wordlists can take days, weeks, or months to process
3. **Rate Limiting**: Blockchain API calls may be rate-limited
4. **Network Dependent**: Requires stable internet connection for balance checking

---

## Legal Disclaimer

This software is provided "as is" for educational purposes only. The authors and contributors:

- Are **NOT** responsible for any misuse or illegal activities
- Do **NOT** condone unauthorized access to cryptocurrency wallets
- Will **NOT** be held liable for any damages resulting from use of this software

Users are solely responsible for ensuring their use complies with all applicable laws in their jurisdiction.

**Unauthorized access to cryptocurrency wallets is a serious crime that can result in:**
- Criminal prosecution
- Imprisonment
- Heavy fines
- Civil liability

---

## Contributing

Contributions should follow these guidelines:
1. Only submit improvements that enhance legitimate use cases
2. Include appropriate legal warnings in new code
3. Test thoroughly before submitting
4. Respect the educational purpose of this project

---

## Support

- **Telegram**: [@MrPyMmdrza](https://t.me/MrPyMmdrza)
- **Discord**: [Join Server](https://discord.gg/FQNxnVJM3U)
- **Website**: [mmdrza.com](https://mmdrza.com)

---

## License

MIT License - See [LICENSE](LICENSE) file for details.

**Remember: This tool is for recovering YOUR OWN lost passphrases ONLY!**

---

```
 ██████╗ ██████╗ ███╗   ███╗    ███╗   ███╗   ███╗███╗   ███╗██████╗ ██████╗ ███████╗ █████╗    
██╔════╝██╔═══██╗████╗ ████║    ████╗ ████║   ██╔╝    ██╔╝██╔══██╗██╔══██╗╚══███╔╝██╔══██╗   
██║     ██║   ██║██╔████╔██║    ██╔████╔██║   ██║     ██║ ██║  ██║██████╔╝  ███╔╝ ███████║   
██║     ██║   ██║██║╚██╔╝██║    ██║╚██╔╝██║   ██║     ██║ ██║  ██║██╔══██╗ ███╔╝  ██╔══██║   
╚██████╗╚██████╔╝██║ ╚═╝ ██║    ██║ ╚═╝ ██║   ██║     ██║ ╚██████╔╝██║  ██║███████╗██║  ██║██╗
 ╚═════╝ ╚═════╝ ╚═╝     ╚═╝    ╚═╝     ╚═╝   ╚═╝     ╚═╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝
  Programmer Mmdrza.Com ~ Telegram Channel @mPython3 ~ ID Telegram @MrPyMmdrza ~ https://Mmdrza.Com
```
