# Please modify the settings below according to your needs.

# List of source URLs to fetch proxy configurations from.
# Add or remove URLs as needed. All URLs in this list are automatically enabled.
SOURCE_URLS = [
    "https://raw.githubusercontent.com/mmsahvaz-org/GAFN-11/refs/heads/main/configs/proxy_configs.txt",
    "https://raw.githubusercontent.com/mmsahvaz-org/GAFN-12/refs/heads/main/configs/proxy_configs.txt",
    "https://raw.githubusercontent.com/mmsahvaz-org/GAFN-13/refs/heads/main/configs/proxy_configs.txt",
    "https://raw.githubusercontent.com/mmsahvaz-org/GAFN-14/refs/heads/main/configs/proxy_configs.txt",
    "https://raw.githubusercontent.com/mmsahvaz-org/GAFN-15/refs/heads/main/configs/proxy_configs.txt",
    "https://raw.githubusercontent.com/mmsahvaz-org/GAFN-16/refs/heads/main/configs/proxy_configs.txt",
    "https://raw.githubusercontent.com/mmsahvaz-org/GAFN-17/refs/heads/main/configs/proxy_configs.txt",
    "https://raw.githubusercontent.com/mmsahvaz-org/GAFN-18/refs/heads/main/configs/proxy_configs.txt",
    "https://raw.githubusercontent.com/mmsahvaz-org/GAFN-19/refs/heads/main/configs/proxy_configs.txt",
    "https://getafreenode.com/subscribe/?uuid=55ca7a9e-cf90-49df-b14a-9346c59b73b9",
    # Add more URLs here if you want to include additional sources.
]

# Set to True to fetch the maximum possible number of configurations.
# If True, SPECIFIC_CONFIG_COUNT will be ignored.
USE_MAXIMUM_POWER = True

# Desired number of configurations to fetch.
# This is used only if USE_MAXIMUM_POWER is False.
SPECIFIC_CONFIG_COUNT = 1000

# Dictionary of protocols to enable or disable.
# Set each protocol to True to enable, False to disable.
ENABLED_PROTOCOLS = {
    "wireguard://": False,
    "hysteria2://": True,
    "vless://": False,
    "vmess://": False,
    "ss://": False,
    "trojan://": False,
    "tuic://": False,
}

# Maximum age of configurations in days.
# Configurations older than this will be considered invalid.
MAX_CONFIG_AGE_DAYS = 365
