from app.utils.config_loader import load_config

# Load configuration once during module import
config = load_config()

def calculate_demurrage_and_detention_fees(days_on_terminal: int, days_with_consignee: int):
    """
    Calculate demurrage and detention fees based on the number of days a container
    spends on terminal and with consignee.

    Parameters:
    - days_on_terminal (int): The number of days the container is on the terminal.
    - days_with_consignee (int): The number of days the container is with the consignee.

    Returns:
    - Tuple[float, float]: A tuple containing the demurrage fee and detention fee.
    """
    demurrage_fee = calculate_fee(
        days=days_on_terminal,
        rates=config['demurrage']['rates']
    )

    detention_fee = calculate_fee(
        days=days_with_consignee,
        rates=config['detention']['rates']
    )

    return demurrage_fee, detention_fee

def calculate_fee(days: int, rates: list):
    """
    Calculate the fee based on the number of days and rate tiers.

    Parameters:
    - days (int): The number of days to calculate the fee for.
    - rates (list): A list of rate tiers, each containing 'from', 'till', and 'rate'.

    Returns:
    - float: The calculated fee.
    """
    fee = 0
    for rate_tier in rates:
        # If the 'till' value is None, consider it as no upper limit
        upper_limit = rate_tier['till'] if rate_tier['till'] is not None else float('inf')
        lower_limit = rate_tier['from']
        rate = rate_tier['rate']

        # Determine how many days fall within the current tier
        if days > lower_limit:
            days_in_tier = min(days, upper_limit) - lower_limit + 1
            fee += days_in_tier * rate

    return fee
